## 🎉 Flaco AI v2.0.0 - Professional iOS Code Review Platform

This is the first **production-ready** release of Flaco AI, completely reimagined as a professional iOS code review platform with **405+ automated checks**.

### 🚀 What's New in v2.0.0

#### **Enhanced Code Review System**
- **Structured Output Format**: Executive Summary, Critical/High/Medium/Low severity sections
- **405+ Automated Checks** across 11 specialized analyzers
- **AI-Powered Insights** with context-aware recommendations
- **Severity-Based Prioritization**: CRITICAL → HIGH → MEDIUM → LOW

#### **Interactive Fix Application** (`/review --fix`)
- Automatically generate fixes for common issues
- Interactive prompting for each fix with before/after preview
- Safe fix detection for low-risk auto-apply
- Supports:
  - Force unwrap → optional binding
  - Missing `[weak self]` → add capture list
  - Deprecated APIs → modern alternatives

#### **CI/CD Integration** (`/review --ci`)
- JSON output mode for pipeline integration
- Exit code 1 if HIGH+ severity issues found
- Exit code 0 for clean builds
- Perfect for GitHub Actions, GitLab CI, Jenkins

#### **Baseline Tracking** (`/review --baseline`, `--compare`)
- Save current analysis state as baseline
- Compare against baseline to show only NEW issues
- Track code quality improvements over time
- Statistics by severity (critical/high/medium/low)
- Stored in `.flaco/baselines/current.json`

#### **GitHub Issues Export** (`/review --export-github`)
- Export HIGH+ severity findings to GitHub Issues
- Uses `gh` CLI for seamless integration
- Auto-labeled by category (security, performance, quality, architecture)
- Auto-labeled by severity (critical, high, medium, low)
- Formatted markdown bodies with code snippets

#### **Custom Team Rules** (`.flaco/rules.yaml`)
- Define team-specific code standards
- Regex, contains, and not_contains pattern matching
- Configurable severity and category
- File pattern and extension filtering
- Example:
  ```yaml
  rules:
    - name: "No force unwrapping in ViewModels"
      pattern: "class.*ViewModel.*!"
      severity: high
      message: "Force unwrapping in ViewModels can crash the app"
  ```

#### **Smart Context Loading**
- Automatically skips generated code (`.generated`, `.min`, `.bundle`)
- Skips build artifacts (`node_modules`, `dist`, `Pods`, `DerivedData`)
- Detects code files by extension
- Finds related files through import analysis
- Prioritizes recently changed files (git diff)
- Limits to 100 files for performance

---

### 📊 Analyzer Coverage (405+ Total Checks)

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
| **CustomRulesAnalyzer** | ∞ | Your team's custom rules |

---

### 💻 Usage Examples

#### **Basic Review**
```bash
flaco
> /review                      # Review entire project
> /review MyViewModel.swift    # Review specific file
> /review --security           # Security-focused review
> /review --save report.md     # Save report to file
```

#### **CI/CD Pipeline**
```bash
# GitHub Actions
flaco << EOF
/review --ci
EOF
# Exit code 1 if HIGH+ issues, 0 if clean
```

#### **Track Progress**
```bash
# Week 1: Establish baseline
> /review --baseline

# Week 2: Check new issues
> /review --compare
# Output: 15 new issues, 8 fixed, 42 unchanged
```

#### **Interactive Fixes**
```bash
> /review --fix
# Interactively apply fixes for force unwrap, weak self, etc.
```

#### **Export to GitHub**
```bash
> /review --export-github
# Creates GitHub issues for HIGH+ severity findings
```

---

### 🔧 Technical Details

**New Modules:**
- `flacoai/baseline_manager.py` (175 lines) - Baseline tracking
- `flacoai/fix_applicator.py` (262 lines) - Interactive fixes
- `flacoai/integrations/github_exporter.py` (174 lines) - GitHub export
- `flacoai/smart_context.py` (305 lines) - Smart file discovery
- `flacoai/analyzers/custom_rules_analyzer.py` (372 lines) - Custom rules

**Enhanced Modules:**
- `flacoai/coders/review_prompts.py` - Structured output format
- `flacoai/commands.py` - New /review flags
- `flacoai/coders/review_coder.py` - Custom rules integration
- `flacoai/__init__.py` - Version bumped to 2.0.0

**Total Changes:**
- **Files Changed**: 11 new files, 4 modified files
- **Lines Added**: ~2,400+
- **Features Added**: 7 major professional features
- **Analyzers**: 12 total (11 built-in + custom rules)

---

### 📦 Installation

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

---

### 🔄 Upgrading from v1.x

```bash
cd /path/to/flaco.cli
git pull
python3 scripts/install_flaco.py
source ~/.zshrc
```

**Breaking Changes:**
- None! v2.0.0 is fully backward compatible with v1.x

**New Environment Variables:**
- None required, but you can use `.flaco/rules.yaml` for custom rules

---

### 🦙 Ollama Integration

Flaco AI works perfectly with local Ollama models:

```bash
# Configure Ollama
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"

# Run with local model
flaco --model openai/qwen2.5-coder:32b

# Or remote Ollama server
export OPENAI_API_BASE="http://192.168.1.100:11434/v1"
```

**Recommended Models:**
- `qwen2.5-coder:32b` - Best for iOS development
- `deepseek-r1:32b` - Excellent for architecture review
- `deepseek-coder-v2:16b` - Fast and efficient

---

### 🎯 What's Next?

**v2.1.0** (Code Generation):
- `/generate` - SwiftUI template generation
- `/screenshot` - Vision-based UI generation

**v2.2.0** (Xcode Integration):
- `/xcode` - Project manipulation
- Build system integration

**v2.3.0** (Design Tools):
- `/figma` - Figma to SwiftUI
- Sketch/Adobe XD support

**v3.0.0** (AI Pair Programmer):
- Full context awareness
- Multi-file refactoring
- Architectural suggestions

---

### 📝 Full Changelog

**v2.0.0** (2026-01-03)

**Features:**
- ✨ Enhanced review output with structured sections
- ✨ Interactive fix application with before/after preview
- ✨ CI/CD integration with JSON output and exit codes
- ✨ Baseline tracking to show only new issues
- ✨ GitHub issues export for HIGH+ severity findings
- ✨ Custom team rules via .flaco/rules.yaml
- ✨ Smart context loading
- ✨ 405+ total automated checks across 11 analyzers

**Bug Fixes:**
- 🐛 Fixed version number (was stuck at 1.0.0)
- 🐛 Fixed tree-sitter API compatibility (v0.25+)
- 🐛 Fixed scipy dependency crash

**Documentation:**
- 📚 Complete README rewrite for v2.0.0
- 📚 CI/CD integration examples
- 📚 Custom rules guide with examples

---

**Made with ❤️ for iOS Developers**

*Catch bugs before they catch you.*

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
