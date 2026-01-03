"""Stripe webhook event handlers for Flaco AI."""

import logging
from datetime import datetime, timedelta
from typing import Dict, Any


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

    def handle_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Route event to appropriate handler.

        Args:
            event: Stripe event object

        Returns:
            Result dict with success status
        """
        event_type = event["type"]

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
            return handler(event)
        else:
            self.logger.info(f"Unhandled event type: {event_type}")
            return {"success": True, "message": f"Ignored event: {event_type}"}

    def _handle_checkout_completed(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle checkout.session.completed event.

        This fires when a customer completes checkout and payment is successful.
        """
        session = event["data"]["object"]

        customer_email = session.get("customer_email")
        customer_id = session.get("customer")
        subscription_id = session.get("subscription")
        metadata = session.get("metadata", {})

        tier = metadata.get("tier", "pro")
        billing = metadata.get("billing", "monthly")

        self.logger.info(f"Checkout completed: {customer_email}, tier={tier}, billing={billing}")

        # Generate license key
        # Expiry: 1 year for annual, 1 month + grace period for monthly
        if billing == "annual":
            expires = datetime.now() + timedelta(days=365)
        else:
            expires = datetime.now() + timedelta(days=35)  # 30 days + 5 day grace

        license_key = self.license_generator.generate_license_key(
            email=customer_email,
            tier=tier,
            expires=expires
        )

        # Send welcome email with license key
        self.email_sender.send_license_key_email(
            to_email=customer_email,
            license_key=license_key,
            tier=tier,
            expires=expires
        )

        # TODO: Store in database for lookup
        # db.save_license(customer_email, license_key, tier, expires, customer_id, subscription_id)

        return {
            "success": True,
            "message": f"License key sent to {customer_email}",
            "license_key": license_key  # For logging only
        }

    def _handle_subscription_created(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer.subscription.created event."""
        subscription = event["data"]["object"]

        customer_id = subscription.get("customer")
        subscription_id = subscription.get("id")
        status = subscription.get("status")

        self.logger.info(f"Subscription created: {subscription_id}, status={status}")

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

        self.logger.info(f"Subscription updated: {subscription_id}, status={status}")

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

        self.logger.info(f"Subscription deleted: {subscription_id}")

        # TODO: Revoke license or mark as expired
        # customer_email = db.get_customer_email(customer_id)
        # db.revoke_license(customer_email)
        # self.email_sender.send_cancellation_email(customer_email)

        return {"success": True, "message": f"Subscription {subscription_id} deleted"}

    def _handle_payment_succeeded(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Handle invoice.payment_succeeded event.

        This fires when a subscription payment goes through (monthly renewal).
        """
        invoice = event["data"]["object"]

        customer_id = invoice.get("customer")
        subscription_id = invoice.get("subscription")
        amount_paid = invoice.get("amount_paid")

        self.logger.info(f"Payment succeeded: ${amount_paid/100:.2f} for subscription {subscription_id}")

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

        self.logger.warning(f"Payment failed for {subscription_id}, attempt {attempt_count}")

        # TODO: Send payment failed email
        # customer_email = db.get_customer_email(customer_id)
        # self.email_sender.send_payment_failed_email(customer_email, attempt_count)

        # Don't immediately revoke license - Stripe retries for ~2 weeks
        # Only revoke if subscription gets deleted

        return {"success": True, "message": f"Payment failed for {subscription_id}"}
