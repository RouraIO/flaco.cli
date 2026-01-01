# 🚀 Running FlacoAI - See All Your Changes!

## ✨ The Easy Way (Recommended)

```bash
cd /Users/roura.io/Documents/dev.local/flaco
./run-flaco.sh
```

That's it! This will start FlacoAI with all your new features.

---

## 📺 What You'll See

When you run `./run-flaco.sh`, you'll see this beautiful startup screen:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███████╗██╗      █████╗  ██████╗ ██████╗      █████╗ ██╗               ║
║   ██╔════╝██║     ██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██║               ║
║   █████╗  ██║     ███████║██║     ██║   ██║    ███████║██║               ║
║   ██╔══╝  ██║     ██╔══██║██║     ██║   ██║    ██╔══██║██║               ║
║   ██║     ███████╗██║  ██║╚██████╗╚██████╔╝    ██║  ██║██║               ║
║   ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝  ╚═╝╚═╝               ║
║                                                                           ║
║              🚀 The Ultimate AI-Powered Development Assistant             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Good afternoon, Christopher! Welcome back.

FlacoAI v0.86.1 (Enhanced AI Coding Assistant)
Model: claude-sonnet-4-5 with diff edit format
Git repo: /your/project with X files
Repo-map: using 2048 tokens, auto refresh

💡 Tip: 🔍 Use /review to get comprehensive security, performance & quality analysis

>
```

---

## 🎯 Test Your New Features

Once FlacoAI is running, try these commands:

### 1. Test Code Review

```bash
> /help
# Look for /review command

> /review --help
# See all review options

# Create a test file
> /add test.py
```

### 2. Test Jira Integration

```bash
> /jira
# Should show usage or config error

> /help jira
# See all jira commands
```

### 3. Test Branding

The branding is automatically shown on startup! You should see:
- ✅ Beautiful boxed ASCII art header
- ✅ Personalized greeting
- ✅ "FlacoAI v0.86.1 (Enhanced AI Coding Assistant)"
- ✅ Random tips with emojis
- ✅ (After multiple sessions) Activity tracking

---

## 🛠️ Advanced Usage

### Run in a Specific Project

```bash
cd ~/your-project
/Users/roura.io/Documents/dev.local/flaco/run-flaco.sh
```

### Pass Arguments

```bash
./run-flaco.sh --model gpt-4
./run-flaco.sh --help
./run-flaco.sh --no-show-flaco-branding  # Disable fancy header
```

### Create an Alias (Optional)

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
alias flaco='/Users/roura.io/Documents/dev.local/flaco/run-flaco.sh'
```

Then you can just run:

```bash
flaco
```

---

## 🧪 Full Feature Test

Here's a complete test scenario:

```bash
# 1. Navigate to test directory
mkdir -p ~/test-flaco-demo
cd ~/test-flaco-demo
git init

# 2. Create a test file with intentional issues
cat > vulnerable.py << 'EOF'
import os

def get_user_data(user_id):
    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def slow_function(data):
    # Performance issue - O(n²)
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] + data[j])
    return result

# Hardcoded password
PASSWORD = "admin123"
EOF

# 3. Start FlacoAI
/Users/roura.io/Documents/dev.local/flaco/run-flaco.sh

# 4. Inside FlacoAI, run:
> /add vulnerable.py
> /review vulnerable.py

# 5. You should see detailed analysis of:
#    - SQL injection vulnerability
#    - Performance issue (O(n²) complexity)
#    - Hardcoded credentials
#    - Code quality suggestions
```

---

## ✅ Success Checklist

When you run `./run-flaco.sh`, verify:

- [ ] Beautiful boxed header appears
- [ ] Greeting says "Good [time], [Your Name]!"
- [ ] Version shows "FlacoAI v0.86.1 (Enhanced AI Coding Assistant)"
- [ ] Random tip appears at bottom with emoji
- [ ] `/review` command exists (type `/help` to see it)
- [ ] `/jira` command exists (type `/help` to see it)
- [ ] No errors or import failures

---

## 🐛 Troubleshooting

### Issue: Script says "permission denied"

```bash
chmod +x /Users/roura.io/Documents/dev.local/flaco/run-flaco.sh
```

### Issue: "ModuleNotFoundError"

The script sets PYTHONPATH automatically. If you still get errors:

```bash
cd /Users/roura.io/Documents/dev.local/flaco/flacoai
source ../venv/bin/activate
python -c "from aider import branding; print('OK')"
```

### Issue: Still seeing old header

Make sure you're running the NEW script:

```bash
# Full path
/Users/roura.io/Documents/dev.local/flaco/run-flaco.sh

# NOT the old way:
# python -m aider  ← This might run old version
```

### Issue: Command not found errors

Make sure virtual environment has dependencies:

```bash
source venv/bin/activate
pip install rich jira beautifulsoup4 gitpython
```

---

## 📁 What Changed?

Here's a summary of all the new files and modifications:

### New Files Created:
1. `flacoai/aider/branding.py` - Beautiful FlacoAI header & tips
2. `flacoai/aider/activity_tracker.py` - Session activity tracking
3. `flacoai/aider/analyzers/` - Code review system (7 files)
4. `flacoai/aider/integrations/` - Jira integration (3 files)
5. `flacoai/aider/coders/review_coder.py` - Review orchestrator
6. `flacoai/aider/report_generator.py` - Report formatting

### Modified Files:
1. `flacoai/aider/coders/base_coder.py` - Integrated branding in startup
2. `flacoai/aider/commands.py` - Added /review and /jira commands
3. `flacoai/aider/main.py` - Added activity tracking
4. `flacoai/aider/args.py` - Added branding arguments
5. `flacoai/requirements.txt` - Added jira dependency

---

## 🎉 You're All Set!

Your FlacoAI is now enhanced with:

✅ **Beautiful Branding** - Professional Claude-style header
✅ **Code Review** - 4 analyzers (Security, Performance, Quality, Architecture)
✅ **Jira Integration** - Full ticket management from terminal
✅ **Activity Tracking** - See your usage stats
✅ **Smart Tips** - Context-aware tips on startup

Enjoy your enhanced AI coding assistant! 🚀

---

## 📞 Quick Reference

```bash
# Run FlacoAI
./run-flaco.sh

# Test branding
./run-flaco.sh  # Just start it and look!

# Test review
# (inside FlacoAI):
> /review
> /review <filename>
> /review --security

# Test Jira
# (inside FlacoAI):
> /jira
> /jira my
> /jira create PROJ "Issue title"

# Disable branding
./run-flaco.sh --no-show-flaco-branding
```

**Created by Christopher J. Roura** | FlacoAI Project
