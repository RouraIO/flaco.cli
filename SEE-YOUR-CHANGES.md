# 👀 How to See Your FlacoAI Changes

## 🚀 Quick Start (3 Steps)

### Step 1: Run the Refresh Script

```bash
cd /Users/roura.io/Documents/dev.local/flaco
./refresh-install.sh
```

### Step 2: Test the Installation

```bash
# After installation completes, test with:
python -m aider --help
```

### Step 3: See the Beautiful Header

```bash
# Create a test directory (or use existing project)
mkdir -p ~/test-flaco && cd ~/test-flaco
git init

# Run FlacoAI
python -m aider
```

You should now see the **new FlacoAI header** with:
- ✅ Beautiful ASCII box art
- ✅ Personalized welcome message
- ✅ Activity tracking (if you have previous sessions)
- ✅ Random tips

---

## 📋 Manual Installation (Alternative)

If the script doesn't work, follow these manual steps:

```bash
# 1. Navigate to FlacoAI directory
cd /Users/roura.io/Documents/dev.local/flaco

# 2. Activate or create virtual environment
source venv/bin/activate  # Or: python3 -m venv venv && source venv/bin/activate

# 3. Uninstall old version
pip uninstall -y aider-chat

# 4. Install new version in development mode
cd flacoai
pip install -e .

# 5. Return to project directory
cd ..

# 6. Run FlacoAI
python -m aider
```

---

## 🧪 Verify New Features Work

### Test 1: Branding & Header

```bash
# Start FlacoAI in any git repository
cd ~/your-project  # or mkdir ~/test && cd ~/test && git init
python -m aider

# Expected: Beautiful boxed header with FlacoAI ASCII art
```

**What you should see:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ███████╗██╗      █████╗  ██████╗ ██████╗      █████╗ ██╗               ║
║   ██╔════╝██║     ██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██║               ║
║   █████╗  ██║     ███████║██║     ██║   ██║    ███████║██║               ║
...
Good [morning/afternoon/evening], [Your Name]! Welcome back.

FlacoAI v0.86.1 (Enhanced AI Coding Assistant)
...
💡 Tip: [Random tip about FlacoAI features]
```

### Test 2: Code Review Feature

```bash
# Inside FlacoAI prompt:
> /help

# Look for /review command in the list
# Then test it:
> /review --help
```

**Expected output:**
```
/review                    - Review entire project automatically
/review <filename>         - Review specific file (can omit extension)
/review --security         - Only security analysis
/review --performance      - Only performance analysis
/review --quality          - Only quality analysis
/review --architecture     - Only architecture analysis
/review --save <file>      - Save report to file
```

### Test 3: Jira Integration

```bash
# Inside FlacoAI prompt:
> /jira

# You should see usage information or error about Jira config
```

**Expected output:**
```
Usage: /jira <subcommand> [args...]
Type '/help jira' for details
```

### Test 4: Activity Tracking

```bash
# After running FlacoAI a few times, you should see:
📊 Recent Activity (last 7 days):
   X sessions · Y files edited · Z repos
   Top commands: ...
```

---

## 🐛 Troubleshooting

### Issue: Still seeing old header

**Cause:** Old version still installed or not running from correct location

**Fix:**
```bash
# 1. Find where aider is installed
which aider
pip show aider-chat

# 2. Uninstall ALL versions
pip uninstall -y aider-chat aider

# 3. Clear Python cache
find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete

# 4. Reinstall
cd /Users/roura.io/Documents/dev.local/flaco/flacoai
pip install -e .

# 5. Run with explicit path
python -m aider
```

### Issue: Import errors

**Cause:** Dependencies not installed

**Fix:**
```bash
cd /Users/roura.io/Documents/dev.local/flaco/flacoai
pip install -r requirements.txt
pip install jira  # If Jira integration fails
```

### Issue: Header not showing, seeing plain text

**Cause:** Rich console might be falling back to simple output

**Check:**
```bash
python -c "from rich.console import Console; c = Console(); c.print('[bold cyan]Test[/bold cyan]')"
```

**If this fails:**
```bash
pip install --upgrade rich
```

### Issue: Commands like /review or /jira not found

**Cause:** Running old cached version

**Fix:**
```bash
# Clear all Python caches
cd /Users/roura.io/Documents/dev.local/flaco
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete

# Reinstall
cd flacoai
pip install -e . --force-reinstall --no-cache-dir
```

---

## 🎯 Expected Behavior Summary

After successful installation, when you run `python -m aider`:

1. **✅ Beautiful Header**: Box-style ASCII art with "FLACO AI"
2. **✅ Personalized Greeting**: "Good [time], [Name]! Welcome back."
3. **✅ Version Info**: "FlacoAI v0.86.1 (Enhanced AI Coding Assistant)"
4. **✅ Activity Summary**: If you've used it before
5. **✅ Random Tip**: One of the FlacoAI-specific tips
6. **✅ New Commands**: `/review` and `/jira` available

---

## 🔍 Debug Mode

To see exactly what's happening:

```bash
# Run with verbose output
python -m aider --verbose

# Or check if modules are imported correctly
python -c "
from aider.branding import FLACO_ASCII_ART, get_welcome_message
from aider.activity_tracker import ActivityTracker
print('✅ Branding module loaded')
print('✅ Activity tracker loaded')
print(FLACO_ASCII_ART)
"
```

---

## 📞 Still Not Working?

If you're still seeing the old interface:

1. **Check installation location:**
   ```bash
   pip show aider-chat
   ```

2. **Verify modified files exist:**
   ```bash
   ls -la /Users/roura.io/Documents/dev.local/flaco/flacoai/aider/branding.py
   ls -la /Users/roura.io/Documents/dev.local/flaco/flacoai/aider/activity_tracker.py
   ```

3. **Test imports directly:**
   ```bash
   cd /Users/roura.io/Documents/dev.local/flaco/flacoai
   python -c "from aider.branding import FLACO_ASCII_ART; print(FLACO_ASCII_ART)"
   ```

4. **Run from source:**
   ```bash
   cd /Users/roura.io/Documents/dev.local/flaco/flacoai
   python -m aider
   ```

---

## 🎉 Success Checklist

- [ ] Ran `./refresh-install.sh` successfully
- [ ] See new FlacoAI ASCII header on startup
- [ ] See personalized greeting with your name
- [ ] `/review` command exists and shows help
- [ ] `/jira` command exists and shows help
- [ ] Version shows "FlacoAI v0.86.1 (Enhanced AI Coding Assistant)"
- [ ] Random tips appear at bottom of startup
- [ ] Activity tracking appears (after multiple sessions)

Once all checkboxes are ✅, you're good to go!

---

**Need more help?** Share the exact output you're seeing and I can help debug.
