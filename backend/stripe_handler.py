"""Stripe webhook event handlers for Flaco AI."""

import logging
import stripe
from datetime import datetime, timedelta
from typing import Dict, Any, Optional


class StripeWebhookHandler:
    """Handle Stripe webhook events and manage license lifecycle."""

    def __init__(self, license_generator, email_sender):
        """Initialize webhook handler.

        Args:
            license_generator: LicenseKeyGenerator instance
            email_sender: EmailSender instance
        """
        self.license_generator = license_generator
        self.email_sender = email_sender
        self.logger = logging.getLogger(__name__)

        # TODO: Replace with actual database for production
        # This is a temporary in-memory store for idempotency
        # In production, use PostgreSQL/MySQL with unique constraints
        self._processed_sessions = set()

    def handle_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Route event to appropriate handler.

        Args:
            event: Stripe event object

        Returns:
            Result dict with success status
        """
        event_type = event["type"]
        event_id = event.get("id", "unknown")

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

        if handler:
            try:
                return handler(event)
            except Exception as e:
                self.logger.error(
                    f"[Event {event_id}] Handler exception for {event_type}: {type(e).__name__}: {e}",
                    exc_info=True
                )
                # Re-raise to ensure webhook returns 500 and Stripe retries
                raise
        else:
            self.logger.info(f"[Event {event_id}] Unhandled event type: {event_type}")
            return {"success": True, "message": f"Ignored event: {event_type}"}

    def _extract_email_from_session(self, session: Dict[str, Any]) -> Optional[str]:
        """Extract customer email from Stripe session with multiple fallbacks.

        Args:
            session: Stripe checkout session object

        Returns:
            Customer email or None
        """
        session_id = session.get("id", "unknown")

        # Primary: customer_details.email (Stripe Checkout v3)
        email = session.get("customer_details", {}).get("email")
        if email:
            self.logger.info(f"[Session {session_id}] Email from customer_details: {email}")
            return email

        # Fallback 1: customer_email (legacy)
        email = session.get("customer_email")
        if email:
            self.logger.info(f"[Session {session_id}] Email from customer_email: {email}")
            return email

        # Fallback 2: Fetch from Customer object
        customer_id = session.get("customer")
        if customer_id:
            try:
                self.logger.info(f"[Session {session_id}] Fetching email from customer {customer_id}")
                customer = stripe.Customer.retrieve(customer_id)
                email = customer.get("email")
                if email:
                    self.logger.info(f"[Session {session_id}] Email from Customer object: {email}")
                    return email
            except Exception as e:
                self.logger.warning(
                    f"[Session {session_id}] Failed to retrieve customer {customer_id}: {e}"
                )

        self.logger.error(f"[Session {session_id}] Could not extract email from any source!")
        return None

    def _handle_checkout_completed(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle checkout.session.completed event.

        This fires when a customer completes checkout and payment is successful.
        For subscriptions with 100% discount codes, this is the ONLY reliable event.
        """
        session = event["data"]["object"]
        session_id = session.get("id")

        self.logger.info(f"[Session {session_id}] === CHECKOUT COMPLETED ===")
        self.logger.info(f"[Session {session_id}] Session mode: {session.get('mode')}")
        self.logger.info(f"[Session {session_id}] Payment status: {session.get('payment_status')}")

        # Idempotency check (in production, use database with unique constraint)
        if session_id in self._processed_sessions:
            self.logger.warning(f"[Session {session_id}] Already processed, skipping (idempotency)")
            return {
                "success": True,
                "message": f"Session {session_id} already processed",
                "idempotent": True
            }

        # Extract customer email with fallbacks
        customer_email = self._extract_email_from_session(session)

        if not customer_email:
            error_msg = f"No customer email found in session {session_id}"
            self.logger.error(f"[Session {session_id}] {error_msg}")
            self.logger.error(f"[Session {session_id}] Session data: {session}")
            return {
                "success": False,
                "error": error_msg,
                "session_id": session_id
            }

        # Extract metadata
        customer_id = session.get("customer")
        subscription_id = session.get("subscription")
        metadata = session.get("metadata", {})

        tier = metadata.get("tier", "pro")
        billing = metadata.get("billing", "monthly")

        self.logger.info(
            f"[Session {session_id}] Customer: {customer_email}, "
            f"Tier: {tier}, Billing: {billing}, "
            f"Customer ID: {customer_id}, Subscription ID: {subscription_id}"
        )

        # Generate license key
        # Expiry: 1 year for annual, 1 month + grace period for monthly
        if billing == "annual":
            expires = datetime.now() + timedelta(days=365)
        else:
            expires = datetime.now() + timedelta(days=35)  # 30 days + 5 day grace

        self.logger.info(f"[Session {session_id}] Generating license key...")

        try:
            license_key = self.license_generator.generate_license_key(
                email=customer_email,
                tier=tier,
                expires=expires
            )
            self.logger.info(
                f"[Session {session_id}] License key generated: {license_key[:15]}... "
                f"(expires: {expires.strftime('%Y-%m-%d')})"
            )
        except Exception as e:
            self.logger.error(
                f"[Session {session_id}] License generation failed: {type(e).__name__}: {e}",
                exc_info=True
            )
            return {
                "success": False,
                "error": f"License generation failed: {e}",
                "session_id": session_id
            }

        # Send welcome email with license key
        self.logger.info(f"[Session {session_id}] Sending license key email to {customer_email}...")

        try:
            email_sent = self.email_sender.send_license_key_email(
                to_email=customer_email,
                license_key=license_key,
                tier=tier,
                expires=expires
            )

            if email_sent:
                self.logger.info(f"[Session {session_id}] ✅ Email sent successfully to {customer_email}")
                # Mark as processed (idempotency)
                self._processed_sessions.add(session_id)
            else:
                self.logger.error(
                    f"[Session {session_id}] ❌ Email sending returned False "
                    f"(check SMTP logs above for details)"
                )
                return {
                    "success": False,
                    "error": "Email sending failed (check logs)",
                    "session_id": session_id,
                    "license_key": license_key  # For manual recovery
                }

        except Exception as e:
            self.logger.error(
                f"[Session {session_id}] Email sending exception: {type(e).__name__}: {e}",
                exc_info=True
            )
            return {
                "success": False,
                "error": f"Email sending exception: {e}",
                "session_id": session_id,
                "license_key": license_key  # For manual recovery
            }

        # TODO: Store in database for lookup
        # db.save_license(
        #     email=customer_email,
        #     license_key=license_key,
        #     tier=tier,
        #     expires=expires,
        #     customer_id=customer_id,
        #     subscription_id=subscription_id,
        #     session_id=session_id
        # )

        self.logger.info(f"[Session {session_id}] === CHECKOUT COMPLETED SUCCESSFULLY ===")

        return {
            "success": True,
            "message": f"License key sent to {customer_email}",
            "session_id": session_id,
            "license_key": license_key  # For logging only (remove in production)
        }

    def _handle_subscription_created(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer.subscription.created event."""
        subscription = event["data"]["object"]

        customer_id = subscription.get("customer")
        subscription_id = subscription.get("id")
        status = subscription.get("status")

        self.logger.info(f"Subscription created: {subscription_id}, status={status}, customer={customer_id}")

        # License is already generated in checkout.session.completed
        # This is just for logging/tracking

        return {"success": True, "message": f"Subscription {subscription_id} created"}

    def _handle_subscription_updated(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer.subscription.updated event.

        This fires when:
        - Subscription tier changes (upgrade/downgrade)
        - Billing changes (monthly → annual)
        - Subscription renews
        """
        subscription = event["data"]["object"]

        customer_id = subscription.get("customer")
        subscription_id = subscription.get("id")
        status = subscription.get("status")

        self.logger.info(f"Subscription updated: {subscription_id}, status={status}, customer={customer_id}")

        # If subscription is active, extend license
        if status == "active":
            # TODO: Look up customer email from database
            # customer_email = db.get_customer_email(customer_id)
            # Generate new license with extended expiry
            # expires = datetime.now() + timedelta(days=35)
            # license_key = self.license_generator.generate_license_key(customer_email, tier, expires)
            # db.update_license(customer_email, license_key, expires)
            # self.email_sender.send_license_renewed_email(customer_email, license_key, expires)
            pass

        return {"success": True, "message": f"Subscription {subscription_id} updated"}

    def _handle_subscription_deleted(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer.subscription.deleted event.

        This fires when a subscription is canceled.
        """
        subscription = event["data"]["object"]

        customer_id = subscription.get("customer")
        subscription_id = subscription.get("id")

        self.logger.info(f"Subscription deleted: {subscription_id}, customer={customer_id}")

        # TODO: Revoke license or mark as expired
        # customer_email = db.get_customer_email(customer_id)
        # db.revoke_license(customer_email)
        # self.email_sender.send_cancellation_email(customer_email)

        return {"success": True, "message": f"Subscription {subscription_id} deleted"}

    def _handle_payment_succeeded(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle invoice.payment_succeeded event.

        This fires when a subscription payment goes through (monthly renewal).
        NOTE: This does NOT fire for $0 invoices (100% discount codes).
        """
        invoice = event["data"]["object"]

        customer_id = invoice.get("customer")
        subscription_id = invoice.get("subscription")
        amount_paid = invoice.get("amount_paid", 0)

        self.logger.info(
            f"Payment succeeded: ${amount_paid/100:.2f} for subscription {subscription_id}, "
            f"customer={customer_id}"
        )

        # Extend license on successful payment
        # TODO: Extend license expiry by 1 month
        # customer_email = db.get_customer_email(customer_id)
        # current_license = db.get_license(customer_email)
        # new_expires = current_license.expires + timedelta(days=30)
        # new_license_key = self.license_generator.generate_license_key(customer_email, tier, new_expires)
        # db.update_license(customer_email, new_license_key, new_expires)
        # self.email_sender.send_payment_success_email(customer_email, new_license_key, new_expires)

        return {"success": True, "message": f"Payment processed for {subscription_id}"}

    def _handle_payment_failed(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle invoice.payment_failed event.

        This fires when a subscription payment fails.
        """
        invoice = event["data"]["object"]

        customer_id = invoice.get("customer")
        subscription_id = invoice.get("subscription")
        attempt_count = invoice.get("attempt_count")

        self.logger.warning(
            f"Payment failed for {subscription_id}, attempt {attempt_count}, customer={customer_id}"
        )

        # TODO: Send payment failed email
        # customer_email = db.get_customer_email(customer_id)
        # self.email_sender.send_payment_failed_email(customer_email, attempt_count)

        # Don't immediately revoke license - Stripe retries for ~2 weeks
        # Only revoke if subscription gets deleted

        return {"success": True, "message": f"Payment failed for {subscription_id}"}
