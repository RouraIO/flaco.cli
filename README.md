# 🍎 Flaco AI - Professional iOS Code Review Platform

**The most comprehensive code review tool for iOS/Swift development**

Flaco AI is an AI-powered code review platform with **405+ automated checks** specifically designed for iOS and Swift development. Catch security issues, performance problems, and architecture anti-patterns before they reach production.

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
║      🚀 Professional iOS Code Review Platform (v2.0.0)                    ║
║         405+ Automated Checks • CI/CD Ready • Local-First                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## ⚡ Why Flaco AI?

### 🔍 **405+ Automated Checks**
Comprehensive static analysis covering:
- **Security**: Keychain usage, ATS compliance, API key detection, weak crypto
- **Performance**: Main thread blocking, retain cycles, N+1 queries, inefficient rendering
- **SwiftUI Best Practices**: View body size, @State patterns, GeometryReader usage
- **iOS Platform**: Deprecated APIs, version compatibility, HIG compliance
- **Architecture**: Massive View Controllers, tight coupling, separation of concerns

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

## 🚀 Quick Start

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RouraIO/flaco.cli.git
cd flaco.cli

# 2. Run the installer
python3 scripts/install_flaco.py

# 3. Reload your shell
source ~/.zshrc  # or open a new terminal

# 4. Verify installation
flaco --version  # Should show v2.0.0
```

### First Review

```bash
# Navigate to your iOS project
cd ~/Projects/MyiOSApp

# Start Flaco AI
flaco

# Run comprehensive review
/review

# Or review specific files
/review LoginViewController.swift
```

---

## 📊 Analyzer Coverage

### Built-in Analyzers

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

**Total: 405+ automated checks**

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
          cd flaco.cli && python3 scripts/install_flaco.py
      - name: Run Review
        run: |
          source ~/.zshrc
          cd $GITHUB_WORKSPACE
          flaco --model openai/qwen2.5-coder:32b << EOF
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

#### **Custom Team Rules**
```bash
# Create .flaco/rules.yaml
cat > .flaco/rules.yaml << EOF
rules:
  - name: "All ViewModels must use @Observable"
    pattern: "class.*ViewModel(?!.*@Observable)"
    severity: medium
    message: "ViewModels should use @Observable for iOS 17+"
    file_extension: swift
EOF

# Rules automatically applied
/review
# Running custom rules from rules.yaml...
# Loaded 1 custom rules from .flaco/rules.yaml
```

---

## 🎯 Review Output Format

```markdown
## 📊 Executive Summary
Project has good architecture but needs attention to force unwrapping
patterns and missing error handling in network layer.

## 🚨 Critical Issues (Must Fix Before Shipping)
- **LoginViewController.swift:142** - Hardcoded API key in source code
  - **Impact**: Security breach - API key exposed in version control
  - **Fix**: Move to Keychain or environment variable

## ⚠️ High-Priority Improvements
- **ProfileViewModel.swift:89** - Force unwrapping user data
  - **Impact**: App will crash if user is nil
  - **Fix**: Use guard let or if let binding

## 💡 Medium-Priority Improvements
- **NetworkManager.swift:234** - Missing error handling in catch block
  - **Fix**: Add proper error logging and user notification

## ✅ What's Working Well
- Clean MVVM architecture with proper separation
- Good use of async/await for networking
- Comprehensive SwiftUI previews

## 🎯 Recommendations
1. Implement error handling strategy across network layer
2. Add crash analytics to track force unwrap failures
3. Consider migrating to @Observable for iOS 17+
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

### Custom Rules Location
Flaco AI automatically searches for custom rules in:
1. `.flaco/rules.yaml` (recommended)
2. `.flacoai/rules.yaml`
3. `flaco-rules.yaml` (project root)

### Baseline Storage
Baselines are stored in `.flaco/baselines/current.json`

---

## 📚 Documentation

- **Command Reference**: Type `/help` in Flaco AI
- **Custom Rules Guide**: See [Custom Rules](docs/CUSTOM_RULES.md) (coming soon)
- **CI/CD Integration**: See [CI/CD Guide](docs/CICD.md) (coming soon)
- **Troubleshooting**: See [FAQ](docs/FAQ.md) (coming soon)

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

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built on top of [Aider](https://github.com/paul-gauthier/aider)
- Powered by Claude AI and Ollama
- Inspired by the iOS development community

---

## 🔗 Links

- **Repository**: https://github.com/RouraIO/flaco.cli
- **Issues**: https://github.com/RouraIO/flaco.cli/issues
- **Discussions**: https://github.com/RouraIO/flaco.cli/discussions

---

**Made with ❤️ for iOS Developers**

*Catch bugs before they catch you.*
