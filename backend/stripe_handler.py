"""Stripe webhook event handlers for Flaco AI.

This handler issues licenses durably and is safe under Stripe retries.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import stripe

from backend.license_store import LicenseStore


class StripeWebhookHandler:
    """Handle Stripe webhook events and manage license lifecycle."""

    _ACCEPTED_PAYMENT_STATUSES = {"paid", "no_payment_required"}
    _DEFAULT_ISSUANCE_DEDUP_SECONDS = 6 * 60 * 60  # 6 hours

    def __init__(self, license_generator, email_sender, license_store: LicenseStore):
        self.license_generator = license_generator
        self.email_sender = email_sender
        self.license_store = license_store
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _mask_email(value: Optional[str]) -> str:
        value = (value or "").strip()
        if "@" not in value:
            return "***"
        local, domain = value.split("@", 1)
        if not local:
            return f"***@{domain}"
        keep = local[:2]
        return f"{keep}***@{domain}"

    def handle_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Route event to appropriate handler with durable idempotency."""
        event_type = event.get("type", "unknown")
        event_id = event.get("id", "unknown")

        if self.license_store.is_event_processed(event_id):
            self.logger.warning(f"[Event {event_id}] Already processed, skipping (DB idempotency)")
            return {"success": True, "message": f"Event {event_id} already processed", "idempotent": True}

        self.logger.info(f"[Event {event_id}] Processing event type: {event_type}")

        handlers = {
            "checkout.session.completed": self._handle_checkout_completed,
            "customer.subscription.created": self._handle_subscription_created,
            "customer.subscription.updated": self._handle_subscription_updated,
            "customer.subscription.deleted": self._handle_subscription_deleted,
            "invoice.payment_succeeded": self._handle_payment_succeeded,
            "invoice.payment_failed": self._handle_payment_failed,
        }

        handler = handlers.get(event_type)
        if not handler:
            self.logger.info(f"[Event {event_id}] Unhandled event type: {event_type}")
            return {"success": True, "message": f"Ignored event: {event_type}"}

        result = handler(event)
        if result.get("success"):
            self.license_store.mark_event_processed(event_id)
        return result

    def _extract_email_from_session(self, session: Dict[str, Any]) -> Optional[str]:
        session_id = session.get("id", "unknown")

        email = (session.get("customer_details") or {}).get("email")
        if email:
            self.logger.info(f"[Session {session_id}] Email from customer_details: {self._mask_email(email)}")
            return email

        email = session.get("customer_email")
        if email:
            self.logger.info(f"[Session {session_id}] Email from customer_email: {self._mask_email(email)}")
            return email

        customer_id = session.get("customer")
        if customer_id:
            try:
                self.logger.info(f"[Session {session_id}] Fetching email from customer {customer_id}")
                customer = stripe.Customer.retrieve(customer_id)
                email = customer.get("email")
                if email:
                    self.logger.info(f"[Session {session_id}] Email from Customer object: {self._mask_email(email)}")
                    return email
            except Exception as e:
                self.logger.warning(
                    f"[Session {session_id}] Failed to retrieve customer {customer_id}: {type(e).__name__}: {e}"
                )

        self.logger.error(f"[Session {session_id}] Could not extract email from any source!")
        return None

    def _handle_checkout_completed(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle checkout.session.completed.

        For $0 invoices (100% discount), this is often the only reliable event.
        """
        session = event["data"]["object"]
        session_id = session.get("id")

        mode = session.get("mode")
        payment_status = session.get("payment_status")

        if mode and mode != "subscription":
            self.logger.info(f"[Session {session_id}] Non-subscription checkout (mode={mode}). Skipping.")
            return {"success": True, "message": f"Ignored non-subscription checkout: {mode}", "session_id": session_id}

        if payment_status and payment_status not in self._ACCEPTED_PAYMENT_STATUSES:
            self.logger.warning(
                f"[Session {session_id}] Checkout completed but payment_status={payment_status}. Not issuing license yet."
            )
            return {
                "success": True,
                "message": f"Checkout completed but not payable yet (payment_status={payment_status})",
                "session_id": session_id,
            }

        customer_email = self._extract_email_from_session(session)
        if not customer_email:
            return {"success": False, "error": f"No customer email found in session {session_id}", "session_id": session_id}

        subscription_id = session.get("subscription")
        metadata = session.get("metadata") or {}

        tier = metadata.get("tier", "pro")
        billing = metadata.get("billing", "monthly")

        if not subscription_id:
            return {"success": False, "error": f"Missing subscription_id in checkout session {session_id}", "session_id": session_id}

        existing = self.license_store.get_license(subscription_id)
        if existing:
            expires = datetime.fromisoformat(existing.expires_iso)
            if existing.email_sent_at:
                return {
                    "success": True,
                    "message": "License already issued (email previously sent)",
                    "session_id": session_id,
                    "subscription_id": subscription_id,
                    "idempotent": True,
                }

            email_sent = self.email_sender.send_license_key_email(
                to_email=existing.customer_email,
                license_key=existing.license_key,
                tier=existing.tier,
                expires=expires,
            )
            if email_sent:
                self.license_store.mark_license_email_sent(subscription_id)

            return {
                "success": bool(email_sent),
                "message": "Existing license emailed" if email_sent else "Failed to email existing license",
                "session_id": session_id,
                "subscription_id": subscription_id,
                "idempotent": True,
            }

        # If Stripe created a second subscription/checkout accidentally for the same user/tier,
        # do not mint a fresh key immediately. Reuse the most recent issued license for a short window.
        try:
            dedup_seconds = int(os.getenv("LICENSE_ISSUANCE_DEDUP_SECONDS") or self._DEFAULT_ISSUANCE_DEDUP_SECONDS)
        except Exception:
            dedup_seconds = self._DEFAULT_ISSUANCE_DEDUP_SECONDS

        recent = self.license_store.get_latest_license_for_email_and_tier(customer_email, tier)
        if recent:
            try:
                recent_created = datetime.fromisoformat(recent.created_at)
            except Exception:
                recent_created = None

            if recent_created and (datetime.utcnow() - recent_created).total_seconds() <= max(0, dedup_seconds):
                # Create a row for this new subscription_id pointing at the same license payload.
                stored, _created = self.license_store.create_license_if_missing(
                    subscription_id=subscription_id,
                    customer_email=recent.customer_email,
                    tier=recent.tier,
                    billing=recent.billing,
                    license_key=recent.license_key,
                    expires_iso=recent.expires_iso,
                )

                # Avoid spamming: if we already sent a license email recently, don't send again.
                if recent.email_sent_at:
                    return {
                        "success": True,
                        "message": "Recent license already issued for this user/tier (deduped)",
                        "session_id": session_id,
                        "subscription_id": subscription_id,
                        "idempotent": True,
                    }

                expires = datetime.fromisoformat(stored.expires_iso)
                email_sent = self.email_sender.send_license_key_email(
                    to_email=stored.customer_email,
                    license_key=stored.license_key,
                    tier=stored.tier,
                    expires=expires,
                )
                if email_sent:
                    self.license_store.mark_license_email_sent(subscription_id)

                return {
                    "success": bool(email_sent),
                    "message": "Deduped license emailed" if email_sent else "Failed to email deduped license",
                    "session_id": session_id,
                    "subscription_id": subscription_id,
                    "idempotent": True,
                }

        expires = datetime.now() + (timedelta(days=365) if billing == "annual" else timedelta(days=35))

        license_key = self.license_generator.generate_license_key(email=customer_email, tier=tier, expires=expires)

        stored, created = self.license_store.create_license_if_missing(
            subscription_id=subscription_id,
            customer_email=customer_email,
            tier=tier,
            billing=billing,
            license_key=license_key,
            expires_iso=expires.isoformat(),
        )

        if not created:
            expires = datetime.fromisoformat(stored.expires_iso)
            license_key = stored.license_key

        email_sent = self.email_sender.send_license_key_email(
            to_email=customer_email,
            license_key=license_key,
            tier=tier,
            expires=expires,
        )

        if not email_sent:
            return {
                "success": False,
                "error": "Email sending failed (check logs)",
                "session_id": session_id,
                "subscription_id": subscription_id,
            }

        self.license_store.mark_license_email_sent(subscription_id)

        return {
            "success": True,
            "message": f"License key sent to {customer_email}",
            "session_id": session_id,
            "subscription_id": subscription_id,
        }

    def _handle_subscription_created(self, event: Dict[str, Any]) -> Dict[str, Any]:
        subscription = event["data"]["object"]
        subscription_id = subscription.get("id")
        status = subscription.get("status")
        self.logger.info(f"Subscription created: {subscription_id}, status={status}")
        return {"success": True, "message": f"Subscription {subscription_id} created"}

    def _handle_subscription_updated(self, event: Dict[str, Any]) -> Dict[str, Any]:
        subscription = event["data"]["object"]
        subscription_id = subscription.get("id")
        status = subscription.get("status")
        self.logger.info(f"Subscription updated: {subscription_id}, status={status}")
        return {"success": True, "message": f"Subscription {subscription_id} updated"}

    def _handle_subscription_deleted(self, event: Dict[str, Any]) -> Dict[str, Any]:
        subscription = event["data"]["object"]
        subscription_id = subscription.get("id")
        self.logger.info(f"Subscription deleted: {subscription_id}")
        return {"success": True, "message": f"Subscription {subscription_id} deleted"}

    def _handle_payment_succeeded(self, event: Dict[str, Any]) -> Dict[str, Any]:
        invoice = event["data"]["object"]
        subscription_id = invoice.get("subscription")
        amount_paid = invoice.get("amount_paid", 0)
        self.logger.info(f"Payment succeeded: ${amount_paid/100:.2f} for subscription {subscription_id}")
        return {"success": True, "message": f"Payment processed for {subscription_id}"}

    def _handle_payment_failed(self, event: Dict[str, Any]) -> Dict[str, Any]:
        invoice = event["data"]["object"]
        subscription_id = invoice.get("subscription")
        attempt_count = invoice.get("attempt_count")
        self.logger.warning(f"Payment failed for {subscription_id}, attempt {attempt_count}")
        return {"success": True, "message": f"Payment failed for {subscription_id}"}
