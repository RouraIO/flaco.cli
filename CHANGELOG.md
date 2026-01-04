# Changelog

All notable changes to Flaco AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2026-01-03

### 🚀 First Commercial Release - Professional Code Review Platform

Flaco AI v3.0.0 transforms the tool into a **commercial-grade professional code review platform** with **FREE**, **PRO**, and **ENTERPRISE** tiers. This release adds 200+ premium checks, full Stripe payment integration, and enterprise features while keeping the core v2.0.0 features completely free and open source.

**Status**: 🎉 READY FOR COMMERCIAL LAUNCH

---

### 💰 Pricing & Tiers

#### 🆓 FREE Tier (Open Source - Apache 2.0)
- **11 Built-in Analyzers** (405+ checks)
- All v2.0.0 features (CI/CD, baseline tracking, GitHub export, interactive fixes)
- Unlimited local usage with Ollama
- **No license required**

#### ⭐ PRO Tier ($49/developer/month or $399/year)
- **Everything in FREE** plus:
- **5 Premium Analyzers** (200+ additional checks, 605+ total)
- Advanced auto-fix capabilities
- Team collaboration features
- Priority email support (24-hour response)

#### 🏢 ENTERPRISE Tier (Custom pricing, starts at $2,500/month)
- **Everything in PRO** plus:
- Cloud dashboard (SaaS)
- SSO/SAML integration
- Priority support (4-hour SLA)
- Custom analyzer development
- Dedicated account manager
- On-premises deployment option

---

### ✨ New Features (v3.0.0)

#### 🎯 5 Premium Analyzers (PRO/ENTERPRISE only)

**1. Crash Prediction Analyzer** (350 lines, 40+ patterns)
- Predicts crash likelihood with percentage scoring (50-95%)
- **Patterns detected**:
  - Force unwrap chains (user!.profile!.name) - 95% crash risk for 3+ levels
  - Array bounds access without checking - 60% crash risk
  - Optional cascade complexity (4+ levels deep)
  - Unchecked force casts (`as!`) - 70% crash risk
  - Async/await without try-catch - 55% crash risk
  - Collection mutation during iteration - 90% crash risk
  - Missing `[weak self]` in escaping closures
- **Value**: Catches crashes before production deployment

**2. Performance Profiler Analyzer** (300+ lines, 50+ checks)
- Identifies UI lag and FPS drop triggers
- **Detections**:
  - Main thread blocking operations - 75-95% lag likelihood
  - Deep view hierarchy (7+ nesting levels) - 50-95% FPS drop risk
  - Heavy image processing on main thread - 60-80% lag risk
  - Core Data inefficiencies (N+1 queries, missing fetchBatchSize)
  - Auto Layout complexity scoring (8+ constraints flagged)
  - Expensive collection operations (chained map+filter)
  - Network requests in loops - 80% latency multiplier
- **Value**: Prevents UI freezes and performance degradation

**3. Memory Leak Analyzer** (280+ lines, 40+ checks)
- Detects retain cycles and memory management issues
- **Detections**:
  - Closure retain cycles without `[weak self]` - 60-95% leak risk
  - Delegate strong reference cycles - 75% risk
  - Timer leaks (not invalidated in deinit) - 80% risk
  - NotificationCenter observer leaks - 65% risk
  - Core Data context retention issues - 60% risk
  - Image cache unbounded growth
  - Singleton memory accumulation without cleanup - 70% growth risk
- **Value**: Prevents memory-related crashes and app termination

**4. Security Scoring Analyzer** (320+ lines, 35+ checks)
- **Quantitative security score (0-100)** with letter grade (A-F)
- **OWASP Mobile Top 10 compliance checking**
- **Detections**:
  - Hardcoded secrets, API keys, passwords - CRITICAL
  - Insecure HTTP connections - HIGH (OWASP M3)
  - Weak cryptography (MD5, SHA-1, DES, RC4) - HIGH/CRITICAL (OWASP M5)
  - Hardcoded encryption keys - CRITICAL (OWASP M5)
  - Insecure data storage (UserDefaults for sensitive data) - HIGH (OWASP M2)
  - Authentication weaknesses (missing biometric fallback) - MEDIUM (OWASP M4)
  - SQL injection via string concatenation - CRITICAL (OWASP M7)
  - WebView XSS risks - HIGH (OWASP M7)
  - Missing SSL pinning - MEDIUM
  - Jailbreak detection recommendations - LOW
- **Weighted vulnerability scoring** with actionable prioritization
- **Value**: Provides executive-level security metrics and compliance reporting

**5. Technical Debt Analyzer** (300+ lines, 35+ checks)
- **Maintainability Index (0-100)** scoring with grade
- **Detections**:
  - File size violations (>500 lines) - debt scoring
  - Function complexity (cyclomatic complexity >10) - HIGH
  - Long functions (>50 lines) - MEDIUM
  - Code duplication (5+ line blocks repeated) - MEDIUM
  - Class complexity (>15 properties, >20 methods) - MEDIUM/LOW
  - Missing public API documentation - LOW
  - TODO/FIXME comments (unfinished work) - LOW
  - High coupling (>15 imports) - LOW
  - Potential test coverage gaps
- **Value**: Quantifies code health for leadership and prioritizes refactoring

**Total**: **605+ automated checks** (405 free + 200 premium)

---

#### 🔐 License Management System

**License Validation**:
- **HMAC-based license key validation** (SHA-256 signatures)
- **Offline validation** supported (file-based: `~/.flaco/license.json`)
- **Tier-based feature gating** (FREE/PRO/ENTERPRISE)
- **License expiration tracking** with grace periods
- **Optional LaunchDarkly integration** for feature flags with fallback defaults

**New `/license` Command**:
```bash
/license                       # Show current status
/license info                  # Detailed information
/license activate <email> <key> # Activate PRO/ENTERPRISE
/license deactivate            # Revert to FREE
/license upgrade               # Pricing and ROI information
```

---

#### 💳 Complete Stripe Integration

**Payment Backend** (`backend/` directory):
- **Flask-based license server** with Stripe webhooks
- **Automated license key generation** and email delivery
- **Webhook handlers** for subscription lifecycle:
  - `checkout.session.completed` - generate and email license
  - `customer.subscription.updated` - extend license on renewal
  - `customer.subscription.deleted` - revoke license on cancellation
  - `invoice.payment_succeeded` - extend expiry on payment
  - `invoice.payment_failed` - send payment failure notification
- **Email delivery** via SendGrid (or SMTP fallback)
- **Customer portal** access for subscription management
- **Production-ready** with Gunicorn deployment

**Setup Guide** (`STRIPE_SETUP_GUIDE.md`):
- Complete step-by-step Stripe account setup
- Product creation (PRO Monthly, PRO Annual, ENTERPRISE)
- Webhook configuration with signing secrets
- SendGrid email setup
- Deployment options (Railway, Heroku, VPS)
- Testing workflow with Stripe CLI
- Go-live checklist

**Pricing Page**:
- Embedded Stripe Checkout integration
- Real-time checkout session creation
- Support for promotion codes
- Mobile-responsive design

---

#### 🎨 Enhanced Interactive Setup (`scripts/install_flaco_v3.py`)

**Comprehensive Configuration**:
1. **LLM Provider Choice**:
   - Local Ollama (free, private, offline)
   - Claude API (Anthropic - powerful, cloud)
   - Both (hybrid: local for review, Claude for complex tasks)
   - Automatic API key configuration

2. **GitHub Integration**:
   - Git user name and email for commits
   - Auto-configures `git config --global`

3. **Jira Integration** (Optional):
   - Jira URL (e.g., https://company.atlassian.net)
   - Jira email
   - API token for automatic issue creation

4. **Ollama Configuration**:
   - Custom server URL or default (localhost:11434)
   - Default model selection (qwen2.5-coder:32b, deepseek-r1:32b, etc.)

5. **Theme Customization**:
   - Color choice (cyan, green, yellow, magenta, blue, red)
   - Dark mode preference
   - Banner visibility toggle

6. **TUI Preferences**:
   - Compact mode (less verbose output)
   - ASCII art banner on/off
   - Model warnings on/off

**Auto-Configuration**:
- Writes all settings to `~/.zshrc` or `~/.bashrc`
- Creates `~/.local/bin/flaco` executable
- Verifies Ollama connection
- Tests Claude API if configured
- Provides next steps and quick start guide

---

#### 🐛 Bug Fixes

**Critical Fixes**:
1. **Directory Bug** (commands.py:1905, 1937):
   - `/review` now uses **current working directory** (`os.getcwd()`) instead of Flaco's git root
   - Fixes: "reviewing code that isn't about what i want to review"
   - Impact: Users can now run `/review` from any project directory

2. **GitHub Export Labels** (github_exporter.py:36-92):
   - Auto-creates GitHub labels if they don't exist
   - Adds `ensure_labels_exist()` method with 12 predefined labels:
     - Severity: `severity:critical`, `severity:high`, `severity:medium`, `severity:low`
     - Categories: `security`, `performance`, `code-quality`, `architecture`, `ios`, etc.
   - Uses `--force` flag to update existing labels
   - Fixes: "Failed to create issue: could not add label: 'security' not found"

---

### 📄 Legal & Compliance

**Dual Licensing Model**:
- **Open Source** (Apache 2.0): All v1.0.0-v2.0.0 features remain free
- **Commercial**: Premium features (v3.0.0+) require paid license

**Compliance Files**:
- `LICENSE.aider` - Original Apache 2.0 license from Aider
- `NOTICE` - Detailed attribution and modifications list
- `LICENSE` - Dual license (Apache 2.0 + Commercial terms)
- `PRICING.md` - Complete pricing documentation with feature comparison

**Attribution**:
- Full compliance with Apache 2.0 requirements
- Detailed documentation of all modifications
- Proper copyright notices for derivative work

---

### 🔧 Technical Details

**New Files Created**:
```
backend/
├── app.py                          # Flask license server (470 lines)
├── stripe_handler.py               # Webhook handlers (210 lines)
├── license_generator.py            # HMAC key generation (90 lines)
├── email_sender.py                 # SendGrid/SMTP delivery (320 lines)
├── requirements.txt                # Backend dependencies
└── .env.example                    # Configuration template

flacoai/licensing/
├── license_manager.py              # License validation (280 lines)
└── feature_flags.py                # LaunchDarkly integration (220 lines)

flacoai/premium/
├── __init__.py                     # Premium exports
├── crash_prediction_analyzer.py    # Crash predictor (350 lines)
├── performance_profiler_analyzer.py # Performance profiler (300+ lines)
├── memory_leak_analyzer.py         # Memory leak detector (280+ lines)
├── security_scoring_analyzer.py    # Security scorer (320+ lines)
└── technical_debt_analyzer.py      # Debt analyzer (300+ lines)

scripts/
└── install_flaco_v3.py             # Enhanced installer (450 lines)

STRIPE_SETUP_GUIDE.md               # Complete setup guide (450 lines)
PRICING.md                          # Pricing documentation (370 lines)
V3_IMPLEMENTATION_PLAN.md           # Implementation roadmap (445 lines)
```

**Modified Files**:
- `flacoai/__init__.py` - Version bumped to 3.0.0
- `flacoai/commands.py` - Added `/license` command (220 lines), fixed directory bug
- `flacoai/coders/review_coder.py` - Premium analyzer integration with tier gating (80 lines)
- `flacoai/integrations/github_exporter.py` - Auto-label creation (40 lines)

**Lines of Code**:
- **Premium Analyzers**: ~1,550 lines
- **License System**: ~500 lines
- **Stripe Backend**: ~1,000 lines
- **Total New Code**: ~3,000+ lines

**Environment Variables** (New):
```bash
# Stripe
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
STRIPE_PRICE_PRO_MONTHLY
STRIPE_PRICE_PRO_ANNUAL
STRIPE_PRICE_ENTERPRISE_MONTHLY

# Licensing
FLACO_LICENSE_SECRET

# Email
SENDGRID_API_KEY
FROM_EMAIL
FROM_NAME

# TUI
FLACO_TINT_COLOR
FLACO_DARK_MODE
FLACO_COMPACT_MODE
FLACO_SHOW_BANNER
FLACO_SHOW_MODEL_WARNINGS

# Integrations
JIRA_URL
JIRA_EMAIL
JIRA_API_TOKEN
CLAUDE_API_KEY
```

---

### 💰 Business Model

**Stripe Fees**:
- PRO Monthly ($49): Stripe takes $1.72 → You receive **$47.28** (96.5%)
- PRO Annual ($399): Stripe takes $11.82 → You receive **$387.18** (97%)
- ENTERPRISE ($2,500): Stripe takes $72.80 → You receive **$2,427.20** (97%)

**Revenue Projections**:
- **Conservative** (Month 3): 10 PRO + 1 ENTERPRISE = **$2,900 MRR**
- **Optimistic** (Month 6): 50 PRO + 3 ENTERPRISE = **$9,950 MRR**
- **Aggressive** (Year 1): 200 PRO + 10 ENTERPRISE = **$34,800 MRR** (~$417k ARR)

**Break-even**: ~5 PRO customers

---

### 🎯 Success Metrics

**Technical**:
- ✅ All 5 premium analyzers functional (605+ checks)
- ✅ License validation working (FREE/PRO/ENTERPRISE)
- ✅ Stripe integration complete with webhooks
- ✅ Email delivery configured (SendGrid)
- ✅ Directory bug fixed (/review uses cwd)
- ✅ GitHub export auto-creates labels
- ✅ Enhanced setup with full customization

**Business** (Target for Q1 2026):
- [ ] 10+ PRO tier signups in first month
- [ ] 2+ ENTERPRISE conversations in first quarter
- [ ] $500+ MRR by month 3
- [ ] 80%+ customer satisfaction (NPS >40)

---

### 📦 Installation & Upgrade

**New Users**:
```bash
git clone https://github.com/RouraIO/flaco.cli.git
cd flaco.cli
python3 scripts/install_flaco_v3.py
```

**Existing Users (Upgrade from v2.0.0)**:
```bash
cd flaco.cli
git pull
python3 scripts/install_flaco_v3.py
```

**Activate PRO License**:
```bash
flaco
> /license activate you@example.com FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX
```

---

### 🆘 Support & Documentation

**Free Tier**:
- GitHub Discussions
- Documentation (GitHub README)
- Community Slack (planned)

**PRO Tier**:
- Email support: support@roura.io (24-hour response)
- Bug fix prioritization
- Feature voting

**ENTERPRISE Tier**:
- Dedicated Slack/Teams channel
- 4-hour SLA
- Dedicated account manager
- Quarterly business reviews

**Resources**:
- 📖 README: https://github.com/RouraIO/flaco.cli
- 💳 Pricing: `PRICING.md`
- 🔧 Stripe Setup: `STRIPE_SETUP_GUIDE.md`
- 📋 Implementation Plan: `V3_IMPLEMENTATION_PLAN.md`
- 🐛 Issues: https://github.com/RouraIO/flaco.cli/issues

---

### 🚀 What's Next (v3.1.0+)

**Advanced Features** (Planned):
- [ ] GitHub App integration (automatic PR reviews)
- [ ] Local team dashboard (HTML metrics)
- [ ] Batch fix mode (auto-fix LOW severity)
- [ ] Cloud dashboard (SaaS for ENTERPRISE)
- [ ] SSO/SAML provider integration
- [ ] Custom analyzer marketplace
- [ ] Usage analytics backend

**Community Requests**:
- [ ] VS Code extension
- [ ] Xcode integration
- [ ] Kotlin Multiplatform support
- [ ] Android support

---

**This release took Flaco AI from a free tool to a commercial-grade platform. Ready to launch! 🎉**

---

## [1.0.0] - 2026-01-02

### 🎉 First Official Release

This is the first official stable release of **Flaco AI** - The Ultimate Local-First Swift & iOS Development Assistant. Built on top of the proven aider codebase, Flaco AI brings a complete rebrand, modern UI, and optimized workflow for local LLM development.

### ✨ Core Features

#### 🎨 Modern, Beautiful UI
- **Compact Loading Spinner**: Minimal ★ → ✦ → ● cycling animation (unicode) or * → + → • (ASCII)
- **Fun Loading Messages**: 18 random phrases like "Thinking...", "Pondering...", "Hubbub-a-looing...", "Channeling the AI spirits..."
- **Cyan Response Text**: High-contrast #00FFFF color for excellent readability in all themes
- **Organized Header**: Clean 3-line display with emoji labels
  - 🤖 Model: [model info with format]
  - 📁 Directory: [working directory]
  - 🌿 [branch] • 📊 [file count] • 🗺️ [repo-map stats]
- **Version in Banner**: Version displayed in the ASCII art header box

#### 🚀 Local-First Development
- **Ollama Integration**: Seamless support for local LLM models via Ollama
- **Interactive Setup**: One-command setup that configures everything:
  - Git user configuration
  - Ollama server URL
  - Default model selection
  - Auto-disables model warnings for local installs
- **Model Warnings Suppressed**: No annoying unknown context window warnings for local models

#### 🔧 Complete Rebrand
- **Internal Namespace**: Complete migration from `aider` to `flacoai`
  - All imports updated: `from aider` → `from flacoai`
  - Module structure: `flacoai/aider/` → `flacoai/flacoai/`
  - Resource paths: `aider.resources` → `flacoai.resources`
- **Environment Variables**: `aider_*` → `flaco_*` prefix for all env vars
- **GitHub Repository**: `RouraIO/flaco.cli`
- **Branding**: FlacoAI ASCII art and Swift/iOS focused messaging

#### 🐛 Critical Fixes
- **scipy Dependency**: Fixed ModuleNotFoundError crash by including scipy in requirements
- **Tree-sitter Compatibility**: Updated to tree-sitter 0.25+ API using QueryCursor
- **Documentation URLs**: All URLs point to GitHub repository (no non-existent website links)
- **Python 3.14 Compatibility**: Full support for latest Python version

#### 📦 Installation & Setup
- **Simple Installation**: `python3 scripts/install_flaco.py`
- **Auto-Configuration**: Interactive setup handles git, Ollama, and preferences
- **Clean Launcher**: Direct venv Python interpreter in shebang for reliability

### 🔧 Technical Details

**Key Files:**
- `flacoai/__init__.py` - Version 1.0.0
- `flacoai/waiting.py` - Compact 3-character cycling spinner
- `flacoai/branding.py` - `get_flaco_ascii_art()` with version, `format_compact_header()` with labels
- `flacoai/coders/base_coder.py` - Redesigned `get_announcements()` with organized header
- `flacoai/args.py`, `flacoai/main.py`, `flacoai/io.py` - Cyan color defaults (#00FFFF)
- `requirements.txt` - scipy included for PageRank algorithm
- `flacoai/urls.py` - All URLs point to GitHub repository

**Environment Variables:**
- `flaco_DOCKER_IMAGE`, `flaco_ANALYTICS`, `flaco_DARK_MODE`, `flaco_SHOW_DIFFS`
- `flaco_CHECK_UPDATE`, `flaco_CACHE_KEEPALIVE_DELAY`, `flaco_SANITY_CHECK_TURNS`
- `flaco_BENCHMARK_DIR`, `flaco_DOCKER`

### 📖 Documentation
- Complete README with installation instructions
- CONTRIBUTING.md with correct repository URLs
- Comprehensive CHANGELOG
- GitHub repository with release notes

### 🦙 Ollama Support

Perfect integration with local models:
```bash
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"
flaco --model openai/qwen2.5-coder:32b --no-show-model-warnings
```

---

## Pre-1.0 Development Versions

The following were development versions leading up to the 1.0.0 release:

## [0.3.0] - 2026-01-01

### Fixed
- Improved launcher reliability by using venv's Python interpreter directly in shebang
- Resolved compatibility issues with Python 3.14 and Pillow dependencies
- Eliminated venv activation complexity from launcher script

### Changed
- Renamed aider references to flacoai in documentation and configuration files
- Maintained internal aider package structure for compatibility

### Technical
- Simplified launcher architecture for better cross-platform compatibility
- Enhanced installer to generate more reliable executable scripts

## [1.2.0] - 2026-01-01

### Added
- Interactive Ollama server configuration during installation
- Tint color customization with 6 color choices
- Smart defaults with Enter key support
- Auto-formatting of user input

### Enhanced
- Default localhost:11434 for Ollama configuration
- Python 3.14 full compatibility
- Improved installer user experience

### Configuration
- OPENAI_API_BASE auto-configured during setup
- FLACO_TINT_COLOR environment variable support
- Shell aliases for quick model switching

## [1.0.0] - 2026-01-01

### Added
- Initial Python-only, production-ready release
- Python 3.14 support
- Core Swift & iOS development features
- Local LLM support via Ollama
- Jira integration for ticket-driven development
- Project memory and persistent understanding

### Fixed
- ASCII art alignment in startup UI

[1.3.0]: https://github.com/yourusername/flaco/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/yourusername/flaco/compare/1.0.0...1.2.0
[1.0.0]: https://github.com/yourusername/flaco/releases/tag/1.0.0
