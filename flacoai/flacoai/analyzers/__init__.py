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
]
