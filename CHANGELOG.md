# Changelog

All notable changes to Flaco AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.0] - 2026-01-02

### 🎨 UI/UX Modernization

This release focuses on making Flaco AI more modern, engaging, and visually appealing while maintaining all the stability of v1.5.0.

### Added
- **Fun Loading Animations**: Randomized loading phrases instead of static "Waiting for [model]" text
  - 18 different phrases including "Thinking...", "Pondering...", "Hubbub-a-looing...", "Channeling the AI spirits...", etc.
  - Makes interactions more engaging and lighthearted
  - Different phrase shown on each interaction
- **Compact Header Design**: Completely redesigned startup header inspired by Claude Code
  - All key information on one line: version, model, directory, branch, file count
  - Much more information-dense and modern
  - Removed verbose multi-line formatting
  - Kept the beloved ASCII logo

### Changed
- **Assistant Output Color**: Changed from dark blue (#0088ff) to cyan (#00FFFF)
  - Better readability across all terminal themes
  - Consistent across both light and dark modes
  - More modern, professional appearance
- **Header Layout**: Streamlined from ~15 lines to ~3 lines while showing same information
- **Warning Messages**: Simplified with emoji prefixes (⚠️) for better visual scanning

### Technical
- Updated `flacoai/waiting.py` with THINKING_PHRASES list and random selection
- Updated `flacoai/args.py`, `flacoai/main.py`, `flacoai/io.py` with new cyan color defaults
- Added `format_compact_header()` function in `flacoai/branding.py`
- Redesigned `get_announcements()` method in `flacoai/coders/base_coder.py`

## [1.5.0] - 2026-01-02

### 🎉 First Stable Release

This marks the first truly stable production release of Flaco AI with complete branding consistency and unified configuration.

### Changed
- **BREAKING**: Environment variable prefix changed from `aider_` to `flaco_` for consistency
  - `aider_DOCKER_IMAGE` → `flaco_DOCKER_IMAGE`
  - `aider_ANALYTICS` → `flaco_ANALYTICS`
  - `aider_DARK_MODE` → `flaco_DARK_MODE`
  - `aider_SHOW_DIFFS` → `flaco_SHOW_DIFFS`
  - `aider_CHECK_UPDATE` → `flaco_CHECK_UPDATE`
  - `aider_CACHE_KEEPALIVE_DELAY` → `flaco_CACHE_KEEPALIVE_DELAY`
  - `aider_SANITY_CHECK_TURNS` → `flaco_SANITY_CHECK_TURNS`
  - `aider_BENCHMARK_DIR` → `flaco_BENCHMARK_DIR`
  - `aider_DOCKER` → `flaco_DOCKER`

### Fixed
- Unified version numbering across all files to 1.5.0
- Updated GitHub repository URLs from `flacoai-AI/flacoai` to `RouraIO/flaco.cli`
- Synchronized version in installer, launcher scripts, and core modules
- Updated all test fixtures to use new `flaco_` environment variable prefix

### Documentation
- Updated CONTRIBUTING.md with correct repository URLs
- Updated README.md with current GitHub organization
- Improved consistency across all documentation files

### Technical
- Complete environment variable namespace migration for better branding
- Version consistency enforcement across installation and runtime scripts
- Enhanced test suite with updated environment variable references

## [1.3.0] - 2026-01-01

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
