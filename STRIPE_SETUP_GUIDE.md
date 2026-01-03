# 💳 Flaco AI v3.0.0 - Complete Stripe Setup Guide

This guide walks you through setting up the **full commercial Stripe integration** for Flaco AI.

**Time Required**: ~30 minutes
**Cost**: $0 (Stripe is free until you make sales)

---

## 📋 Prerequisites

- [ ] Domain name (e.g., `flaco.ai`)
- [ ] SSL certificate (use Let's Encrypt free)
- [ ] Server to host license backend (VPS, Heroku, Railway, etc.)
- [ ] Stripe account (free to create)
- [ ] SendGrid account (free 100 emails/day)

---

## Part 1: Stripe Account Setup (10 min)

### Step 1: Create Stripe Account

1. Go to https://stripe.com
2. Click **"Start now"**
3. Enter email, create password
4. Fill in business details:
   - **Business type**: Individual or Company
   - **Industry**: Software as a Service (SaaS)
   - **Website**: https://flaco.ai (or your domain)

### Step 2: Activate Account

1. Complete business verification (may take 1-2 days)
2. Add bank account for payouts
3. Enable **Test Mode** (toggle in top right)

### Step 3: Create Products

**PRO Monthly Product:**
1. Dashboard → Products → **Create product**
2. Name: `Flaco AI PRO - Monthly`
3. Description: `Premium code review with 605+ checks`
4. Pricing:
   - Type: **Recurring**
   - Price: **$49.00** USD
   - Billing period: **Monthly**
5. Click **Save product**
6. **Copy the Price ID** (starts with `price_xxxxx`)
   - Save as `STRIPE_PRICE_PRO_MONTHLY`

**PRO Annual Product:**
1. Products → **Create product**
2. Name: `Flaco AI PRO - Annual`
3. Pricing:
   - Price: **$499.00** USD (17% discount = 10 months)
   - Billing period: **Yearly**
4. **Copy the Price ID**
   - Save as `STRIPE_PRICE_PRO_ANNUAL`

**ENTERPRISE Monthly Product:**
1. Products → **Create product**
2. Name: `Flaco AI ENTERPRISE - Monthly`
3. Pricing:
   - Price: **$2,500.00** USD
   - Billing period: **Monthly**
4. **Copy the Price ID**
   - Save as `STRIPE_PRICE_ENTERPRISE_MONTHLY`

---

## Part 2: Webhook Configuration (5 min)

### Step 4: Create Webhook Endpoint

1. Dashboard → Developers → **Webhooks**
2. Click **Add endpoint**
3. Endpoint URL: `https://yourdomain.com/webhooks/stripe`
   - Replace `yourdomain.com` with your server
4. **Select events to listen to**:
   - `checkout.session.completed`
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `invoice.payment_succeeded`
   - `invoice.payment_failed`
5. Click **Add endpoint**
6. **Copy the Signing secret** (starts with `whsec_xxxxx`)
   - Save as `STRIPE_WEBHOOK_SECRET`

### Step 5: Get API Keys

1. Dashboard → Developers → **API keys**
2. **Test mode** (for testing):
   - Copy **Secret key** (starts with `sk_test_xxxxx`)
   - Save as `STRIPE_SECRET_KEY`
3. **Live mode** (for production):
   - Toggle to **Live mode**
   - Copy **Secret key** (starts with `sk_live_xxxxx`)
   - Save this separately for production

---

## Part 3: Email Setup with SendGrid (5 min)

### Step 6: Create SendGrid Account

1. Go to https://sendgrid.com/
2. Click **Start for Free**
3. Complete signup (100 emails/day free forever)

### Step 7: Create API Key

1. Dashboard → Settings → **API Keys**
2. Click **Create API Key**
3. Name: `Flaco AI License Server`
4. Permissions: **Full Access** (or just "Mail Send")
5. Click **Create & View**
6. **Copy the API key** (starts with `SG.xxxxx`)
   - Save as `SENDGRID_API_KEY`
   - ⚠️ You won't see this again!

### Step 8: Verify Sender Email

1. Dashboard → Settings → **Sender Authentication**
2. Click **Verify a Single Sender**
3. Enter:
   - From Email: `licenses@roura.io` (or your domain)
   - From Name: `Flaco AI`
4. Check inbox and click verification link
5. Update `.env`:
   - `FROM_EMAIL=licenses@roura.io`
   - `FROM_NAME=Flaco AI`

---

## Part 4: Deploy License Server (10 min)

### Step 9: Prepare Server

**Option A: Railway (Easiest)**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
cd flaco.cli/backend
railway init
railway up
```

**Option B: Heroku**
```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
cd flaco.cli/backend
heroku create flaco-license-server

# Deploy
git push heroku main
```

**Option C: Your VPS (DigitalOcean, Linode, etc.)**
```bash
# SSH into server
ssh user@yourserver.com

# Clone repo
git clone https://github.com/RouraIO/flaco.cli.git
cd flaco.cli/backend

# Install dependencies
pip3 install -r requirements.txt

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Step 10: Configure Environment Variables

Create `.env` file on your server:

```bash
# Copy from example
cp .env.example .env

# Edit with your values
nano .env
```

Fill in these values (from previous steps):
```bash
STRIPE_SECRET_KEY=sk_test_xxxxx  # From Step 5
STRIPE_WEBHOOK_SECRET=whsec_xxxxx  # From Step 4
STRIPE_PRICE_PRO_MONTHLY=price_xxxxx  # From Step 3
STRIPE_PRICE_PRO_ANNUAL=price_xxxxx  # From Step 3
STRIPE_PRICE_ENTERPRISE_MONTHLY=price_xxxxx  # From Step 3

FLACO_LICENSE_SECRET=$(openssl rand -hex 32)  # Generate this

SENDGRID_API_KEY=SG.xxxxx  # From Step 7
FROM_EMAIL=licenses@roura.io  # From Step 8
FROM_NAME=Flaco AI

STRIPE_SUCCESS_URL=https://flaco.ai/success?session_id={CHECKOUT_SESSION_ID}
STRIPE_CANCEL_URL=https://flaco.ai/pricing
STRIPE_RETURN_URL=https://flaco.ai/account

PORT=5000
FLASK_ENV=production
```

### Step 11: Test the Server

```bash
# Health check
curl https://yourdomain.com/health

# Expected response:
{
  "status": "healthy",
  "service": "flaco-license-server",
  "version": "3.0.0"
}
```

---

## Part 5: Test Purchases (Before Going Live)

### Step 12: Test Stripe Webhooks Locally

```bash
# Install Stripe CLI
brew install stripe/stripe-cli/stripe

# Login
stripe login

# Forward webhooks to local server
stripe listen --forward-to localhost:5000/webhooks/stripe

# In another terminal, run your server
python backend/app.py

# Trigger test events
stripe trigger checkout.session.completed
```

### Step 13: Test Payment Flow

1. Go to your pricing page: `http://localhost:5000/pricing`
2. Click **Buy PRO Monthly**
3. Enter test email: `test@example.com`
4. Stripe Checkout opens
5. Use test card: `4242 4242 4242 4242`
   - Expiry: Any future date
   - CVC: Any 3 digits
   - ZIP: Any 5 digits
6. Complete payment
7. Check your email (or server logs) for license key
8. Activate license in Flaco:
   ```bash
   flaco
   > /license activate test@example.com FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX
   ```

---

## Part 6: Go Live! (5 min)

### Step 14: Switch to Live Mode

1. Stripe Dashboard → Toggle **Live mode** (top right)
2. Get **Live API keys**:
   - Copy new Secret key (`sk_live_xxxxx`)
3. Update `.env` on server:
   ```bash
   STRIPE_SECRET_KEY=sk_live_xxxxx  # LIVE key
   FLASK_ENV=production
   ```
4. Restart server

### Step 15: Update Webhook Endpoint

1. Dashboard → Developers → **Webhooks** (Live mode)
2. Add endpoint: `https://yourdomain.com/webhooks/stripe`
3. Select same events as test mode
4. Copy **new signing secret** (`whsec_xxxxx`)
5. Update `.env`:
   ```bash
   STRIPE_WEBHOOK_SECRET=whsec_xxxxx  # LIVE secret
   ```

### Step 16: Announce Launch! 🎉

1. Update GitHub README with pricing link
2. Tweet announcement
3. Post to r/iOSProgramming
4. Email your list

---

## 🧪 Testing Checklist

Before going live, test:

- [ ] Health check endpoint works
- [ ] Pricing page loads
- [ ] Checkout session creates successfully
- [ ] Webhook receives `checkout.session.completed`
- [ ] License key is generated
- [ ] Email is sent with license key
- [ ] License activates in Flaco CLI
- [ ] Premium analyzers run after activation
- [ ] `/license info` shows correct tier
- [ ] Customer portal link works
- [ ] Subscription updates are handled
- [ ] Cancellation revokes license
- [ ] Payment failure sends notification

---

## 💰 Revenue Projections

**Fees (Stripe):**
- PRO Monthly: $49 → You get $47.28 (96.5%)
- PRO Annual: $499 → You get $484.23 (97%)
- ENTERPRISE: $2,500 → You get $2,427.20 (97%)

**Conservative Month 3:**
- 10 PRO Monthly × $47.28 = $472.80
- 1 ENTERPRISE × $2,427.20 = $2,427.20
- **Total MRR**: ~$2,900

**Break-even**: ~5 PRO customers covers infrastructure costs

---

## 🆘 Troubleshooting

**Webhook not receiving events:**
- Check webhook URL is accessible publicly
- Verify signing secret matches
- Check server logs for errors

**Email not sending:**
- Verify SendGrid API key
- Check sender email is verified
- Look at SendGrid Activity Feed

**License activation fails:**
- Check `FLACO_LICENSE_SECRET` matches on server and in CLI
- Verify license key format (FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX)
- Check expiry date hasn't passed

---

## 📞 Support

**Stripe Issues:**
- https://support.stripe.com

**SendGrid Issues:**
- https://support.sendgrid.com

**Flaco AI Issues:**
- Email: support@roura.io
- GitHub: https://github.com/RouraIO/flaco.cli/issues

---

**Ready to launch v3.0.0? 🚀**
