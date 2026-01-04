"""
Flaco AI License Server - Stripe Integration

This server handles:
- Stripe webhook events (subscriptions, payments)
- License key generation and delivery
- Customer portal access
- Subscription management
"""

import os
import sys
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, redirect, render_template_string
from flask_cors import CORS
import stripe
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.stripe_handler import StripeWebhookHandler
from backend.email_sender import EmailSender
from backend.license_generator import LicenseKeyGenerator

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load environment variables
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
FLACO_LICENSE_SECRET = os.getenv("FLACO_LICENSE_SECRET", "CHANGE_ME_IN_PRODUCTION")

if not STRIPE_SECRET_KEY:
    raise ValueError("STRIPE_SECRET_KEY environment variable is required")

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Initialize handlers
webhook_handler = StripeWebhookHandler(
    license_generator=LicenseKeyGenerator(secret_key=FLACO_LICENSE_SECRET),
    email_sender=EmailSender()
)


@app.route("/")
def index():
    """Home page - redirect to pricing."""
    return redirect("/pricing")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "flaco-license-server",
        "version": "3.0.0"
    })


@app.route("/webhooks/stripe", methods=["POST"])
def stripe_webhook():
    """Handle Stripe webhook events.

    Events handled:
    - checkout.session.completed (new subscription)
    - customer.subscription.updated (tier change)
    - customer.subscription.deleted (cancellation)
    - invoice.payment_failed (payment issues)
    """
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Verify webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        app.logger.error(f"Invalid payload: {e}")
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        app.logger.error(f"Invalid signature: {e}")
        return jsonify({"error": "Invalid signature"}), 400

    # Handle the event
    event_type = event["type"]
    app.logger.info(f"Received Stripe event: {event_type}")

    try:
        result = webhook_handler.handle_event(event)

        if result.get("success"):
            app.logger.info(f"Successfully handled {event_type}")
            return jsonify(result), 200
        else:
            app.logger.error(f"Failed to handle {event_type}: {result.get('error')}")
            return jsonify(result), 500

    except Exception as e:
        app.logger.error(f"Error handling webhook: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/create-checkout-session", methods=["POST"])
def create_checkout_session():
    """Create Stripe Checkout session for purchasing a license.

    Request body:
    {
        "tier": "pro" | "enterprise",
        "billing": "monthly" | "annual",
        "email": "customer@example.com"
    }
    """
    try:
        data = request.get_json()
        tier = data.get("tier", "pro")
        billing = data.get("billing", "monthly")
        customer_email = data.get("email")

        # Get price ID based on tier and billing
        price_ids = {
            "pro_monthly": os.getenv("STRIPE_PRICE_PRO_MONTHLY"),
            "pro_annual": os.getenv("STRIPE_PRICE_PRO_ANNUAL"),
            "enterprise_monthly": os.getenv("STRIPE_PRICE_ENTERPRISE_MONTHLY"),
        }

        price_key = f"{tier}_{billing}"
        price_id = price_ids.get(price_key)

        if not price_id:
            return jsonify({"error": f"Invalid tier/billing: {price_key}"}), 400

        # Create Checkout Session
        checkout_session = stripe.checkout.Session.create(
            customer_email=customer_email,
            payment_method_types=["card"],
            line_items=[{
                "price": price_id,
                "quantity": 1,
            }],
            mode="subscription",
            success_url=os.getenv("STRIPE_SUCCESS_URL", "https://flaco-license-server.onrender.com/success?session_id={CHECKOUT_SESSION_ID}"),
            cancel_url=os.getenv("STRIPE_CANCEL_URL", "https://flaco-license-server.onrender.com/pricing"),
            metadata={
                "tier": tier,
                "billing": billing,
            },
            allow_promotion_codes=True,  # Allow discount codes
        )

        return jsonify({
            "success": True,
            "checkout_url": checkout_session.url,
            "session_id": checkout_session.id
        })

    except Exception as e:
        app.logger.error(f"Error creating checkout session: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/customer-portal", methods=["POST"])
def customer_portal():
    """Create Stripe Customer Portal session for managing subscription.

    Request body:
    {
        "customer_id": "cus_xxxxx"
    }
    """
    try:
        data = request.get_json()
        customer_id = data.get("customer_id")

        if not customer_id:
            return jsonify({"error": "customer_id is required"}), 400

        # Create portal session
        portal_session = stripe.billing_portal.Session.create(
            customer=customer_id,
            return_url=os.getenv("STRIPE_RETURN_URL", "https://flaco.ai/account"),
        )

        return jsonify({
            "success": True,
            "portal_url": portal_session.url
        })

    except Exception as e:
        app.logger.error(f"Error creating portal session: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/verify-license", methods=["POST"])
def verify_license():
    """Verify a license key (for customer support).

    Request body:
    {
        "email": "customer@example.com",
        "license_key": "FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX"
    }
    """
    try:
        data = request.get_json()
        email = data.get("email")
        license_key = data.get("license_key")

        if not email or not license_key:
            return jsonify({"error": "email and license_key are required"}), 400

        # Verify license
        license_gen = LicenseKeyGenerator(secret_key=FLACO_LICENSE_SECRET)
        is_valid = license_gen.verify_license_key(email, license_key)

        if is_valid:
            # Extract tier and expiry from key (you'd need to store this)
            return jsonify({
                "success": True,
                "valid": True,
                "message": "License key is valid"
            })
        else:
            return jsonify({
                "success": True,
                "valid": False,
                "message": "License key is invalid or expired"
            })

    except Exception as e:
        app.logger.error(f"Error verifying license: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/success")
def success_page():
    """Success page after checkout completion."""
    session_id = request.args.get("session_id")

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Payment Successful - Flaco AI</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #007aff 0%, #5ac8fa 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .success-container {
                background: white;
                border-radius: 16px;
                padding: 60px 40px;
                max-width: 500px;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            .checkmark {
                width: 80px;
                height: 80px;
                border-radius: 50%;
                background: #00a86b;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 30px;
                animation: scaleIn 0.5s ease-out;
            }
            .checkmark::after {
                content: "✓";
                color: white;
                font-size: 48px;
                font-weight: bold;
            }
            @keyframes scaleIn {
                from { transform: scale(0); }
                to { transform: scale(1); }
            }
            h1 {
                font-size: 32px;
                margin: 0 0 16px 0;
                color: #1d1d1f;
            }
            p {
                font-size: 18px;
                color: #666;
                line-height: 1.6;
                margin: 16px 0;
            }
            .email-box {
                background: #f5f5f7;
                border-radius: 8px;
                padding: 20px;
                margin: 30px 0;
            }
            .email-box strong {
                color: #007aff;
                font-size: 20px;
            }
            .close-button {
                background: #007aff;
                color: white;
                border: none;
                padding: 14px 32px;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 20px;
            }
            .close-button:hover {
                background: #0051d5;
            }
        </style>
    </head>
    <body>
        <div class="success-container">
            <div class="checkmark"></div>
            <h1>Payment Successful!</h1>
            <p>Thank you for upgrading to Flaco AI PRO</p>

            <div class="email-box">
                <p><strong>📧 Check Your Email</strong></p>
                <p style="margin: 0;">We've sent your license key to your email address. It should arrive within a few minutes.</p>
            </div>

            <p style="font-size: 14px; color: #999;">
                Didn't receive it? Check your spam folder or contact us at support@roura.io
            </p>

            <button class="close-button" onclick="window.close()">Close Window</button>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)


@app.route("/pricing")
def pricing_page():
    """Simple pricing page with Stripe Checkout buttons."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flaco AI Pricing</title>
        <script src="https://js.stripe.com/v3/"></script>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                   margin: 0; padding: 40px; background: #f5f5f7; }
            .container { max-width: 1200px; margin: 0 auto; }
            h1 { text-align: center; font-size: 48px; margin-bottom: 60px; }
            .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                           gap: 30px; margin-top: 40px; }
            .pricing-card { background: white; border-radius: 12px; padding: 40px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }
            .pricing-card h2 { margin-top: 0; font-size: 32px; }
            .pricing-card .price { font-size: 48px; font-weight: bold; margin: 20px 0; }
            .pricing-card .price span { font-size: 18px; color: #666; }
            .pricing-card ul { list-style: none; padding: 0; margin: 30px 0; }
            .pricing-card li { padding: 10px 0; border-bottom: 1px solid #eee; }
            .pricing-card li:before { content: "✓ "; color: #00a86b; font-weight: bold; }
            .buy-button { background: #007aff; color: white; border: none; padding: 16px 32px;
                         border-radius: 8px; font-size: 18px; cursor: pointer; width: 100%; }
            .buy-button:hover { background: #0051d5; }
            .enterprise-card { border: 3px solid #007aff; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flaco AI Pricing</h1>

            <div class="pricing-grid">
                <!-- FREE Tier -->
                <div class="pricing-card">
                    <h2>FREE</h2>
                    <div class="price">$0<span>/forever</span></div>
                    <ul>
                        <li>11 Built-in Analyzers</li>
                        <li>405+ automated checks</li>
                        <li>CI/CD integration</li>
                        <li>GitHub export</li>
                        <li>Unlimited local usage</li>
                    </ul>
                    <button class="buy-button" onclick="window.location.href='https://github.com/RouraIO/flaco.cli'">
                        Get Started Free
                    </button>
                </div>

                <!-- PRO Tier -->
                <div class="pricing-card">
                    <h2>PRO</h2>
                    <div class="price">$49<span>/dev/month</span></div>
                    <ul>
                        <li>Everything in FREE</li>
                        <li>5 Premium Analyzers</li>
                        <li>605+ total checks</li>
                        <li>Crash prediction</li>
                        <li>Memory leak detection</li>
                        <li>Security scoring (0-100)</li>
                        <li>Technical debt metrics</li>
                        <li>Email support (24h)</li>
                    </ul>
                    <button class="buy-button" onclick="buyPro('monthly')">
                        Buy PRO Monthly
                    </button>
                    <button class="buy-button" style="margin-top: 10px; background: #5ac8fa;" onclick="buyPro('annual')">
                        Buy PRO Annual (Save 17%)
                    </button>
                </div>

                <!-- ENTERPRISE Tier -->
                <div class="pricing-card enterprise-card">
                    <h2>ENTERPRISE</h2>
                    <div class="price">Custom<span>/pricing</span></div>
                    <ul>
                        <li>Everything in PRO</li>
                        <li>Cloud dashboard</li>
                        <li>SSO/SAML integration</li>
                        <li>Priority support (4h SLA)</li>
                        <li>Custom analyzers</li>
                        <li>Dedicated account manager</li>
                        <li>On-premises deployment</li>
                    </ul>
                    <button class="buy-button" onclick="window.location.href='mailto:sales@roura.io?subject=Enterprise Inquiry'">
                        Contact Sales
                    </button>
                </div>
            </div>
        </div>

        <script>
            async function buyPro(billing) {
                const email = prompt("Enter your email address:");
                if (!email) return;

                try {
                    const response = await fetch('/api/create-checkout-session', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ tier: 'pro', billing, email })
                    });

                    const data = await response.json();
                    if (data.success) {
                        window.location.href = data.checkout_url;
                    } else {
                        alert('Error: ' + (data.error || 'Unknown error'));
                    }
                } catch (err) {
                    alert('Error: ' + err.message);
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    # Run development server
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"

    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug
    )
