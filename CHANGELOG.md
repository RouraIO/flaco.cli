# Changelog

All notable changes to Flaco AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
