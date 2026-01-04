# 🚀 FlacoAI Quick Start Guide

## Installation & Setup

### Step 1: Activate Virtual Environment (if not already active)

```bash
cd /Users/roura.io/Documents/dev.local/flaco

# If venv doesn't exist, create it
python3 -m venv venv

# Activate it
source venv/bin/activate
```

### Step 2: Install FlacoAI

```bash
# Install in development mode
pip install -e flacoai/

# Or install dependencies manually
pip install -r flacoai/requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in your project directory:

```bash
# API Keys (required for AI features)
OPENAI_API_KEY=your_key_here
# or
ANTHROPIC_API_KEY=your_key_here

# Jira Integration (optional)
JIRA_SERVER=https://your-company.atlassian.net
JIRA_USERNAME=your.email@company.com
JIRA_API_TOKEN=your_jira_api_token
JIRA_PROJECT=PROJ
```

### Step 4: Run FlacoAI

```bash
# Basic usage
flaco

# Or if that doesn't work
python -m flacoai

# With specific model
flaco --model gpt-4

# In a specific directory
cd your-project
flaco
```

---

## 🎯 Testing New Features

### Feature 1: Custom Branding ✨

```bash
# Start FlacoAI - you should see the beautiful header
flaco

# Expected output:
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║   ███████╗██╗      █████╗  ██████╗ ██████╗      █████╗ ██╗               ║
# ║   FlacoAI startup screen with activity tracking...                       ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# Disable branding if needed
flaco --no-show-flaco-branding
```

### Feature 2: Code Review 🔍

```bash
# Inside FlacoAI terminal:

# Review entire project
/review

# Review specific file
/review src/app.py

# Review with specific analyzers
/review --security
/review --performance
/review --quality
/review --architecture

# Save report to file
/review --save code-review-report.md

# Review a file without extension (smart search)
/review app  # finds app.py, app.js, etc.
```

### Feature 3: Jira Integration 🎟️

```bash
# Inside FlacoAI terminal:

# Search issues
/jira search "project = PROJ AND status = 'In Progress'"

# Show specific issue
/jira show PROJ-123

# Create new issue
/jira create PROJ "Fix login bug" "Description here"

# Add comment
/jira comment PROJ-123 "Working on this now"

# Update status
/jira status PROJ-123 "In Progress"

# Show my issues
/jira my

# Show my issues with specific status
/jira my "In Progress"

# Create tickets from code review
/review
/jira from-review

# Link current work to issue
/jira link PROJ-123
```

### Feature 4: Activity Tracking 📊

```bash
# Activity is tracked automatically
# On startup, you'll see:
# 📊 Recent Activity (last 7 days):
#    5 sessions · 12 files edited · 2 repos
#    Top commands: review, jira, add

# Activity is saved to: ~/.flacoai/cache/flaco_activity.json
```

---

## 🧪 Testing the Installation

### Quick Verification Test

```bash
# 1. Start FlacoAI
flaco

# 2. You should see:
#    ✅ FlacoAI ASCII header
#    ✅ Personalized welcome message
#    ✅ Version info
#    ✅ Model information
#    ✅ Random tip
#    ✅ (Optional) Recent activity

# 3. Test basic commands
/help
/model
/map

# 4. Test new features
/review
/jira
```

### Full Feature Test

```bash
# Create a test project
mkdir ~/test-flaco
cd ~/test-flaco
git init

# Create a test file with intentional issues
cat > test.py << 'EOF'
import os

def get_user(user_id):
    # SQL Injection vulnerability (for testing)
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def process_data(data):
    # Inefficient loop (for testing)
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] + data[j])
    return result
EOF

# Start FlacoAI
flaco

# Inside FlacoAI:
/add test.py
/review test.py

# You should see:
# ✅ Security issues detected (SQL injection)
# ✅ Performance issues detected (O(n²) loop)
# ✅ Quality suggestions
```

---

## 🛠️ Troubleshooting

### Issue: Command 'flaco' not found

**Solution:**
```bash
# Option 1: Use python module
python -m flacoai

# Option 2: Install properly
cd /Users/roura.io/Documents/dev.local/flaco
pip install -e flacoai/

# Option 3: Add to PATH
export PATH="$PATH:/Users/roura.io/Documents/dev.local/flaco/flacoai"
```

### Issue: Module import errors

**Solution:**
```bash
# Reinstall dependencies
pip install -r flacoai/requirements.txt

# Or install specific missing modules
pip install jira beautifulsoup4 rich
```

### Issue: Branding not showing

**Solution:**
```bash
# Check if rich console is available
python -c "from rich.console import Console; print('OK')"

# Run with branding explicitly enabled
flaco --show-flaco-branding

# Check if io.console is available (might fallback to simple output)
```

### Issue: Review command not working

**Solution:**
```bash
# Make sure you're in a git repository
git init

# Check if tree-sitter is installed
pip install tree-sitter tree-sitter-language-pack

# Try reviewing a specific file
/review --help
/review <filepath>
```

### Issue: Jira commands failing

**Solution:**
```bash
# Verify environment variables
echo $JIRA_SERVER
echo $JIRA_USERNAME

# Test Jira connection
/jira my

# Check credentials in .env file
cat .env | grep JIRA
```

---

## 📁 File Structure Overview

```
flacoai/
├── flacoai/
│   ├── analyzers/              # Code review analyzers
│   │   ├── __init__.py
│   │   ├── base_analyzer.py
│   │   ├── security_analyzer.py
│   │   ├── performance_analyzer.py
│   │   ├── quality_analyzer.py
│   │   └── architecture_analyzer.py
│   │
│   ├── integrations/           # External integrations
│   │   ├── __init__.py
│   │   ├── jira_client.py
│   │   └── jira_formatter.py
│   │
│   ├── coders/                 # Coder implementations
│   │   ├── review_coder.py
│   │   └── review_prompts.py
│   │
│   ├── branding.py            # FlacoAI branding
│   ├── activity_tracker.py    # Session tracking
│   ├── report_generator.py    # Review reports
│   ├── commands.py            # Extended with /review and /jira
│   ├── args.py                # Added branding args
│   └── main.py                # Added activity tracking
```

---

## 🎨 Expected Startup Experience

When you run `flaco`, you should see:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███████╗██╗      █████╗  ██████╗ ██████╗      █████╗ ██╗                ║
║   ██╔════╝██║     ██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██║                ║
║   █████╗  ██║     ███████║██║     ██║   ██║    ███████║██║                ║
║   ██╔══╝  ██║     ██╔══██║██║     ██║   ██║    ██╔══██║██║                ║
║   ██║     ███████╗██║  ██║╚██████╗╚██████╔╝    ██║  ██║██║                ║
║   ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝                ║
║                                                                           ║
║              🚀 The Ultimate AI-Powered Development Assistant             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Good afternoon, Christopher! Welcome back.

FlacoAI v0.86.1 (Enhanced AI Coding Assistant)
Model: claude-sonnet-4-5 with diff edit format
Git repo: /Users/roura.io/Documents/dev.local/flaco with 247 files
Repo-map: using 2048 tokens, auto refresh

📊 Recent Activity (last 7 days):
   5 sessions · 12 files edited · 2 repos
   Top commands: review, jira, add

💡 Tip: 🔍 Use /review to get comprehensive security, performance & quality analysis

>
```

---

## 🚀 Next Steps

1. **Test all features** using the commands above
2. **Review the code** you've created with `/review`
3. **Explore Jira integration** if you have a Jira instance
4. **Check activity tracking** after a few sessions
5. **Read the full documentation** in the repo

## 📚 Additional Resources

- **Help**: Type `/help` inside FlacoAI
- **Model switching**: `/model` to change LLM
- **Repository map**: `/map` to see code structure
- **Architecture mode**: `/architect` for planning

---

**Need more help?** Check the main README or create an issue on GitHub.

**Created by Christopher J. Roura** | FlacoAI v1.0
