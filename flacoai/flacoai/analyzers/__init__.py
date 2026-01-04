"""Code analysis framework for FlacoAI."""

from .base_analyzer import (
    BaseAnalyzer,
    AnalysisResult,
    AnalysisReport,
    Severity,
    Category,
)
from .security_analyzer import SecurityAnalyzer
from .performance_analyzer import PerformanceAnalyzer
from .quality_analyzer import QualityAnalyzer
from .architecture_analyzer import ArchitectureAnalyzer
from .ios_symbols_analyzer import IOSSymbolsAnalyzer
from .ios_hig_analyzer import IOSHIGAnalyzer
from .ios_plist_analyzer import IOSPlistAnalyzer
from .swiftui_analyzer import SwiftUIAnalyzer
from .ios_version_analyzer import IOSVersionAnalyzer
from .spm_analyzer import SPMAnalyzer
from .documentation_analyzer import DocumentationAnalyzer
from .custom_rules_analyzer import CustomRulesAnalyzer

__all__ = [
    "BaseAnalyzer",
    "AnalysisResult",
    "AnalysisReport",
    "Severity",
    "Category",
    "SecurityAnalyzer",
    "PerformanceAnalyzer",
    "QualityAnalyzer",
    "ArchitectureAnalyzer",
    "IOSSymbolsAnalyzer",
    "IOSHIGAnalyzer",
    "IOSPlistAnalyzer",
    "SwiftUIAnalyzer",
    "IOSVersionAnalyzer",
    "SPMAnalyzer",
    "DocumentationAnalyzer",
    "CustomRulesAnalyzer",
]
