# 🍎 Flaco AI - Professional iOS Code Review Platform

**The Ultimate Local-First Swift & iOS Development Assistant with Premium Features**

Flaco AI is an AI-powered code review platform with **605+ automated checks** specifically designed for iOS and Swift development. Catch security issues, performance problems, crashes, and memory leaks before they reach production.

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║      ███████╗ ██╗      █████╗   ██████╗  ██████╗       █████╗  ██╗        ║
║      ██╔════╝ ██║     ██╔══██╗ ██╔════╝ ██╔═══██╗     ██╔══██╗ ██║        ║
║      █████╗   ██║     ███████║ ██║      ██║   ██║     ███████║ ██║        ║
║      ██╔══╝   ██║     ██╔══██║ ██║      ██║   ██║     ██╔══██║ ██║        ║
║      ██║      ███████╗██║  ██║ ╚██████╗ ╚██████╔╝     ██║  ██║ ██║        ║
║      ╚═╝      ╚══════╝╚═╝  ╚═╝  ╚═════╝  ╚═════╝      ╚═╝  ╚═╝ ╚═╝        ║
║                                                                           ║
║      🚀 Professional iOS Code Review Platform (v3.0.0)                    ║
║         605+ Automated Checks • Premium Analyzers • Local-First          ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 💰 Pricing & Tiers

### 🆓 **FREE Tier** (Forever)
**$0 - No credit card required**

- ✅ **405+ automated checks** across 11 analyzers
- ✅ Security, Performance, Quality analysis
- ✅ CI/CD integration (--ci, --json)
- ✅ Baseline tracking (--baseline, --compare)
- ✅ GitHub issues export (--export-github)
- ✅ Interactive fixes (--fix)
- ✅ Unlimited local usage with Ollama
- ✅ Custom team rules engine
- ✅ 100% open source

**Perfect for:** Individual developers, small projects, learning iOS

---

### ⭐ **PRO Tier** - **$49/month** or **$399/year** (save $189)
**Everything in FREE, plus 5 premium analyzers with 200+ additional checks**

#### **Premium Analyzers:**

**1. 💥 Crash Prediction Analyzer**
- Detects crash-prone patterns with 50-95% likelihood scoring
- Chained force unwraps (`user!.profile!.name` = 95% crash risk)
- Array bounds violations
- Unchecked optional casts
- Async/await pitfalls

**2. ⚡ Performance Profiler**
- Main thread blocking detection (90-95% UI lag risk)
- View hierarchy complexity analysis (>10 levels = 70% lag)
- Image processing inefficiencies
- Core Data fetch optimization
- Auto Layout performance problems

**3. 🧠 Memory Leak Detector**
- Closure retain cycle detection
- Delegate strong reference issues
- Timer leak detection
- NotificationCenter observer leaks
- Core Data context cycles

**4. 🔒 Security Scoring Analyzer**
- Quantitative security score (0-100)
- Hardcoded credentials detection
- Certificate pinning validation
- API key exposure
- OWASP Mobile Top 10 compliance

**5. 📊 Technical Debt Analyzer**
- Maintainability Index (0-100 score)
- Cyclomatic complexity analysis
- Code duplication detection
- Documentation coverage metrics
- Test coverage gap identification

#### **Additional PRO Features:**
- ✅ **605+ total checks** (200 premium)
- ✅ Priority email support (24-hour response)
- ✅ Early access to new features
- ✅ Automatic license delivery via email
- ✅ Offline license validation (no phone-home)

**Perfect for:** Professional iOS developers, freelancers, small teams

**[Purchase PRO License →](https://flaco-license-server.onrender.com/pricing)**

---

### 🏢 **ENTERPRISE Tier** - Custom Pricing
**Everything in PRO, plus team collaboration and enterprise features**

- ✅ Team dashboard & analytics
- ✅ Automated PR review integration
- ✅ Custom analyzer rules & policies
- ✅ SSO/SAML authentication
- ✅ Priority support (4-hour SLA)
- ✅ Volume licensing discounts
- ✅ Dedicated account manager
- ✅ On-premises deployment options

**Perfect for:** Large teams (10+ developers), enterprises, companies with compliance requirements

**[Contact Sales →](mailto:sales@roura.io)**

---

## 💡 ROI Justification

### For Individual Developers
- Catching 1 crash/month saves 2-4 hours debugging = **$200-400 value**
- **4-8x ROI** on $49/month subscription

### For Small Teams (3-5 devs)
- Prevents 5-10 production crashes/month = **$1,000-2,000 saved**
- Reduces code review time by 30% = **15-20 hours/month**
- **20-40x ROI** on $49/month per developer

### For Enterprise Teams (10+ devs)
- Prevents **$10K-50K in incident costs monthly**
- Reduces technical debt accumulation
- Improves security posture & compliance
- **100-1000x ROI** on ENTERPRISE tier

---

## 🚀 Quick Start

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RouraIO/flaco.cli.git
cd flaco.cli

# 2. Run the interactive installer
python3 scripts/install_flaco_v3.py

# 3. Reload your shell
source ~/.zshrc  # or open a new terminal

# 4. Verify installation
flaco --version  # Should show v3.0.0
```

### First Review (FREE Tier)

```bash
# Navigate to your iOS project
cd ~/Projects/MyiOSApp

# Start Flaco AI
flaco

# Run comprehensive review (405 checks)
/review

# Or review specific files
/review LoginViewController.swift
```

### Upgrade to PRO

```bash
# Check current license
flaco
/license info

# Get upgrade information
/license upgrade

# Purchase at: https://flaco-license-server.onrender.com/pricing
# You'll receive a license key via email

# Activate PRO license (enables 605 checks)
/license activate your@email.com FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX

# Verify PRO features are active
/license info

# Run review with all premium analyzers
/review
```

---

## 📊 Analyzer Coverage

### FREE Tier (11 Analyzers - 405 checks)

| Analyzer | Checks | Focus |
|----------|--------|-------|
| **SecurityAnalyzer** | 50+ | Keychain, crypto, ATS, credentials |
| **PerformanceAnalyzer** | 45+ | Main thread, retain cycles, Core Data |
| **QualityAnalyzer** | 60+ | Force unwrap, error handling, naming |
| **ArchitectureAnalyzer** | 40+ | MVC, MVVM, separation of concerns |
| **SwiftUIAnalyzer** | 40+ | View body size, @State, @ViewBuilder |
| **IOSVersionAnalyzer** | 55+ | Deprecated APIs, version compatibility |
| **IOSSymbolsAnalyzer** | 30+ | SF Symbols deprecation, alternatives |
| **IOSHIGAnalyzer** | 35+ | Button sizes, spacing, accessibility |
| **IOSPlistAnalyzer** | 20+ | Privacy manifest, permissions |
| **SPMAnalyzer** | 25+ | Package.swift quality, dependencies |
| **DocumentationAnalyzer** | 30+ | Missing docs, TODO quality |

### PRO Tier (16 Analyzers - 605 checks)

**All FREE analyzers, plus:**

| Analyzer | Checks | Focus |
|----------|--------|-------|
| **CrashPredictorAnalyzer** | 60+ | Force unwraps, nil safety, crash likelihood |
| **MemoryLeakAnalyzer** | 50+ | Retain cycles, strong refs, observer leaks |
| **PerformanceProfilerAnalyzer** | 45+ | UI lag, main thread, FPS optimization |
| **SecurityScorerAnalyzer** | 25+ | OWASP Top 10, quantitative scoring |
| **TechnicalDebtAnalyzer** | 20+ | Complexity, duplication, maintainability |

---

## ⚡ Why Flaco AI?

### 🔍 **Comprehensive Coverage**
- **Security**: Keychain usage, ATS compliance, API key detection, weak crypto
- **Performance**: Main thread blocking, retain cycles, N+1 queries, inefficient rendering
- **Crashes**: Force unwraps, nil checks, async/await pitfalls, array bounds
- **Memory**: Retain cycles, leaks, strong references, observer cleanup
- **SwiftUI Best Practices**: View body size, @State patterns, GeometryReader usage
- **iOS Platform**: Deprecated APIs, version compatibility, HIG compliance
- **Architecture**: Massive View Controllers, tight coupling, separation of concerns
- **Technical Debt**: Code complexity, duplication, maintainability metrics

### 🤖 **AI-Powered Insights**
- Structured review output with Executive Summary
- Severity-based issue prioritization (Critical/High/Medium/Low)
- Context-aware recommendations with code examples
- Integration with Claude Sonnet for intelligent analysis

### 🛠️ **Professional Features**

#### **Interactive Fix Application**
```bash
/review --fix
# Automatically fix common issues interactively
# • Force unwrap → optional binding
# • Missing [weak self] → add capture list
# • Deprecated APIs → modern alternatives
```

#### **CI/CD Integration**
```bash
/review --ci
# JSON output for pipelines
# Exit code 1 if HIGH+ issues found
# Perfect for GitHub Actions, GitLab CI
```

#### **Baseline Tracking**
```bash
/review --baseline          # Save current state
/review --compare          # Show only NEW issues
# Track code quality improvements over time
```

#### **GitHub Issues Export**
```bash
/review --export-github
# Create GitHub issues for HIGH+ severity findings
# Auto-labeled by category and severity
# Formatted markdown with code snippets
```

#### **Custom Team Rules**
```yaml
# .flaco/rules.yaml
rules:
  - name: "No force unwrapping in ViewModels"
    pattern: "class.*ViewModel.*!"
    severity: high
    message: "Force unwrapping in ViewModels can crash the app"
    recommendation: "Use optional binding or ?? instead"
```

### 🏠 **Local-First with Ollama**
Complete privacy - runs entirely on your machine:
```bash
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"
flaco --model openai/qwen2.5-coder:32b
```

---

## 💻 Usage Examples

### Basic Review
```bash
# Review entire project
/review

# Review specific file
/review MyViewModel.swift

# Security-focused review only
/review --security

# Save report to file
/review --save report.md
```

### Professional Workflows

#### **CI/CD Pipeline** (GitHub Actions)
```yaml
# .github/workflows/code-review.yml
name: Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Flaco AI
        run: |
          git clone https://github.com/RouraIO/flaco.cli
          cd flaco.cli && python3 scripts/install_flaco_v3.py
      - name: Run Review
        env:
          FLACO_LICENSE_KEY: ${{ secrets.FLACO_LICENSE_KEY }}
          FLACO_LICENSE_EMAIL: ${{ secrets.FLACO_LICENSE_EMAIL }}
        run: |
          source ~/.zshrc
          cd $GITHUB_WORKSPACE
          flaco --model openai/qwen2.5-coder:32b << EOF
          /license activate $FLACO_LICENSE_EMAIL $FLACO_LICENSE_KEY
          /review --ci
          EOF
```

#### **Track Progress Over Time**
```bash
# Week 1: Establish baseline
/review --baseline

# Week 2: Check new issues
/review --compare
# Output: 15 new issues, 8 fixed, 42 unchanged

# Export new issues to GitHub
/review --compare --export-github
```

#### **Interactive Fixes**
```bash
/review --fix

# Output:
# ========================================
# File: LoginViewModel.swift:42
# Issue: Force unwrapping [HIGH]
# Fix: Replace ! with optional binding
#
# Before: let user = fetchUser()!
# After:  guard let user = fetchUser() else { return }
#
# Apply this fix? [y/n/q] y
# ✓ Fix applied
```

---

## 🎯 Review Output Format

### FREE Tier Output
```markdown
## 📊 Executive Summary
Project has good architecture but needs attention to force unwrapping
patterns and missing error handling in network layer.

## 🚨 Critical Issues (2 found)
- **LoginViewController.swift:142** - Hardcoded API key
- **NetworkManager.swift:89** - Force unwrapping response data

## ⚠️ High-Priority Improvements (8 found)
- Force unwrapping patterns in 5 ViewModels
- Missing error handling in 3 network methods

## 💡 Medium-Priority Improvements (15 found)
## ✅ What's Working Well
## 🎯 Recommendations
```

### PRO Tier Output (Additional Sections)
```markdown
## 💥 Crash Risk Analysis
- **CRITICAL (95% crash risk)**: ProfileView.swift:23
  - Chained force unwraps: user!.profile!.name!
  - Will crash 100% of time if any value is nil
  - Fix: Use optional chaining

## 🧠 Memory Leak Detection
- **HIGH**: SettingsViewController.swift:45
  - Timer retain cycle detected
  - Recommendation: Use [weak self] in closure

## ⚡ Performance Issues
- **HIGH (90% UI lag risk)**: FeedViewController.swift:120
  - Image processing on main thread
  - Fix: Move to background queue

## 🔒 Security Score: 87/100 (Grade: B - Good)
- ✓ Excellent: No hardcoded secrets
- ⚠️ Medium: Missing certificate pinning (3 files)

## 📊 Technical Debt Score: 76/100 (Grade: C - Fair)
- Maintainability Index: 76
- High complexity methods: 12
- Code duplication: 8%
```

---

## 🔧 Configuration

### Ollama Setup (Local Models)
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull recommended model
ollama pull qwen2.5-coder:32b

# Configure Flaco AI
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"

# For remote Ollama server
export OPENAI_API_BASE="http://192.168.1.100:11434/v1"
```

### License Management
```bash
# View current license status
flaco
/license info

# Activate PRO license
/license activate your@email.com FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX

# Deactivate license (revert to FREE)
/license deactivate

# Get upgrade information
/license upgrade
```

### Custom Rules Location
Flaco AI automatically searches for custom rules in:
1. `.flaco/rules.yaml` (recommended)
2. `.flacoai/rules.yaml`
3. `flaco-rules.yaml` (project root)

### Baseline Storage
Baselines are stored in `.flaco/baselines/current.json`

---

## 📚 Documentation

- **Pricing Details**: [PRICING.md](PRICING.md)
- **Stripe Setup Guide**: [STRIPE_SETUP_GUIDE.md](STRIPE_SETUP_GUIDE.md)
- **Command Reference**: Type `/help` in Flaco AI
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## 🤝 Contributing

We welcome contributions! Areas to help:
- Add more analyzer checks
- Improve auto-fix capabilities
- Add support for more iOS frameworks
- Write documentation and guides

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License

Dual licensed:
- **FREE Tier**: Apache 2.0 License - 100% open source
- **PRO/ENTERPRISE**: Commercial license required

See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built on top of [Aider](https://github.com/paul-gauthier/aider) by Paul Gauthier
- Powered by Claude AI and Ollama
- Inspired by the iOS development community

---

## 🔗 Links

- **Repository**: https://github.com/RouraIO/flaco.cli
- **Purchase PRO**: https://flaco-license-server.onrender.com/pricing
- **Issues**: https://github.com/RouraIO/flaco.cli/issues
- **Support**: support@roura.io
- **Enterprise Sales**: sales@roura.io

---

**Made with ❤️ for iOS Developers**

*Catch bugs, crashes, and memory leaks before they catch you.*
