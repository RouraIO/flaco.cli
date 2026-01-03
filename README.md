# 🍎 Flaco AI - The Ultimate iOS Development Platform

**Build. Generate. Ship. All in your terminal.**

Flaco AI is an AI-powered iOS development platform that transforms how you build Swift and SwiftUI apps. From converting design mockups to production-ready code, to managing Xcode projects without leaving your terminal – Flaco AI is your complete iOS development companion.

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
║              🍎 The Ultimate iOS Development Platform 🚀                  ║
║                 Build. Generate. Ship. All in your terminal.             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## ⚡ What Makes Flaco AI Different?

### 🎨 Design to Code in Seconds
Convert any UI mockup or screenshot to production-ready SwiftUI code using vision AI:
```bash
/screenshot login_mockup.png --save LoginView.swift
```

### 🏗️ SwiftUI Code Generation
Generate SwiftUI views from templates instantly:
```bash
/generate login for MyApp
/generate list of tasks
/generate settings
```

### 📱 Xcode Project Management
Add and manage files in your Xcode project without opening Xcode:
```bash
/xcode add-file LoginView.swift
/xcode list-targets
```

### 🔍 Comprehensive Code Review
Get staff-level PR reviews with security, performance, and architecture analysis:
```bash
/review
/review LoginViewController.swift
```

### 🏠 Local-First with Ollama
Run powerful models locally for complete privacy:
```bash
# Works with Ollama models out of the box
flaco --model openai/qwen2.5-coder:32b
```

### 🎟️ Jira Integration
Ticket-driven development made easy:
```bash
/jira link PROJ-123
/jira plan
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
```

### Your First Workflow

```bash
# Navigate to your iOS project
cd ~/Projects/MyiOSApp

# Start Flaco AI
flaco

# Generate a SwiftUI view
/generate login for MyApp --save LoginView.swift

# Add to Xcode project
/xcode add-file LoginView.swift

# Review the code
/review LoginView.swift

# Done! 🎉
```

---

## 🎯 Key Features

### 📸 Screenshot to SwiftUI Code

Convert design mockups to working SwiftUI code:

```bash
# Basic conversion
/screenshot mockup.png

# Save directly to file
/screenshot design.jpg --save OnboardingView.swift

# Preview analysis without code
/screenshot ui-design.png --preview

# Full workflow
/screenshot login_mockup.png --save LoginView.swift
/xcode add-file LoginView.swift
```

**Supports:**
- PNG, JPG, JPEG, PDF formats
- GPT-4V, Claude 3, Gemini vision models
- Accurate layout, colors, spacing
- SF Symbols detection
- Production-ready code

### 🎨 SwiftUI Template Generation

5 professional SwiftUI templates:

```bash
# Login View
/generate login for FitApp

# Settings View
/generate settings

# List View with CRUD
/generate list of workouts

# Detail View
/generate detail for workout

# TabView Navigation
/generate tabview
```

**All templates include:**
- Modern SwiftUI best practices (iOS 15+)
- Proper state management
- SF Symbols
- #Preview for testing
- Accessibility labels
- Clean, well-commented code

### 📱 Xcode Project Management

Manage your Xcode project from the terminal:

```bash
# Show project info
/xcode

# List all targets
/xcode list-targets

# List files in target
/xcode list-files MyApp

# Add file to project
/xcode add-file NewView.swift

# Add to specific target
/xcode add-file Feature.swift MyAppTests

# Remove file
/xcode remove-file OldView.swift
```

**Features:**
- Auto-discovers Xcode projects
- Smart source file detection
- Preserves project structure
- Multi-target support

### 🔍 Advanced Code Review

Get comprehensive PR-style reviews:

```bash
# Review entire project
/review

# Review specific file
/review LoginViewController.swift

# Focus on specific aspects
/review --security
/review --performance
/review --architecture

# Save review report
/review --save review_report.md
```

**Analysis includes:**
- Security vulnerabilities (OWASP Top 10)
- Performance bottlenecks
- Code quality issues
- Architecture suggestions
- iOS best practices
- HIG compliance

### 🎟️ Jira-Driven Development

Work ticket-first with Jira integration:

```bash
# Link to Jira ticket
/jira link PROJ-123

# Generate implementation plan
/jira plan

# Create issue from code
/jira create

# View ticket details
/jira show PROJ-456
```

### 🧠 Project Memory

Flaco AI learns your project:

```bash
# Initialize project memory
/init

# Add project-specific rules
/memory note "We use MVVM architecture"
/memory note "All API calls go through NetworkManager"

# View project memory
/memory show
```

---

## 🛠️ Complete Workflow Example

### From Mockup to Production

```bash
# 1. Start with a design
/screenshot onboarding.png --save OnboardingView.swift

# 2. Add to Xcode
/xcode add-file OnboardingView.swift

# 3. Review the code
/review OnboardingView.swift

# 4. Make changes (if needed)
> Update the OnboardingView to use our custom color palette

# 5. Commit with good message
/commit-msg

# 6. Link to Jira
/jira link PROJ-789

# 7. Push to GitHub
> /git push

# Done! Design → Production in minutes
```

### Rapid Prototyping

```bash
# Generate multiple screens
/generate login --save LoginView.swift
/generate settings --save SettingsView.swift
/generate list of tasks --save TaskListView.swift
/generate tabview --save MainTabView.swift

# Add all to Xcode
/xcode add-file LoginView.swift
/xcode add-file SettingsView.swift
/xcode add-file TaskListView.swift
/xcode add-file MainTabView.swift

# Review the app structure
/review

# Boom! Full app skeleton ready
```

---

## 🏠 Local LLM Setup (Ollama)

Run Flaco AI completely offline with Ollama:

### Install Ollama

```bash
# macOS
brew install ollama

# Start Ollama service
ollama serve
```

### Pull Recommended Models

```bash
# Best for iOS development (32B parameters)
ollama pull qwen2.5-coder:32b

# Faster alternative (16B parameters)
ollama pull deepseek-coder-v2:16b

# With reasoning capabilities
ollama pull deepseek-r1:32b
```

### Configure Flaco AI

```bash
# Set Ollama as API endpoint
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"

# Run Flaco with local model
flaco --model openai/qwen2.5-coder:32b
```

### Remote Ollama

```bash
# Use Ollama on another machine
export OPENAI_API_BASE="http://192.168.1.100:11434/v1"
flaco --model openai/qwen2.5-coder:32b
```

---

## 📚 All Commands

### Code Generation
```bash
/generate <template> [prompt]      # Generate SwiftUI from template
/screenshot <image> [--save]       # Convert screenshot to SwiftUI
```

### Project Management
```bash
/xcode                             # Show project info
/xcode list-targets                # List all targets
/xcode add-file <path> [target]   # Add file to project
/xcode remove-file <path>          # Remove file from project
```

### Code Review & Analysis
```bash
/review [file]                     # Comprehensive code review
/review --security                 # Security-focused review
/review --performance              # Performance analysis
/init                              # Initialize project memory
```

### Jira Integration
```bash
/jira link <KEY>                   # Link to Jira ticket
/jira plan                         # Generate implementation plan
/jira create                       # Create Jira issue
/jira show <KEY>                   # View ticket details
```

### Git & Commits
```bash
/commit-msg                        # Generate commit message
/diff                              # Natural language diff summary
/git <command>                     # Run git commands
```

### Modes
```bash
/mode architect                    # Design-focused mode
/mode bugfix                       # Debugging mode
/mode refactor                     # Code quality mode
```

### Utilities
```bash
/help                              # Show all commands
/model <name>                      # Switch AI model
/memory note <text>                # Add to project memory
/tour                              # Generate codebase tour
/standup                           # Daily standup summary
```

---

## 🎨 SwiftUI Templates

### Login View
```bash
/generate login for MyApp
```
- Email/password fields
- Loading states
- Error handling
- Forgot password link
- Sign up navigation

### Settings View
```bash
/generate settings
```
- Toggle switches
- Navigation links
- Account management
- App info section

### List View
```bash
/generate list of tasks
```
- Search functionality
- Add/delete operations
- Pull to refresh
- Empty state
- Swipe actions

### Detail View
```bash
/generate detail for task
```
- Image header
- Metadata display
- Edit/share/delete
- Confirmation alerts

### TabView
```bash
/generate tabview
```
- 4 customizable tabs
- SF Symbols icons
- Tab navigation

---

## 📸 Vision Model Support

For screenshot-to-code conversion:

### Recommended Models
- **GPT-4o** - Most accurate (OpenAI)
- **Claude 3 Opus** - Great design understanding (Anthropic)
- **Claude 3 Sonnet** - Fast, good quality (Anthropic)
- **Gemini Pro Vision** - Good alternative (Google)

### Switch Models
```bash
/model gpt-4o
/model claude-3-opus
/model gemini-pro-vision
```

---

## ⚙️ Configuration

### Setup Wizard

Interactive setup on first run:

```bash
flaco --setup
```

Configures:
- Ollama or cloud API
- Model selection
- Jira credentials (optional)
- Git settings
- Color theme

### Manual Configuration

Edit `~/.flacoai.conf.yml`:

```yaml
# Model Configuration
model: openai/qwen2.5-coder:32b
api-base: http://localhost:11434/v1

# UI Configuration
assistant-output-color: "#00FFFF"
dark-mode: true

# Jira Configuration
jira-url: https://yourcompany.atlassian.net
jira-email: your@email.com

# Git Configuration
auto-commits: true
```

---

## 🎯 Why Flaco AI for iOS Development?

### Speed
- Generate SwiftUI views in seconds
- Convert designs to code instantly
- Manage Xcode without context switching

### Quality
- Production-ready code
- iOS best practices built-in
- Comprehensive code reviews

### Privacy
- Local LLM support via Ollama
- No cloud required
- Your code stays on your machine

### Integration
- Works with your existing workflow
- Xcode project management
- Jira ticket tracking
- Git integration

---

## 📦 Requirements

- **Python**: 3.10 - 3.14 (3.14 recommended)
- **OS**: macOS or Linux
- **Git**: Required
- **Xcode**: For iOS development (optional for Flaco AI itself)

### Optional
- **Ollama**: For local models
- **Jira Account**: For ticket integration
- **Vision Model**: For screenshot conversion (GPT-4V, Claude 3, etc.)

---

## 🚢 Deployment Workflow

### TestFlight Integration (Coming Soon)

```bash
/testflight upload
```

### Figma Integration (Coming Soon)

```bash
/figma import <url>
```

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone repository
git clone https://github.com/RouraIO/flaco.cli.git
cd flaco.cli

# Install in development mode
pip install -e .

# Run tests
pytest tests/
```

---

## 📝 Documentation

- [Installation Guide](docs/installation.md)
- [Command Reference](docs/commands.md)
- [SwiftUI Templates](docs/templates.md)
- [Xcode Integration](docs/xcode.md)
- [Vision Models](docs/vision.md)
- [Jira Integration](docs/jira.md)
- [Troubleshooting](docs/troubleshooting.md)

---

## 🌟 Showcase

### What Developers Are Building

- 🏋️ Fitness tracking apps
- 📱 Social media platforms
- 🎮 Mobile games
- 📊 Business dashboards
- 🛍️ E-commerce apps

---

## 📊 Project Status

**Current Version**: v1.4.0

### Recent Releases
- ✅ v1.4.0 - Screenshot-to-Code conversion
- ✅ v1.3.0 - Xcode project manipulation
- ✅ v1.2.0 - SwiftUI template generation
- ✅ v1.1.0 - UI improvements

### Coming Soon (v2.0.0)
- 🎨 iOS-specific branding
- 🔍 Advanced PR-style reviews with Jira intelligence
- 🍎 SF Symbols integration
- 📐 Apple HIG validation
- 🔒 iOS security scanning
- 🎨 Figma-to-SwiftUI converter
- 🚀 TestFlight integration
- 📚 Comprehensive documentation
- 🧪 Full test coverage

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

Built with:
- [Claude](https://claude.ai) by Anthropic
- [OpenAI GPT-4](https://openai.com)
- [Ollama](https://ollama.ai) for local models
- Based on [Aider](https://github.com/paul-gauthier/aider)

---

## 🔗 Links

- **GitHub**: https://github.com/RouraIO/flaco.cli
- **Issues**: https://github.com/RouraIO/flaco.cli/issues
- **Releases**: https://github.com/RouraIO/flaco.cli/releases

---

**Made with ❤️ for iOS developers**

🍎 Build amazing iOS apps. Fast. 🚀
