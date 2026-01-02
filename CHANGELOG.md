# Changelog

All notable changes to Flaco AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
