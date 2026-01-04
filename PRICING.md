# 💰 Flaco AI Pricing & Tiers

## Overview

Flaco AI offers three tiers designed for different team sizes and needs:
- **FREE**: Full-featured code review for individual developers
- **PRO**: Advanced analyzers and team features for professional teams
- **ENTERPRISE**: Everything + custom development and priority support

---

## 🆓 FREE Tier

**Price**: $0/month (Always free)

### What's Included (v2.0.0 - Open Source)

✅ **11 Built-in Analyzers** (405+ checks):
- SecurityAnalyzer (50+ checks)
- PerformanceAnalyzer (45+ checks)
- QualityAnalyzer (60+ checks)
- ArchitectureAnalyzer (40+ checks)
- SwiftUIAnalyzer (40+ checks)
- IOSVersionAnalyzer (55+ checks)
- IOSSymbolsAnalyzer (30+ checks)
- IOSHIGAnalyzer (35+ checks)
- IOSPlistAnalyzer (20+ checks)
- SPMAnalyzer (25+ checks)
- DocumentationAnalyzer (30+ checks)

✅ **Core Features**:
- Complete `/review` command with all analyzers
- CI/CD integration (`--ci`, `--json` modes)
- Baseline tracking (`--baseline`, `--compare`)
- GitHub issues export (`--export-github`)
- Custom team rules (`.flaco/rules.yaml`)
- Smart context loading (skips generated code)
- Interactive fix application (basic patterns)

✅ **Local-First**:
- Works with Ollama (complete privacy)
- No data sent to cloud
- Unlimited usage

✅ **Support**:
- Community support (GitHub Discussions)
- Documentation and guides
- Public roadmap

**Best For**:
- Individual iOS developers
- Open source projects
- Students and learners
- Evaluating Flaco AI

---

## ⭐ PRO Tier

**Price**: $49/developer/month (billed annually)
**Price**: $59/developer/month (billed monthly)

### Everything in FREE, plus:

✅ **5 Premium Analyzers** (200+ additional checks):
- **CrashPredictionAnalyzer**: Predicts crash points with likelihood scores (40+ patterns)
- **PerformanceProfilerAnalyzer**: Deep performance analysis and bottleneck detection (50+ checks)
- **MemoryLeakAnalyzer**: Detect retain cycles, reference issues, memory patterns (40+ checks)
- **SecurityScoringAnalyzer**: Quantitative security scoring and vulnerability ranking (35+ checks)
- **TechnicalDebtAnalyzer**: Code complexity metrics and maintainability scoring (35+ checks)

**Total Checks**: 605+ (405 free + 200 premium)

✅ **Advanced Auto-Fix**:
- Multi-line refactoring (not just single-line)
- Batch fix mode (fix all LOW severity automatically)
- Safer fix patterns with rollback
- Custom fix templates

✅ **Team Features**:
- GitHub App integration (automatic PR comments)
- Slack notifications (review results, issues found)
- Local team dashboard (HTML metrics)
- Team baseline comparison
- Developer leaderboards (gamification)

✅ **Enhanced Workflows**:
- Advanced baseline comparisons
- Multi-project support
- Custom analyzer templates
- Priority feature requests

✅ **Support**:
- Email support (24-hour response time)
- Priority bug fixes
- Feature voting rights
- Quarterly check-ins

**Best For**:
- Professional iOS development teams
- Agencies building client apps
- Startups scaling quality
- Teams with 2-20 developers

**ROI Calculation**:
- Catches 1 crash/month that would cost 2-4 hours debugging
- At $100/hour developer cost: **Saves $200-400/month**
- **Pays for itself 4-8x**

---

## 🏢 ENTERPRISE Tier

**Price**: Custom (starts at $2,500/month for 10 developers)

### Everything in PRO, plus:

✅ **Cloud Dashboard** (SaaS):
- Real-time team metrics
- Historical trends and graphs
- Cross-project analytics
- Executive reporting
- API access

✅ **Enterprise Security**:
- SSO/SAML integration
- Role-based access control (RBAC)
- Audit logging
- Data residency options
- On-premises deployment option

✅ **Custom Development**:
- Custom analyzer development
- Integration with your tools
- Tailored workflows
- Custom rule templates
- API extensions

✅ **White-Glove Support**:
- Dedicated account manager
- Priority support (4-hour SLA)
- Direct Slack/Teams channel
- Training and onboarding
- Quarterly business reviews

✅ **Legal & Compliance**:
- Custom licensing terms
- Vendor security questionnaires
- SOC 2 Type II compliance (roadmap)
- GDPR compliance
- Custom contracts

✅ **Advanced Features**:
- Multi-tenant management
- Usage analytics and reporting
- Cost center allocation
- Advanced permissions
- Integration with Jira, Linear, Azure DevOps

**Best For**:
- Enterprise iOS teams (20+ developers)
- Companies with compliance requirements
- Organizations needing custom features
- Companies requiring on-premises deployment

**ROI Calculation**:
- Prevents 1 production incident/quarter ($50k+ impact)
- Reduces code review time by 30% (saves 15+ hours/week)
- **Pays for itself in first incident prevented**

---

## 📊 Feature Comparison

| Feature | FREE | PRO | ENTERPRISE |
|---------|------|-----|------------|
| **Analyzers** | 11 (405+ checks) | 16 (605+ checks) | 16+ custom |
| **CI/CD Integration** | ✅ | ✅ | ✅ |
| **Baseline Tracking** | ✅ | ✅ | ✅ |
| **GitHub Export** | ✅ | ✅ | ✅ |
| **Custom Rules** | ✅ | ✅ | ✅ |
| **Interactive Fixes** | Basic | Advanced | Advanced + Custom |
| **Batch Fix Mode** | ❌ | ✅ | ✅ |
| **GitHub App** | ❌ | ✅ | ✅ |
| **Slack Notifications** | ❌ | ✅ | ✅ |
| **Team Dashboard** | ❌ | Local HTML | Cloud SaaS |
| **SSO/SAML** | ❌ | ❌ | ✅ |
| **On-Premises** | ✅ (self-hosted) | ✅ (self-hosted) | ✅ (dedicated) |
| **Custom Analyzers** | ❌ | ❌ | ✅ |
| **Support** | Community | Email (24h) | Dedicated (4h SLA) |
| **SLA** | ❌ | ❌ | ✅ |
| **Price** | **$0** | **$49/dev/mo** | **Custom** |

---

## 🎯 Which Tier is Right For You?

### Choose FREE if:
- You're an individual developer
- You want full code review capabilities
- You're evaluating Flaco AI
- You have tight budgets
- You prefer open source

### Choose PRO if:
- You have a team of 2-20 developers
- You need crash prediction and security scoring
- You want GitHub/Slack integrations
- You value advanced auto-fix
- You want email support

### Choose ENTERPRISE if:
- You have 20+ developers
- You need SSO/SAML
- You require SLA guarantees
- You want custom analyzers
- You need on-premises deployment
- You have compliance requirements

---

## 💳 How to Upgrade

### FREE → PRO

```bash
# Purchase license at https://flaco.ai/pricing
# Then activate:

flaco
> /license activate your-email@company.com YOUR-LICENSE-KEY

# Verify:
> /license info
# Should show: PRO tier, expires 2027-01-03
```

### PRO → ENTERPRISE

Contact sales@roura.io for:
- Custom pricing for your team size
- On-premises deployment options
- Custom analyzer development
- SLA terms and support levels

---

## 🔒 License Management

### Activating Your License

```bash
flaco
> /license activate email@company.com LICENSE-KEY
# ✓ License activated for email@company.com (pro tier)
```

### Checking License Status

```bash
> /license info
# Tier: pro
# Email: email@company.com
# Expires: 2027-01-03
# Days remaining: 365
# Status: active
```

### Deactivating License

```bash
> /license deactivate
# ✓ License deactivated. Reverted to FREE tier.
```

---

## 📈 ROI Examples

### Small Team (5 developers)
**Cost**: $245/month (PRO tier)

**Savings**:
- Catches 2 crashes/month: **Saves 8 hours** ($800)
- Reduces review time 20%: **Saves 20 hours** ($2,000)
- **Total Savings**: $2,800/month
- **ROI**: 11.4x

### Medium Team (15 developers)
**Cost**: $735/month (PRO tier)

**Savings**:
- Catches 5 crashes/month: **Saves 20 hours** ($2,000)
- Reduces review time 25%: **Saves 75 hours** ($7,500)
- Prevents 1 security incident/quarter: **Saves $50k impact**
- **Total Savings**: $9,500/month + incident prevention
- **ROI**: 12.9x

### Enterprise (50 developers)
**Cost**: $3,500/month (Custom Enterprise)

**Savings**:
- Catches 15 crashes/month: **Saves 60 hours** ($6,000)
- Reduces review time 30%: **Saves 300 hours** ($30,000)
- Prevents 1 critical bug/quarter: **Saves $200k impact**
- **Total Savings**: $36,000/month + incident prevention
- **ROI**: 10.3x

---

## ❓ FAQ

### Can I try PRO before buying?
Yes! We offer a 14-day free trial of PRO tier.
Email sales@roura.io with your use case.

### What happens if I cancel?
Your license continues until expiration, then reverts to FREE tier.
All your code and baselines remain - you just lose access to premium analyzers.

### Can I upgrade/downgrade mid-cycle?
Yes! Pro-rated adjustments are applied automatically.

### Do you offer discounts?
- Annual billing: **17% discount** (2 months free)
- Startups (<2 years): **50% off** for first year
- Open source projects: **Free PRO tier**
- Education: **Free PRO tier** for students/teachers
- Non-profits: **50% off**

### Can I purchase licenses for my team?
Yes! Contact sales@roura.io for:
- Team billing (single invoice)
- Flexible seats (add/remove as needed)
- Volume discounts (20+ developers)

### What payment methods do you accept?
- Credit card (Stripe)
- ACH bank transfer
- Invoice (Enterprise only, Net-30)
- Purchase orders (Enterprise only)

### Can I see a demo?
Yes! Book a demo at https://flaco.ai/demo
Or watch our video demo at https://flaco.ai/demo-video

---

## 📞 Contact Sales

**Questions about pricing?**
Email: sales@roura.io

**Want a custom quote?**
Email: enterprise@roura.io

**Technical questions?**
Email: support@roura.io

**Legal/licensing questions?**
Email: legal@roura.io

---

**Start Free Today**: https://github.com/RouraIO/flaco.cli
**Upgrade to Pro**: https://flaco.ai/pricing
**Contact Enterprise Sales**: sales@roura.io

---

*Pricing effective as of 2026-01-03. Subject to change with 30 days notice.*
