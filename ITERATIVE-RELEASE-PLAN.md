# Flaco AI Iterative Release Plan: v1.0.0 → v2.0.0

> **Philosophy**: Ship working software incrementally. Each minor version is production-ready with real value.

**Total Journey**: ~9-10 weeks from v1.0.0 to v2.0.0
**Strategy**: 10 minor releases, each building on the previous stable foundation

---

## 📋 Version Overview

| Version | Focus | Duration | Cumulative | Status |
|---------|-------|----------|------------|--------|
| **v1.0.0** | Stable foundation (current) | - | - | ✅ Complete |
| **v1.1.0** | Header polish + foundation fixes | 2-3 days | 3 days | 🔜 Next |
| **v1.2.0** | SwiftUI Code Generation | 3-5 days | 8 days | ⏳ Planned |
| **v1.3.0** | Xcode Project Manipulation | 4-6 days | 14 days | ⏳ Planned |
| **v1.4.0** | Screenshot-to-Code | 5-7 days | 21 days | ⏳ Planned |
| **v1.5.0** | iOS Branding & Polish | 2-3 days | 24 days | ⏳ Planned |
| **v1.6.0** | Advanced PR-Style Review System | 5-7 days | 31 days | ⏳ Planned |
| **v1.7.0** | iOS-Specific Features | 6-8 days | 39 days | ⏳ Planned |
| **v1.8.0** | Advanced Integrations | 7-10 days | 49 days | ⏳ Planned |
| **v1.9.0** | Project-Wide Documentation | 6-8 days | 57 days | ⏳ Planned |
| **v2.0.0** | Comprehensive Testing + Launch | 5-7 days | **~64 days** | 🎯 Goal |

---

## 🎯 v1.1.0 - Header Polish + Foundation Fixes

**Release Date**: ~3 days
**Goal**: Perfect the v1.0.0 foundation and improve UX

### Tickets

#### FLA-101: Improve startup header layout
- ✅ Strip "openai/" prefix from model names
- ✅ Move working directory info into header after tip
- ✅ Add yellow triangle (⚠️) to directory note
- ✅ Show both current and git working directory

**Acceptance Criteria**:
- Model shows as "qwen2.5-coder:32b" not "openai/qwen2.5-coder:32b"
- Directory note appears inside header, below tip
- Git directory shown if different from current directory

**Files Changed**:
- `flacoai/branding.py`: Update `format_compact_header()`, add `format_directory_note()`
- `flacoai/coders/base_coder.py`: Update `get_announcements()`

---

#### FLA-102: Test v1.0.0 stability thoroughly
- [ ] Test inline code rendering (no white background)
- [ ] Test streaming response (smooth, no flickering)
- [ ] Test cyan color theme (#00FFFF)
- [ ] Test with real iOS project (ChirpChirp)
- [ ] Test loading phrases (68 variations)
- [ ] Test Python 3.14+ compatibility

**Acceptance Criteria**:
- Zero crashes in 2-3 days of heavy use
- All v1.0.0 features work correctly
- Ready to build v1.2.0 on top

**Exit Criteria**: v1.1.0 is rock-solid for 2-3 days before starting v1.2.0

---

## 🧱 v1.2.0 - SwiftUI Code Generation

**Release Date**: ~5 days after v1.1.0
**Goal**: First iOS-specific feature

### Tickets

#### FLA-201: Implement /generate command system
- [ ] Create command parser and dispatcher
- [ ] Add `/generate view <ViewName>` syntax
- [ ] Add `/generate list <ItemType>` for list views
- [ ] Add help text and documentation
- [ ] Implement error handling for invalid requests

**Acceptance Criteria**:
- `/generate view Login` creates SwiftUI login view
- `/help generate` shows command syntax
- Errors are user-friendly (e.g., "Invalid view type")

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_generate()`
- `flacoai/coders/generate_coder.py`: New coder for generation

---

#### FLA-202: Build SwiftUI template library
- [ ] Create `flacoai/templates/swiftui/` directory
- [ ] Add `login_view.swift.template`
- [ ] Add `settings_view.swift.template`
- [ ] Add `list_view.swift.template`
- [ ] Add `detail_view.swift.template`
- [ ] Add `tabview.swift.template`
- [ ] Implement template variable substitution (e.g., `{VIEW_NAME}`, `{ITEM_TYPE}`)

**Acceptance Criteria**:
- 5 working templates
- Variables are properly replaced
- Generated code compiles in Xcode

**Files Changed**:
- `flacoai/templates/swiftui/*.swift.template`: New template files
- `flacoai/template_engine.py`: New template loader

---

#### FLA-203: Implement template generation logic
- [ ] Parse user request (e.g., "Login with email/password")
- [ ] Select appropriate template based on keywords
- [ ] Extract parameters from request
- [ ] Customize template with user parameters
- [ ] Generate clean SwiftUI code
- [ ] Save to file or display in chat

**Acceptance Criteria**:
- `/generate view Login with email and password` produces valid SwiftUI
- Code includes email/password fields
- Works with all 5 templates

**Files Changed**:
- `flacoai/coders/generate_coder.py`: Generation logic

**Exit Criteria**: `/generate` works reliably with 5 template types

---

## 🔧 v1.3.0 - Xcode Project Manipulation

**Release Date**: ~6 days after v1.2.0
**Goal**: Manage Xcode projects without leaving CLI

### Tickets

#### FLA-301: Implement /xcode command system
- [ ] Add `/xcode add-file <path>` subcommand
- [ ] Add `/xcode remove-file <path>` subcommand
- [ ] Add `/xcode create-target <name>` subcommand
- [ ] Add `/xcode list-targets` subcommand
- [ ] Add help text for all subcommands

**Acceptance Criteria**:
- `/xcode add-file NewView.swift` adds file to project
- `/xcode list-targets` shows all targets
- Errors are descriptive (e.g., "File already exists in project")

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_xcode()`
- `flacoai/xcode/xcode_manager.py`: New Xcode integration

---

#### FLA-302: Build Xcode project parser and modifier
- [ ] Install/integrate `pbxproj` library (or `mod-pbxproj`)
- [ ] Implement `.xcodeproj` parser
- [ ] Implement file addition logic (update PBXBuildFile, PBXFileReference, etc.)
- [ ] Implement file removal logic
- [ ] Implement target creation logic
- [ ] Preserve project structure and formatting

**Acceptance Criteria**:
- Add file to project → Xcode opens without errors
- Remove file → File disappears from project navigator
- Project structure is preserved (no corruption)

**Files Changed**:
- `requirements.txt`: Add `mod-pbxproj`
- `flacoai/xcode/pbxproj_wrapper.py`: New wrapper around pbxproj

---

#### FLA-303: Test with real Xcode projects
- [ ] Test with single-target project
- [ ] Test with multi-target project (app + tests)
- [ ] Test with SwiftUI project
- [ ] Test with UIKit project
- [ ] Verify Xcode can open modified projects

**Acceptance Criteria**:
- All 4 project types work
- Xcode shows no warnings after modification

**Exit Criteria**: `/xcode` reliably modifies Xcode projects without corruption

---

## 📸 v1.4.0 - Screenshot-to-Code

**Release Date**: ~7 days after v1.3.0
**Goal**: Convert UI mockups to SwiftUI code

### Tickets

#### FLA-401: Implement /screenshot command
- [ ] Add `/screenshot <image_path>` command
- [ ] Support PNG, JPG, PDF formats
- [ ] Support multiple images (e.g., `/screenshot design1.png design2.png`)
- [ ] Add `--preview` mode to show analysis without code generation

**Acceptance Criteria**:
- `/screenshot mockup.png` analyzes image
- Supports common image formats
- Preview mode shows detected UI elements

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_screenshot()`
- `flacoai/coders/screenshot_coder.py`: New coder for vision analysis

---

#### FLA-402: Integrate vision model
- [ ] Configure vision model (GPT-4V or Claude with vision)
- [ ] Send image to model with analysis prompt
- [ ] Parse UI elements from response (buttons, text fields, labels, etc.)
- [ ] Handle multi-image analysis (compare designs)

**Acceptance Criteria**:
- Vision model correctly identifies UI elements
- Text content is extracted accurately
- Layout structure is understood

**Files Changed**:
- `flacoai/coders/screenshot_coder.py`: Vision integration
- `flacoai/prompts/screenshot_prompts.py`: Vision analysis prompts

---

#### FLA-403: Generate SwiftUI from screenshot analysis
- [ ] Map UI elements to SwiftUI components (Text, Button, TextField, etc.)
- [ ] Generate layout code (VStack, HStack, ZStack)
- [ ] Generate styling (colors, fonts, spacing)
- [ ] Add placeholder text and images
- [ ] Combine with existing templates when applicable

**Acceptance Criteria**:
- Generated code visually resembles input image
- Code compiles in Xcode
- Layout is responsive

**Files Changed**:
- `flacoai/coders/screenshot_coder.py`: Code generation logic

**Exit Criteria**: `/screenshot` generates compilable SwiftUI that resembles input

---

## 🎨 v1.5.0 - iOS Branding & Polish

**Release Date**: ~3 days after v1.4.0
**Goal**: Make it feel like an iOS development tool

### Tickets

#### FLA-501: Update ASCII art banner
- [ ] Design iOS-themed ASCII art (Swift logo inspiration?)
- [ ] Use blue/cyan color scheme
- [ ] Keep professional, modern look
- [ ] Ensure it fits in 80-column terminal

**Acceptance Criteria**:
- Banner is visually distinct from Aider
- Clearly iOS-focused
- Works in both light and dark terminals

**Files Changed**:
- `flacoai/branding.py`: Update `get_flaco_ascii_art()`

---

#### FLA-502: Update startup messages
- [ ] Update tagline to "The Ultimate iOS Development Platform"
- [ ] Add iOS-specific tips to startup carousel
- [ ] Use Apple-style messaging (simple, clear)
- [ ] Update all copy to be iOS-focused

**Acceptance Criteria**:
- All tips are iOS-relevant
- Messaging is professional and clear
- No generic "code assistant" language

**Files Changed**:
- `flacoai/branding.py`: Update `STARTUP_TIPS`

---

#### FLA-503: Update documentation for iOS focus
- [ ] Update README.md to focus on iOS development
- [ ] Add iOS-specific examples (SwiftUI, Xcode)
- [ ] Add screenshot showcase
- [ ] Update installation instructions

**Acceptance Criteria**:
- README clearly positions Flaco AI as iOS tool
- Screenshots show iOS development workflow

**Files Changed**:
- `README.md`: Complete rewrite for iOS focus

**Exit Criteria**: Flaco AI looks and feels like it was built specifically for iOS developers

---

## 🧠 v1.6.0 - Advanced PR-Style Review System

**Release Date**: ~7 days after v1.5.0
**Goal**: Best-in-class code review experience

### Tickets

#### FLA-601: Replace review_prompts.py with advanced system
- [ ] Create new comprehensive system prompt
- [ ] Add PR-style review instructions
- [ ] Define staff-level reviewer persona
- [ ] Add iOS-specific review guidelines

**Acceptance Criteria**:
- New prompt produces structured reviews
- Reviews are thorough and insightful
- Tone is professional and constructive

**Files Changed**:
- `flacoai/coders/review_prompts.py`: Complete rewrite

---

#### FLA-602: Implement structured review output sections
- [ ] Executive Summary section
- [ ] "What's Working Well (Do NOT Change)" section
- [ ] High-Impact Improvements (priority ordered with risk)
- [ ] Medium/Optional Improvements section
- [ ] "Things NOT Worth Changing" section
- [ ] Architectural & Product Questions section
- [ ] Suggested Follow-Up Reviews section

**Acceptance Criteria**:
- All 7 sections appear in every review
- Sections are clearly labeled
- Content is well-organized

**Files Changed**:
- `flacoai/coders/review_coder.py`: Review output formatter

---

#### FLA-603: Add review mode selection
- [ ] Add `--mode pr` for full PR review
- [ ] Add `--mode arch` for architecture focus
- [ ] Add `--mode perf` for performance focus
- [ ] Add `--mode minimal` for quick check

**Acceptance Criteria**:
- Each mode produces appropriate review depth
- Mode selection is documented

**Files Changed**:
- `flacoai/commands.py`: Add mode flag to `/review`

---

#### FLA-604: Implement Jira Ticket Intelligence
- [ ] Detect Jira ticket references (PROJ-123 format)
- [ ] Fetch ticket details from Jira API
- [ ] Find related PRs via ticket links
- [ ] Find related commits via commit messages
- [ ] Review code in context of ticket requirements
- [ ] Validate implementation matches acceptance criteria
- [ ] Flag missing requirements from ticket

**Acceptance Criteria**:
- `/review PROJ-123` fetches ticket and reviews against it
- Related PRs and commits are analyzed
- Missing requirements are flagged

**Files Changed**:
- `flacoai/integrations/jira_client.py`: Enhance Jira integration
- `flacoai/coders/review_coder.py`: Add ticket intelligence

**Exit Criteria**: `/review` produces comprehensive, staff-level PR reviews with Jira context

---

## 🍎 v1.7.0 - iOS-Specific Features

**Release Date**: ~8 days after v1.6.0
**Goal**: Features that make Flaco AI irreplaceable for iOS devs

### Tickets

#### FLA-701: SF Symbols integration
- [ ] Add `/symbols search <keyword>` command
- [ ] Fetch SF Symbols catalog (or use local cache)
- [ ] Browse symbols by category
- [ ] Insert SF Symbol code snippets

**Acceptance Criteria**:
- `/symbols search mail` shows mail-related symbols
- Code snippets are ready to paste into SwiftUI

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_symbols()`
- `flacoai/integrations/sf_symbols.py`: New SF Symbols integration

---

#### FLA-702: Apple HIG validation
- [ ] Check for HIG compliance (button sizes, spacing, colors)
- [ ] Warn about violations (e.g., button too small)
- [ ] Suggest HIG-compliant alternatives
- [ ] Add `/hig check` command

**Acceptance Criteria**:
- `/hig check` scans SwiftUI views for violations
- Warnings are actionable (e.g., "Button height should be at least 44pt")

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_hig()`
- `flacoai/hig/validator.py`: New HIG validator

---

#### FLA-703: iOS security scanning
- [ ] Check keychain usage patterns
- [ ] Validate data protection settings
- [ ] Check network security (ATS compliance)
- [ ] Validate privacy manifest
- [ ] Add `/security scan` command

**Acceptance Criteria**:
- `/security scan` identifies security issues
- Reports are actionable with fix suggestions

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_security()`
- `flacoai/security/scanner.py`: New security scanner

**Exit Criteria**: iOS-specific features provide real value and catch actual issues

---

## 🚢 v1.8.0 - Advanced Integrations

**Release Date**: ~10 days after v1.7.0
**Goal**: Connect to design and deployment workflows

### Tickets

#### FLA-801: Figma-to-SwiftUI converter
- [ ] Add `/figma import <url>` command
- [ ] Authenticate with Figma API
- [ ] Parse Figma API response (components, frames, styles)
- [ ] Convert Figma components to SwiftUI
- [ ] Handle layouts (Auto Layout → SwiftUI layout)
- [ ] Convert styling (colors, fonts, spacing)

**Acceptance Criteria**:
- `/figma import https://figma.com/file/...` generates SwiftUI
- Layout resembles Figma design
- Code compiles in Xcode

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_figma()`
- `flacoai/integrations/figma_client.py`: New Figma integration
- `requirements.txt`: Add Figma API client

---

#### FLA-802: TestFlight integration
- [ ] Add `/testflight upload` command
- [ ] Build and archive app using `xcodebuild`
- [ ] Upload to App Store Connect using `altool` or `notarytool`
- [ ] Notify testers
- [ ] Show upload progress

**Acceptance Criteria**:
- `/testflight upload` builds and uploads app
- Progress is shown in terminal
- Testers receive notification

**Files Changed**:
- `flacoai/commands.py`: Add `cmd_testflight()`
- `flacoai/integrations/testflight.py`: New TestFlight integration

**Exit Criteria**: Design-to-code-to-TestFlight workflow works smoothly

---

## 📚 v1.9.0 - Project-Wide Documentation

**Release Date**: ~8 days after v1.8.0
**Goal**: Document everything for current users AND future maintainers

### Tickets

#### FLA-901: Add inline code documentation
- [ ] Add docstrings to all public functions/classes
- [ ] Document complex algorithms and logic
- [ ] Add type hints throughout codebase
- [ ] Document environment variables and config options
- [ ] Add usage examples in docstrings

**Acceptance Criteria**:
- 80%+ of code has docstrings
- All public APIs documented
- Type hints added to all functions

**Files Changed**:
- All `.py` files in `flacoai/`

---

#### FLA-902: Create architecture documentation
- [ ] Create ARCHITECTURE.md (system design overview)
- [ ] Document module structure and dependencies
- [ ] Explain data flow (user input → LLM → code changes)
- [ ] Document plugin/extension system
- [ ] Diagram key subsystems (coders, commands, integrations)

**Acceptance Criteria**:
- ARCHITECTURE.md explains entire system
- Diagrams are clear and accurate

**Files Changed**:
- `ARCHITECTURE.md`: New file

---

#### FLA-903: Create maintainer onboarding guide
- [ ] Generate MAINTAINER_GUIDE.md from template
- [ ] Add "State of the Codebase" assessment
- [ ] Document module-by-module breakdown with health ratings (🟢🟡🔴)
- [ ] Add common maintenance tasks (how to add command, coder, integration, etc.)
- [ ] Document testing strategy
- [ ] Document release process

**Acceptance Criteria**:
- New developer can read guide and understand codebase in 2-3 hours
- All known issues are documented

**Files Changed**:
- `MAINTAINER_GUIDE.md`: Generated from template

---

#### FLA-904: Auto-generate GitHub issues for technical debt
- [ ] Scan codebase for TODOs, FIXMEs, HACKs
- [ ] Identify modules needing refactoring (using template)
- [ ] Generate GitHub issues with effort estimates and priority
- [ ] Tag issues appropriately
- [ ] Link to relevant code sections

**Acceptance Criteria**:
- GitHub issues board has complete technical debt backlog
- Issues are well-tagged and prioritized

**Files Changed**:
- `scripts/generate_tech_debt_issues.py`: New script

---

#### FLA-905: Create comprehensive user documentation
- [ ] Write command reference (all `/` commands)
- [ ] Write iOS-specific workflow guides
- [ ] Create troubleshooting guide
- [ ] Add FAQ section

**Acceptance Criteria**:
- All commands are documented
- Common workflows have step-by-step guides

**Files Changed**:
- `docs/COMMAND_REFERENCE.md`: New file
- `docs/TROUBLESHOOTING.md`: New file
- `docs/FAQ.md`: New file

**Exit Criteria**: Documentation is comprehensive for both users and maintainers

---

## 🧪 v2.0.0 - Comprehensive Testing + Launch

**Release Date**: ~7 days after v1.9.0
**Goal**: Rock-solid stability, production-ready

### Tickets

#### FLA-1001: Write comprehensive unit tests
- [ ] SwiftUI template generation tests
- [ ] Xcode project manipulation tests
- [ ] Screenshot parsing tests
- [ ] Jira integration tests (mocked)
- [ ] Review output structure tests
- [ ] 80%+ code coverage target

**Acceptance Criteria**:
- All tests pass
- Coverage report shows 80%+ coverage

**Files Changed**:
- `tests/`: New test files

---

#### FLA-1002: Write integration tests
- [ ] End-to-end `/generate` workflow test
- [ ] End-to-end `/xcode` workflow test
- [ ] End-to-end `/screenshot` workflow test
- [ ] End-to-end `/review` with Jira ticket test
- [ ] Jira → GitHub → Code review flow test

**Acceptance Criteria**:
- All integration tests pass
- Tests cover real-world workflows

**Files Changed**:
- `tests/integration/`: New integration tests

---

#### FLA-1003: Real-world testing
- [ ] Test with small iOS project (1-5 files)
- [ ] Test with medium iOS project (10-20 files)
- [ ] Test with large iOS project (50+ files)
- [ ] Test with SwiftUI + UIKit mixed project
- [ ] Test with multi-target Xcode project

**Acceptance Criteria**:
- All project sizes work correctly
- No crashes or errors

---

#### FLA-1004: Performance testing
- [ ] Large file parsing performance (10,000+ lines)
- [ ] Multiple concurrent operations
- [ ] Memory usage under load
- [ ] Streaming response speed

**Acceptance Criteria**:
- Performance benchmarks meet targets
- No memory leaks

---

#### FLA-1005: Compatibility testing
- [ ] Python 3.14+ compatibility
- [ ] macOS Sonoma/Sequoia compatibility
- [ ] Xcode 15/16 compatibility
- [ ] Different terminal emulators (iTerm2, Terminal.app, VS Code)

**Acceptance Criteria**:
- Works on all supported platforms

---

#### FLA-1006: Edge case testing
- [ ] Malformed Jira ticket references
- [ ] Missing Xcode project files
- [ ] Invalid screenshot formats
- [ ] Network failures (Jira/GitHub API)
- [ ] Corrupted template files

**Acceptance Criteria**:
- Graceful error handling for all edge cases

---

#### FLA-1007: Final polish and release
- [ ] Update README.md with v2.0.0 features
- [ ] Add feature showcase with screenshots
- [ ] Update CHANGELOG.md with all v2.0.0 changes
- [ ] Write v2.0.0 release notes
- [ ] Create comparison table (Aider vs Flaco AI)
- [ ] Update GitHub repo description
- [ ] Tag v2.0.0 in git
- [ ] Create GitHub release

**Acceptance Criteria**:
- Documentation is complete and accurate
- Release notes are comprehensive

---

#### FLA-1008: External validation
- [ ] Get external beta tester feedback (at least 3 users)
- [ ] Run full test suite one final time
- [ ] Verify all documentation is accurate
- [ ] Test installation from clean state

**Acceptance Criteria**:
- Beta testers report positive experience
- Zero critical bugs

**Exit Criteria**: Flaco AI v2.0.0 is ready to announce as "The iOS Development Platform"

---

## 🎯 Success Metrics for v2.0.0

By launch, Flaco AI should have:

✅ **Differentiation**
- 10+ features Aider doesn't have
- Clearly positioned as "The iOS Development Platform"
- Visual branding that screams "iOS"

✅ **Quality**
- Zero crashes in 1 week of heavy use
- 80%+ test coverage
- All features work with real iOS projects
- Documentation is comprehensive

✅ **Adoption**
- At least 10 GitHub stars
- At least 3 external users providing feedback
- Positive sentiment in iOS dev communities

---

## 📝 How to Use This Plan

### For Each Release:

1. **Start with v1.1.0** (current next step)
2. **Complete all tickets** for that version
3. **Test thoroughly** before moving to next version
4. **Ship the release** to GitHub with tag and release notes
5. **Use it in production** for 1-2 days to validate stability
6. **Fix critical bugs** if any (patch release)
7. **Move to next version** only when current is stable

### Ticket Management:

- Create GitHub issues for each ticket (FLA-XXX)
- Tag with version milestone (e.g., `v1.2.0`)
- Assign effort estimates (S/M/L/XL)
- Track progress on GitHub Projects board

### Flexibility:

- **Can reorder phases** based on what's most valuable
- **Can reduce scope** if a phase takes longer than estimated
- **Can skip features** that aren't critical for v2.0.0
- **Must maintain quality** - never ship broken features

---

## 🚀 Next Action

**Immediate**: Ship v1.1.0 with header improvements (FLA-101 ✅ complete)

**Then**: Test v1.0.0/v1.1.0 stability for 2-3 days (FLA-102)

**After**: Begin v1.2.0 SwiftUI Code Generation (FLA-201)

---

**Current Status**: 🟢 v1.1.0 FLA-101 complete, ready to test and ship
