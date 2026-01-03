# Flaco AI Maintainer Guide

> **Purpose**: This guide helps new maintainers understand the codebase health, architecture, and common maintenance tasks.
> **Last Updated**: TBD (will be generated during Phase 8)

---

## 📊 State of the Codebase

### Overall Health: 🟡 Good, but needs modernization

**Summary**: Flaco AI is a stable fork of Aider with significant rebrand and iOS-specific features. The core is solid, but some areas need modernization and better documentation.

---

## 🏥 Module Health Assessment

### 🟢 Excellent - Keep As-Is

| Module | Purpose | Why It's Great |
|--------|---------|----------------|
| `flacoai/branding.py` | UI branding and startup messages | Clean, well-structured, easy to customize |
| `flacoai/integrations/jira_client.py` | Jira API integration | Proper error handling, good abstraction |
| `flacoai/waiting.py` | Loading spinner with fun phrases | Fun, well-documented, thread-safe |

**Action**: Just add docstrings and usage examples.

---

### 🟡 Good, But Needs Work

| Module | Purpose | Issues | Effort to Fix |
|--------|---------|--------|---------------|
| `flacoai/mdstream.py` | Markdown streaming renderer | Uses private Rich APIs (`_spans`), fragile | Medium (2-3 days) |
| `flacoai/io.py` | Input/output handling | 1000+ lines, needs splitting | High (5-7 days) |
| `flacoai/coders/base_coder.py` | Base class for all coders | Complex, hard to extend | High (7-10 days) |

**Action**: Create refactoring tickets, modernize incrementally.

**Example Issue**:
```
Title: Refactor io.py - Split into smaller modules
Priority: Medium
Effort: 5-7 days
Description:
- io.py is 1000+ lines and handles too many concerns
- Should split into: InputHandler, OutputRenderer, ConsoleManager
- Would make testing easier and improve maintainability
```

---

### 🔴 Critical - Needs Immediate Attention

| Module | Purpose | Issues | Risk |
|--------|---------|--------|------|
| `flacoai/exceptions.py` | Exception handling | Python 3.14 compatibility hacks | Breaks on Python 3.15+ |
| `flacoai/versioncheck.py` | Check for updates | Silent failures, no retry logic | Users miss updates |

**Action**: Fix in next point release.

**Example Issue**:
```
Title: Fix exceptions.py for Python 3.15+ compatibility
Priority: High
Effort: 1-2 days
Description:
- Current hack filters exceptions using isinstance() and issubclass()
- Will break when litellm updates exception hierarchy
- Should use proper exception registration pattern
```

---

## 🏗️ Architecture Overview

### System Design

```
User Input (CLI)
    ↓
Commands Layer (/generate, /xcode, /review, etc.)
    ↓
Coders Layer (Coder, ReviewCoder, AskCoder, etc.)
    ↓
LLM Integration (litellm wrapper)
    ↓
Model Response
    ↓
Code Changes / Analysis Output
```

### Key Subsystems

1. **Coders** (`flacoai/coders/`)
   - Base abstraction for AI-powered operations
   - Each coder type has specific prompts and behaviors
   - Health: 🟡 Good but complex

2. **Commands** (`flacoai/commands.py`)
   - CLI command dispatch
   - Handles `/generate`, `/xcode`, `/review`, etc.
   - Health: 🟢 Excellent

3. **Integrations** (`flacoai/integrations/`)
   - Jira, GitHub, Figma, TestFlight
   - Each is self-contained
   - Health: 🟢 Excellent

4. **IO System** (`flacoai/io.py`, `flacoai/mdstream.py`)
   - Terminal input/output
   - Markdown streaming
   - Health: 🟡 Needs refactoring

---

## 🛠️ Common Maintenance Tasks

### How to Add a New Command

1. **Define command in `commands.py`**:
```python
def cmd_mycommand(self, args):
    """Add /mycommand description here."""
    # Implementation
    self.io.tool_output("Running mycommand...")
```

2. **Add command metadata**:
```python
# In Commands.__init__()
self.add_command("/mycommand", self.cmd_mycommand,
                 help="Does something awesome")
```

3. **Test**:
```bash
flaco
> /mycommand arg1 arg2
```

**Example PR**: #123 - Add `/screenshot` command

---

### How to Add a New Coder Type

1. **Create new file** in `flacoai/coders/`:
```python
from .ask_coder import AskCoder
from .mytype_prompts import MyTypePrompts

class MyTypeCoder(AskCoder):
    edit_format = "mytype"
    gpt_prompts = MyTypePrompts()
```

2. **Create prompts file** (`mytype_prompts.py`):
```python
from .base_prompts import CoderPrompts

class MyTypePrompts(CoderPrompts):
    main_system = """You are a specialized coder that..."""
```

3. **Register in `__init__.py`**:
```python
from .mytype_coder import MyTypeCoder
```

**Example PR**: #124 - Add ReviewCoder for code review

---

### How to Add a New Integration

1. **Create client** in `flacoai/integrations/`:
```python
class NewServiceClient:
    def __init__(self, api_key):
        self.api_key = api_key

    @classmethod
    def from_config(cls, io=None):
        api_key = os.getenv("NEW_SERVICE_API_KEY")
        if not api_key:
            return None
        return cls(api_key)
```

2. **Add commands** in `commands.py`:
```python
def cmd_newservice(self, args):
    client = NewServiceClient.from_config(self.io)
    if not client:
        self.io.tool_error("NEW_SERVICE_API_KEY not set")
        return
    # Use client
```

**Example PR**: #125 - Add Jira integration

---

### How to Update LLM Prompts

1. **Find the prompt file**:
   - Review: `flacoai/coders/review_prompts.py`
   - Code editing: `flacoai/coders/editblock_prompts.py`
   - Architect mode: `flacoai/coders/architect_prompts.py`

2. **Update `main_system` variable**:
```python
main_system = """Your new prompt here..."""
```

3. **Test** with real project:
```bash
flaco
> /review
# Verify output matches expectations
```

**Best Practice**: Keep prompts in separate files, never hardcode in logic.

---

### How to Add New SwiftUI Templates

1. **Create template** in `flacoai/templates/swiftui/`:
```swift
// login_view.swift.template
import SwiftUI

struct {VIEW_NAME}: View {
    @State private var {STATE_VAR}: String = ""

    var body: some View {
        VStack {
            // Template content
        }
    }
}
```

2. **Register template** in template engine:
```python
TEMPLATES = {
    "login": "templates/swiftui/login_view.swift.template",
    "settings": "templates/swiftui/settings_view.swift.template",
}
```

3. **Add generation logic**:
```python
def generate_view(template_name, view_name, **kwargs):
    template = load_template(template_name)
    return template.format(VIEW_NAME=view_name, **kwargs)
```

---

## 🧪 Testing Strategy

### What's Tested

- ✅ Unit tests for utilities (`flacoai/utils.py`)
- ✅ Integration tests for coders
- ✅ Basic CLI command tests

### What Needs Tests

- ❌ Markdown streaming (`mdstream.py`)
- ❌ Exception handling (`exceptions.py`)
- ❌ Jira integration (mocked tests needed)
- ❌ SwiftUI template generation
- ❌ Xcode project manipulation

### How to Run Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/basic/test_coder.py

# Run with coverage
pytest --cov=flacoai tests/
```

### How to Add New Tests

1. **Create test file** in `tests/`:
```python
import pytest
from flacoai.mymodule import MyClass

def test_myfunction():
    result = MyClass().myfunction()
    assert result == expected
```

2. **Run test**:
```bash
pytest tests/test_mymodule.py -v
```

---

## 🚀 Release Process

### Version Numbering

- **Major** (x.0.0): Breaking changes, major new features
- **Minor** (1.x.0): New features, non-breaking changes
- **Patch** (1.0.x): Bug fixes only

### How to Cut a Release

1. **Update version** in `flacoai/__init__.py`:
```python
__version__ = "2.0.0"
```

2. **Update CHANGELOG.md**:
```markdown
## v2.0.0 (2026-01-15)

### Added
- SwiftUI code generation
- Xcode project manipulation
...
```

3. **Commit and tag**:
```bash
git add -A
git commit -m "chore: Bump version to 2.0.0"
git tag v2.0.0
git push origin main --tags
```

4. **Create GitHub release**:
```bash
gh release create v2.0.0 --notes "$(cat RELEASE_NOTES.md)"
```

---

## 📝 Known Technical Debt

### High Priority

1. **Refactor io.py** (Effort: 5-7 days)
   - Split into InputHandler, OutputRenderer, ConsoleManager
   - Improve testability

2. **Fix Python 3.15+ compatibility** (Effort: 1-2 days)
   - Update exceptions.py to use proper exception registration
   - Remove isinstance() hacks

3. **Add comprehensive error handling** (Effort: 3-5 days)
   - Many functions fail silently
   - Need better error messages and recovery

### Medium Priority

4. **Modernize mdstream.py** (Effort: 2-3 days)
   - Stop using Rich private APIs
   - Implement proper streaming abstraction

5. **Add retry logic to integrations** (Effort: 2-3 days)
   - Jira, GitHub, Figma calls can fail transiently
   - Need exponential backoff

### Low Priority

6. **Performance optimization** (Effort: 5-7 days)
   - Profile large file parsing
   - Optimize repo map generation
   - Cache expensive operations

---

## 🎯 Future Improvements

### v2.1.0 Ideas

- [ ] Voice input support
- [ ] Multi-language support (beyond Swift)
- [ ] AI-powered test generation
- [ ] Code smell detection

### v3.0.0 Vision

- [ ] Plugin system for custom coders
- [ ] Web UI in addition to CLI
- [ ] Team collaboration features
- [ ] Cloud sync for templates

---

## 📞 Getting Help

- **GitHub Issues**: https://github.com/RouraIO/flaco.cli/issues
- **Discussions**: https://github.com/RouraIO/flaco.cli/discussions
- **Email**: support@flaco.ai (TBD)

---

## 🙏 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution guidelines.

This guide will be automatically updated as the codebase evolves.

**Last Generated**: [DATE] by Flaco AI Documentation System v2.0.0
