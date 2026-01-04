"""Email delivery for Flaco AI license keys and notifications."""

import os
import logging
from datetime import datetime
from typing import Optional


class EmailSender:
    """Send license keys and notifications via SendGrid or SMTP."""

    def __init__(self):
        """Initialize email sender."""
        self.logger = logging.getLogger(__name__)
        self.from_email = os.getenv("FROM_EMAIL", "licenses@roura.io")
        self.from_name = os.getenv("FROM_NAME", "Flaco AI")

        # Try SendGrid first (recommended)
        self.sendgrid_api_key = os.getenv("SENDGRID_API_KEY")

        if self.sendgrid_api_key:
            try:
                from sendgrid import SendGridAPIClient
                from sendgrid.helpers.mail import Mail
                self.sendgrid_client = SendGridAPIClient(self.sendgrid_api_key)
                self.use_sendgrid = True
                self.logger.info("Email sender initialized with SendGrid")
            except ImportError:
                self.logger.warning("SendGrid SDK not installed. Install with: pip install sendgrid")
                self.use_sendgrid = False
        else:
            self.use_sendgrid = False
            self.logger.info("No SENDGRID_API_KEY found, will use SMTP if configured")

    def send_license_key_email(self, to_email: str, license_key: str, tier: str,
                               expires: datetime) -> bool:
        """Send welcome email with license key.

        Args:
            to_email: Customer email
            license_key: Generated license key
            tier: License tier (pro, enterprise)
            expires: Expiry date

        Returns:
            True if email sent successfully
        """
        # Validate email address
        if not to_email or not isinstance(to_email, str) or "@" not in to_email:
            self.logger.error(f"Invalid email address: {to_email}")
            return False

        self.logger.info(f"Preparing license email for {to_email}")

        subject = f"🎉 Welcome to Flaco AI {tier.upper()} - Your License Key"

        body_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                       line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #007aff 0%, #5ac8fa 100%);
                          color: white; padding: 40px 20px; text-align: center; border-radius: 8px; }}
                .content {{ background: #f5f5f7; padding: 30px; margin-top: 20px; border-radius: 8px; }}
                .license-box {{ background: white; padding: 20px; border-radius: 8px;
                               border: 2px dashed #007aff; margin: 20px 0; text-align: center; }}
                .license-key {{ font-family: monospace; font-size: 18px; font-weight: bold;
                               color: #007aff; letter-spacing: 2px; }}
                .steps {{ background: white; padding: 20px; border-radius: 8px; margin-top: 20px; }}
                .steps ol {{ padding-left: 20px; }}
                .steps li {{ margin: 10px 0; }}
                code {{ background: #f0f0f0; padding: 2px 6px; border-radius: 3px;
                       font-family: monospace; }}
                .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 14px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🚀 Welcome to Flaco AI {tier.upper()}!</h1>
                    <p>Thank you for upgrading. You now have access to premium features.</p>
                </div>

                <div class="content">
                    <h2>Your License Key</h2>
                    <div class="license-box">
                        <p class="license-key">{license_key}</p>
                        <p style="margin-top: 10px; color: #666; font-size: 14px;">
                            Valid until: {expires.strftime("%B %d, %Y")}
                        </p>
                    </div>

                    <div class="steps">
                        <h3>Activation Steps</h3>
                        <ol>
                            <li>Open your terminal and run: <code>flaco</code></li>
                            <li>Enter the following command:
                                <br><code>/license activate {to_email} {license_key}</code>
                            </li>
                            <li>Verify activation: <code>/license info</code></li>
                            <li>Start using premium features: <code>/review</code></li>
                        </ol>
                    </div>

                    <h3>What You Get ({tier.upper()} Tier)</h3>
                    <ul>
                        <li>✓ 5 Premium Analyzers (605+ total checks)</li>
                        <li>✓ Crash Prediction with likelihood scoring</li>
                        <li>✓ Performance Profiler for bottleneck detection</li>
                        <li>✓ Memory Leak Detection (retain cycles)</li>
                        <li>✓ Security Scoring (0-100 with OWASP compliance)</li>
                        <li>✓ Technical Debt Metrics (maintainability index)</li>
                        <li>✓ Advanced auto-fix capabilities</li>
                        <li>✓ Priority email support (24-hour response)</li>
                    </ul>

                    <h3>Need Help?</h3>
                    <p>
                        📧 Email: <a href="mailto:support@roura.io">support@roura.io</a><br>
                        📖 Docs: <a href="https://github.com/RouraIO/flaco.cli">GitHub README</a><br>
                        💬 Issues: <a href="https://github.com/RouraIO/flaco.cli/issues">GitHub Issues</a>
                    </p>
                </div>

                <div class="footer">
                    <p>This email contains your Flaco AI license key. Keep it secure.</p>
                    <p>Manage your subscription: <a href="https://flaco.ai/account">Customer Portal</a></p>
                    <p>&copy; 2026 Roura.IO - Flaco AI</p>
                </div>
            </div>
        </body>
        </html>
        """

        body_text = f"""
🎉 Welcome to Flaco AI {tier.upper()}!

Your License Key:
{license_key}

Valid until: {expires.strftime("%B %d, %Y")}

Activation Steps:
1. Run: flaco
2. Enter: /license activate {to_email} {license_key}
3. Verify: /license info
4. Use: /review

Need help? Email support@roura.io

---
© 2026 Roura.IO - Flaco AI
        """

        return self._send_email(to_email, subject, body_html, body_text)

    def send_payment_failed_email(self, to_email: str, attempt_count: int) -> bool:
        """Send payment failure notification."""
        subject = "⚠️ Flaco AI Payment Failed - Action Required"

        body_html = f"""
        <html>
        <body style="font-family: sans-serif; line-height: 1.6; padding: 20px;">
            <h2>Payment Failed</h2>
            <p>We were unable to process your payment for Flaco AI PRO subscription.</p>
            <p>Attempt: {attempt_count}</p>
            <p><strong>Action Required:</strong></p>
            <ul>
                <li>Update your payment method in the <a href="https://flaco.ai/account">Customer Portal</a></li>
                <li>Or contact support at <a href="mailto:billing@roura.io">billing@roura.io</a></li>
            </ul>
            <p>Your license will remain active for a grace period while we retry.</p>
        </body>
        </html>
        """

        body_text = f"""
Payment Failed - Flaco AI PRO

We were unable to process your payment (attempt {attempt_count}).

Action Required:
- Update payment method: https://flaco.ai/account
- Contact support: billing@roura.io

Your license remains active during the grace period.
        """

        return self._send_email(to_email, subject, body_html, body_text)

    def send_cancellation_email(self, to_email: str) -> bool:
        """Send subscription cancellation confirmation."""
        subject = "Flaco AI Subscription Canceled"

        body_html = """
        <html>
        <body style="font-family: sans-serif; line-height: 1.6; padding: 20px;">
            <h2>Subscription Canceled</h2>
            <p>Your Flaco AI PRO subscription has been canceled.</p>
            <p>Your license will remain active until the end of the current billing period.</p>
            <p>After expiration, you'll be reverted to the FREE tier with access to:</p>
            <ul>
                <li>11 Built-in Analyzers</li>
                <li>405+ automated checks</li>
                <li>All core features</li>
            </ul>
            <p>Want to reactivate? Visit <a href="https://github.com/RouraIO/flaco.cli/blob/main/PRICING.md">Pricing</a></p>
            <p>We'd love your feedback: <a href="mailto:feedback@roura.io">feedback@roura.io</a></p>
        </body>
        </html>
        """

        body_text = """
Subscription Canceled - Flaco AI

Your PRO subscription has been canceled.

Your license remains active until the end of the current billing period.
After that, you'll revert to the FREE tier (11 analyzers, 405+ checks).

Reactivate: https://github.com/RouraIO/flaco.cli/blob/main/PRICING.md
Feedback: feedback@roura.io
        """

        return self._send_email(to_email, subject, body_html, body_text)

    def _send_email(self, to_email: str, subject: str, body_html: str, body_text: str) -> bool:
        """Send email via SendGrid or SMTP.

        Args:
            to_email: Recipient email
            subject: Email subject
            body_html: HTML body
            body_text: Plain text body

        Returns:
            True if email sent successfully
        """
        if self.use_sendgrid:
            return self._send_via_sendgrid(to_email, subject, body_html, body_text)
        else:
            return self._send_via_smtp(to_email, subject, body_html, body_text)

    def _send_via_sendgrid(self, to_email: str, subject: str, body_html: str, body_text: str) -> bool:
        """Send via SendGrid API."""
        try:
            from sendgrid.helpers.mail import Mail, Email, To, Content

            from_email_obj = Email(self.from_email, self.from_name)
            to_email_obj = To(to_email)

            mail = Mail(
                from_email=from_email_obj,
                to_emails=to_email_obj,
                subject=subject,
                plain_text_content=Content("text/plain", body_text),
                html_content=Content("text/html", body_html)
            )

            response = self.sendgrid_client.send(mail)

            if response.status_code in [200, 202]:
                self.logger.info(f"Email sent to {to_email} via SendGrid")
                return True
            else:
                self.logger.error(f"SendGrid error: {response.status_code} - {response.body}")
                return False

        except Exception as e:
            self.logger.error(f"Failed to send email via SendGrid: {e}")
            return False

    def _send_via_smtp(self, to_email: str, subject: str, body_html: str, body_text: str) -> bool:
        """Send via SMTP (fallback)."""
        smtp_host = os.getenv("SMTP_HOST")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_pass = os.getenv("SMTP_PASS")

        self.logger.info(
            f"SMTP config: host={smtp_host}, port={smtp_port}, "
            f"user={smtp_user}, from={self.from_email}"
        )

        if not all([smtp_host, smtp_user, smtp_pass]):
            missing = []
            if not smtp_host: missing.append("SMTP_HOST")
            if not smtp_user: missing.append("SMTP_USER")
            if not smtp_pass: missing.append("SMTP_PASS")
            self.logger.error(f"SMTP credentials not configured. Missing: {', '.join(missing)}")
            return False

        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            self.logger.info(f"Building email message to {to_email}...")

            msg = MIMEMultipart("alternative")
            msg["From"] = f"{self.from_name} <{self.from_email}>"
            msg["To"] = to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body_text, "plain"))
            msg.attach(MIMEText(body_html, "html"))

            self.logger.info(f"Connecting to SMTP server {smtp_host}:{smtp_port}...")

            with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
                server.set_debuglevel(0)  # Set to 1 for verbose SMTP debugging

                self.logger.info("Starting TLS...")
                server.starttls()

                self.logger.info(f"Logging in as {smtp_user}...")
                server.login(smtp_user, smtp_pass)

                self.logger.info(f"Sending message to {to_email}...")
                server.send_message(msg)

            self.logger.info(f"✅ Email sent successfully to {to_email} via SMTP")
            return True

        except smtplib.SMTPAuthenticationError as e:
            self.logger.error(
                f"❌ SMTP Authentication failed: {e}\n"
                f"   Check SMTP_USER ({smtp_user}) and SMTP_PASS are correct.\n"
                f"   For Gmail, ensure you're using an App Password, not your regular password."
            )
            return False
        except smtplib.SMTPException as e:
            self.logger.error(
                f"❌ SMTP error: {type(e).__name__}: {e}",
                exc_info=True
            )
            return False
        except Exception as e:
            self.logger.error(
                f"❌ Unexpected error sending email: {type(e).__name__}: {e}",
                exc_info=True
            )
            return False
