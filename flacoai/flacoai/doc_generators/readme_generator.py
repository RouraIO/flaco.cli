"""README.md generator for iOS projects."""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional


class ReadmeGenerator:
    """Generates comprehensive README.md files for iOS projects."""

    def __init__(self, project_dir: str, io=None):
        """Initialize README generator.

        Args:
            project_dir: Path to project directory
            io: IO object for output
        """
        self.project_dir = Path(project_dir)
        self.io = io
        self.project_info = {}

    def generate(self) -> str:
        """Generate README content.

        Returns:
            Markdown formatted README content
        """
        self._analyze_project()

        sections = []

        # Header
        sections.append(self._generate_header())

        # Description
        sections.append(self._generate_description())

        # Features
        if self.project_info.get('features'):
            sections.append(self._generate_features())

        # Screenshots
        sections.append(self._generate_screenshots_placeholder())

        # Requirements
        sections.append(self._generate_requirements())

        # Installation
        sections.append(self._generate_installation())

        # Usage
        sections.append(self._generate_usage())

        # Architecture
        if self.project_info.get('architecture'):
            sections.append(self._generate_architecture())

        # Dependencies
        if self.project_info.get('dependencies'):
            sections.append(self._generate_dependencies())

        # Contributing
        sections.append(self._generate_contributing())

        # License
        sections.append(self._generate_license())

        return '\n\n'.join(sections)

    def _analyze_project(self):
        """Analyze project structure to gather information."""
        self.project_info = {
            'name': self.project_dir.name,
            'has_cocoapods': (self.project_dir / 'Podfile').exists(),
            'has_spm': (self.project_dir / 'Package.swift').exists(),
            'has_carthage': (self.project_dir / 'Cartfile').exists(),
            'swift_version': self._detect_swift_version(),
            'ios_version': self._detect_ios_version(),
            'dependencies': self._detect_dependencies(),
            'features': self._detect_features(),
            'architecture': self._detect_architecture(),
        }

    def _detect_swift_version(self) -> Optional[str]:
        """Detect Swift version from project."""
        # Check .swift-version file
        swift_version_file = self.project_dir / '.swift-version'
        if swift_version_file.exists():
            return swift_version_file.read_text().strip()

        # Check Package.swift
        package_swift = self.project_dir / 'Package.swift'
        if package_swift.exists():
            content = package_swift.read_text()
            match = re.search(r'swift-tools-version:\s*(\d+\.\d+)', content)
            if match:
                return match.group(1)

        return '5.9'  # Default

    def _detect_ios_version(self) -> str:
        """Detect minimum iOS version."""
        # Check Podfile
        podfile = self.project_dir / 'Podfile'
        if podfile.exists():
            content = podfile.read_text()
            match = re.search(r"platform\s+:ios,\s*['\"]([^'\"]+)['\"]", content)
            if match:
                return match.group(1)

        # Check Package.swift
        package_swift = self.project_dir / 'Package.swift'
        if package_swift.exists():
            content = package_swift.read_text()
            match = re.search(r'\.iOS\(\.v(\d+)\)', content)
            if match:
                return match.group(1) + '.0'

        return '15.0'  # Default

    def _detect_dependencies(self) -> List[str]:
        """Detect project dependencies."""
        deps = []

        # CocoaPods
        podfile = self.project_dir / 'Podfile'
        if podfile.exists():
            content = podfile.read_text()
            pod_matches = re.findall(r"pod\s+['\"]([^'\"]+)['\"]", content)
            deps.extend(pod_matches)

        # SPM
        package_swift = self.project_dir / 'Package.swift'
        if package_swift.exists():
            content = package_swift.read_text()
            url_matches = re.findall(r'url:\s*"https://github\.com/([^"]+)"', content)
            deps.extend([url.split('/')[-1].replace('.git', '') for url in url_matches])

        return list(set(deps))[:10]  # Limit to 10

    def _detect_features(self) -> List[str]:
        """Detect key features from code."""
        features = []

        # Search for common iOS features
        feature_patterns = {
            'SwiftUI': r'import SwiftUI',
            'CoreData': r'import CoreData',
            'CloudKit': r'import CloudKit',
            'HealthKit': r'import HealthKit',
            'MapKit': r'import MapKit',
            'AVFoundation': r'import AVFoundation',
            'Vision': r'import Vision',
            'ARKit': r'import ARKit',
            'CoreML': r'import CoreML',
            'Combine': r'import Combine',
        }

        for swift_file in self.project_dir.rglob('*.swift'):
            try:
                content = swift_file.read_text()
                for feature, pattern in feature_patterns.items():
                    if re.search(pattern, content) and feature not in features:
                        features.append(feature)
            except Exception:
                continue

        return features[:10]  # Limit to 10

    def _detect_architecture(self) -> Optional[str]:
        """Detect architecture pattern."""
        patterns = {
            'MVVM': ['ViewModel', 'viewModel'],
            'MVC': ['ViewController'],
            'VIPER': ['Interactor', 'Presenter', 'Router'],
            'Clean Architecture': ['UseCase', 'Repository'],
        }

        found_patterns = {}

        for swift_file in self.project_dir.rglob('*.swift'):
            try:
                content = swift_file.read_text()
                for arch, keywords in patterns.items():
                    count = sum(1 for keyword in keywords if keyword in content)
                    found_patterns[arch] = found_patterns.get(arch, 0) + count
            except Exception:
                continue

        if found_patterns:
            return max(found_patterns, key=found_patterns.get)

        return None

    def _generate_header(self) -> str:
        """Generate README header."""
        project_name = self.project_info['name']

        return f"""# {project_name}

![Swift](https://img.shields.io/badge/Swift-{self.project_info['swift_version']}-orange.svg)
![iOS](https://img.shields.io/badge/iOS-{self.project_info['ios_version']}+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> A beautiful iOS app built with Swift and SwiftUI"""

    def _generate_description(self) -> str:
        """Generate description section."""
        return """## 📱 Description

[Add a brief description of your app here. What problem does it solve? Who is it for?]

### Key Highlights

- ✨ Modern Swift and SwiftUI architecture
- 🎨 Beautiful, intuitive user interface
- 🚀 Fast and responsive
- 🔒 Secure and privacy-focused"""

    def _generate_features(self) -> str:
        """Generate features section."""
        features_list = '\n'.join([f'- {feature} integration' for feature in self.project_info['features']])

        return f"""## ✨ Features

{features_list if features_list else '- [List your app features here]'}
- Clean, modern UI design
- Offline support
- Dark mode support
- Accessibility features"""

    def _generate_screenshots_placeholder(self) -> str:
        """Generate screenshots section placeholder."""
        return """## 📸 Screenshots

| Home | Details | Settings |
|------|---------|----------|
| ![Home](screenshots/home.png) | ![Details](screenshots/details.png) | ![Settings](screenshots/settings.png) |

*Add your app screenshots to the `screenshots/` directory*"""

    def _generate_requirements(self) -> str:
        """Generate requirements section."""
        return f"""## 🛠 Requirements

- iOS {self.project_info['ios_version']}+
- Xcode 15.0+
- Swift {self.project_info['swift_version']}+"""

    def _generate_installation(self) -> str:
        """Generate installation section."""
        sections = []

        sections.append("""## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/{}.git
cd {}
```""".format(self.project_info['name'], self.project_info['name']))

        if self.project_info['has_cocoapods']:
            sections.append("""### Install Dependencies (CocoaPods)

```bash
pod install
open {}.xcworkspace
```""".format(self.project_info['name']))

        if self.project_info['has_spm']:
            sections.append("""### Install Dependencies (SPM)

Dependencies are managed via Swift Package Manager. Xcode will automatically resolve them.""")

        if self.project_info['has_carthage']:
            sections.append("""### Install Dependencies (Carthage)

```bash
carthage update --use-xcframeworks
```""")

        if not any([self.project_info['has_cocoapods'], self.project_info['has_spm'], self.project_info['has_carthage']]):
            sections.append("""### Open in Xcode

```bash
open {}.xcodeproj
```""".format(self.project_info['name']))

        return '\n\n'.join(sections)

    def _generate_usage(self) -> str:
        """Generate usage section."""
        return """## 🚀 Usage

1. Open the project in Xcode
2. Select your target device or simulator
3. Press `Cmd+R` to build and run

### Quick Start

```swift
// Example usage
// Add code examples here
```"""

    def _generate_architecture(self) -> str:
        """Generate architecture section."""
        arch = self.project_info.get('architecture', 'MVC')

        return f"""## 🏗 Architecture

This project follows the **{arch}** architecture pattern.

```
{self.project_info['name']}/
├── Models/          # Data models
├── Views/           # UI components
├── ViewModels/      # Business logic (MVVM)
├── Controllers/     # View controllers (MVC)
├── Services/        # Network and data services
├── Utilities/       # Helper functions
└── Resources/       # Assets and resources
```"""

    def _generate_dependencies(self) -> str:
        """Generate dependencies section."""
        if not self.project_info['dependencies']:
            return ""

        deps_list = '\n'.join([f'- **{dep}** - [Add description]' for dep in self.project_info['dependencies']])

        return f"""## 📚 Dependencies

{deps_list}"""

    def _generate_contributing(self) -> str:
        """Generate contributing section."""
        return """## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request"""

    def _generate_license(self) -> str:
        """Generate license section."""
        return """## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with [Flaco AI](https://github.com/RouraIO/flaco.cli)
- Inspired by the iOS development community

---

**Made with ❤️ for iOS**"""
