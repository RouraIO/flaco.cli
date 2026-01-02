# 🚀 Flaco AI

**The Ultimate Local-First Swift & iOS Development Assistant**

Flaco AI is an AI-powered coding assistant specifically designed for Swift and iOS development. Built on proven technology with a focus on local LLMs and ticket-driven workflows, Flaco AI helps you build better iOS apps faster.

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
║        🚀 The Ultimate Local-First Swift & iOS Development Assistant      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## ✨ Features

### 🍎 Swift & iOS First
Optimized for Swift/iOS development with deep understanding of:
- SwiftUI and UIKit patterns
- iOS best practices and conventions
- Xcode project structures
- Swift Package Manager
- Common iOS architectures (MVVM, VIPER, etc.)

### 🏠 Local LLM Support
Work privately with local models via Ollama:
- Qwen 2.5 Coder 32B
- DeepSeek Coder V2 16B
- DeepSeek R1 32B (with reasoning)
- Or use cloud models (Claude, GPT-4, etc.)

### 🎟️ Jira Integration
Seamless ticket-driven development:
- Link commits to Jira issues
- Generate implementation plans from tickets
- Create issues from code reviews
- Track work directly from the terminal

### 🧠 Project Memory
Persistent project understanding:
- Auto-detects Swift/iOS projects
- Remembers your coding conventions
- Learns your architecture patterns
- Preserves project-specific rules

### 🛠️ Development Modes
Work in specialized modes:
- **Architect Mode** - Design-focused planning
- **Bugfix Mode** - Surgical debugging
- **Refactor Mode** - Code quality improvements

### 🔍 Code Analysis
Comprehensive review system:
- Security analysis (OWASP Top 10)
- Performance optimization suggestions
- Code quality checks
- Architecture validation

## 🚀 Quick Start

### Requirements

- **Python 3.10 - 3.14** (Python 3.14 recommended)
- macOS or Linux
- Git

### Installation

```bash
# Verify Python version (3.10-3.14 required)
python3 --version

# Clone the repository
git clone git@github.com:RouraIO/flaco.cli.git flaco
cd flaco

# Run the installer
python3 scripts/install_flaco.py

# Reload your shell
source ~/.zshrc  # or open a new terminal
```

### First Run

```bash
# Navigate to your Swift/iOS project
cd ~/Projects/MyiOSApp

# Start Flaco AI
flaco.ai

# Initialize project memory
/init

# Start coding!
```

## 📚 Key Commands

### Project Management
- `/init` - Analyze project and create FlacoAI.md knowledge base
- `/memory show` - View project memory
- `/memory note <text>` - Add quick notes
- `/summary` - Get project overview

### Development Workflow
- `/mode architect` - Switch to architecture mode
- `/plan <task>` - Generate implementation plan
- `/tour [component]` - Get guided codebase tour
- `/review` - Comprehensive code review

### Git Integration
- `/diff` - Show changes since last message
- `/commit-msg` - AI-generated commit messages
- `/review-diff` - Review uncommitted changes
- `/commit` - Create commits with smart messages

### Jira Integration
- `/jira link <KEY>` - Link current work to ticket
- `/jira plan <KEY>` - Break down ticket into steps
- `/jira show <KEY>` - Display ticket details
- `/jira my` - Show your assigned tickets

### LLM Management
- `/llm list` - Show available models
- `/llm use <model>` - Switch models
- `/llm search <term>` - Find specific models

### Productivity
- `/standup [days]` - Generate standup summary
- `/plan <task>` - Create implementation plan

## 🎯 Recommended Workflow

### Ticket-First Development
```bash
# 1. Start with a Jira ticket
flaco.ai
/jira show PROJ-123

# 2. Generate implementation plan
/jira plan PROJ-123

# 3. Link to ticket and start work
/jira link PROJ-123
/mode architect

# 4. Make changes (Flaco AI helps you code)

# 5. Review before committing
/review-diff

# 6. Generate commit message
/commit-msg --write

# 7. Update standup
/standup
```

### Learning a New Codebase
```bash
# 1. Initialize project memory
/init

# 2. Get a guided tour
/tour

# 3. Review project memory
/memory show

# 4. Ask questions
> What architecture pattern does this project use?
> How is navigation handled?
> Where should I add new features?
```

## 🔧 Configuration

### Model Aliases
Quick shortcuts for popular models:
- `flaco.ai` - Default model (configured in settings)
- `flaco.ai.qwen` - Qwen 2.5 Coder 32B
- `flaco.ai.ds` - DeepSeek Coder V2 16B
- `flaco.ai.r1` - DeepSeek R1 32B (reasoning)

### Environment Variables
```bash
# Jira Integration
export JIRA_SERVER="https://your-company.atlassian.net"
export JIRA_USERNAME="you@company.com"
export JIRA_API_TOKEN="your_api_token"
export JIRA_PROJECT="PROJ"

# Local LLM (default)
export OPENAI_API_BASE="http://192.168.20.3:11434/v1"
export OPENAI_API_KEY="ollama"  # placeholder for Ollama
```

### FlacoAI.md
Each project gets a `FlacoAI.md` memory file with:
- **Project Overview** - Auto-detected type and features
- **Architecture** - Detected patterns (MVVM, VIPER, etc.)
- **Directory Structure** - Auto-mapped
- **Swift/iOS Conventions** - Your custom rules (manual section)
- **Rules & Preferences** - Project-specific guidelines (manual section)
- **Known Quirks** - Gotchas and workarounds (manual section)

Manual sections are preserved when you run `/init` or `/memory refresh`.

## 🤝 Contributing

Flaco AI is built and maintained by Christopher J. Roura for the iOS development community.

**Repository:** git@github.com:RouraIO/flaco.cli.git

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Credits

Flaco AI is built on top of flacoai by Paul Gauthier and the flacoai team. We've transformed it into a specialized Swift/iOS development assistant with enhanced Jira integration, project memory, and local LLM support.

---

**Happy Coding!** 🎉

For questions, issues, or feature requests, please open an issue on GitHub.
