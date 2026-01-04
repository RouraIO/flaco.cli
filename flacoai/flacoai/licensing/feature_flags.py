"""Feature flag management using LaunchDarkly (optional)."""

import os
from typing import Optional, Dict, Any


class FeatureFlags:
    """Manage feature flags with optional LaunchDarkly integration."""

    def __init__(self, user_email: Optional[str] = None, tier: str = "free", io=None):
        """Initialize feature flags.

        Args:
            user_email: User email for LaunchDarkly context
            tier: License tier (free/pro/enterprise)
            io: IO object for output
        """
        self.user_email = user_email
        self.tier = tier
        self.io = io
        self.ld_client = None

        # Try to initialize LaunchDarkly if SDK key is provided
        self._init_launchdarkly()

    def _init_launchdarkly(self):
        """Initialize LaunchDarkly client if SDK key is available."""
        sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")

        if not sdk_key:
            # LaunchDarkly not configured - use fallback values
            return

        try:
            import ldclient
            from ldclient.config import Config

            # Initialize LaunchDarkly client
            ldclient.set_config(Config(sdk_key))
            self.ld_client = ldclient.get()

            if self.io and self.io.verbose:
                self.io.tool_output("✓ LaunchDarkly initialized")

        except ImportError:
            if self.io and self.io.verbose:
                self.io.tool_output("LaunchDarkly SDK not installed. Using fallback values.")
                self.io.tool_output("Install with: pip install launchdarkly-server-sdk")

        except Exception as e:
            if self.io and self.io.verbose:
                self.io.tool_error(f"LaunchDarkly initialization failed: {e}")

    def is_enabled(self, feature_name: str, default: bool = False) -> bool:
        """Check if a feature is enabled.

        Args:
            feature_name: Name of feature flag
            default: Default value if LaunchDarkly is not available

        Returns:
            True if feature is enabled
        """
        if self.ld_client:
            try:
                user = self._get_user_context()
                return self.ld_client.variation(feature_name, user, default)
            except Exception as e:
                if self.io and self.io.verbose:
                    self.io.tool_error(f"LaunchDarkly error: {e}")
                return default

        # Fallback: use tier-based defaults
        return self._get_fallback_value(feature_name, default)

    def get_value(self, feature_name: str, default: Any = None) -> Any:
        """Get feature flag value (for non-boolean flags).

        Args:
            feature_name: Name of feature flag
            default: Default value if LaunchDarkly is not available

        Returns:
            Feature flag value
        """
        if self.ld_client:
            try:
                user = self._get_user_context()
                return self.ld_client.variation(feature_name, user, default)
            except Exception as e:
                if self.io and self.io.verbose:
                    self.io.tool_error(f"LaunchDarkly error: {e}")
                return default

        return self._get_fallback_value(feature_name, default)

    def _get_user_context(self) -> Dict:
        """Get LaunchDarkly user context.

        Returns:
            User context dict
        """
        return {
            "key": self.user_email or "anonymous",
            "email": self.user_email,
            "custom": {
                "tier": self.tier,
            },
        }

    def _get_fallback_value(self, feature_name: str, default: Any) -> Any:
        """Get fallback value when LaunchDarkly is not available.

        Args:
            feature_name: Name of feature
            default: Default value

        Returns:
            Fallback value based on tier
        """
        # Define feature flags and their defaults by tier
        feature_defaults = {
            # Premium analyzers
            "crash_prediction_analyzer": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "performance_profiler_analyzer": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "memory_leak_analyzer": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "security_scoring_analyzer": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "technical_debt_analyzer": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },

            # Advanced features
            "advanced_auto_fix": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "batch_fix_mode": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "github_app_integration": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "slack_notifications": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },
            "local_team_dashboard": {
                "free": False,
                "pro": True,
                "enterprise": True,
            },

            # Enterprise-only features
            "cloud_dashboard": {
                "free": False,
                "pro": False,
                "enterprise": True,
            },
            "sso_saml": {
                "free": False,
                "pro": False,
                "enterprise": True,
            },
            "on_premises_deployment": {
                "free": False,
                "pro": False,
                "enterprise": True,
            },
            "custom_analyzer_development": {
                "free": False,
                "pro": False,
                "enterprise": True,
            },

            # Experimental features (can be toggled via LaunchDarkly)
            "experimental_ai_refactoring": {
                "free": False,
                "pro": False,
                "enterprise": False,  # Off by default, can be enabled via LD
            },
            "experimental_code_generation": {
                "free": False,
                "pro": False,
                "enterprise": False,
            },
        }

        if feature_name in feature_defaults:
            tier_defaults = feature_defaults[feature_name]
            return tier_defaults.get(self.tier, default)

        return default

    def close(self):
        """Close LaunchDarkly client."""
        if self.ld_client:
            try:
                self.ld_client.close()
            except Exception:
                pass


# Convenience function for checking features
def check_feature(feature_name: str, license_manager, default: bool = False) -> bool:
    """Check if a feature is enabled for current user.

    Args:
        feature_name: Name of feature
        license_manager: LicenseManager instance
        default: Default value

    Returns:
        True if feature is enabled
    """
    license_info = license_manager.get_license_info()

    flags = FeatureFlags(
        user_email=license_info.get("email"),
        tier=license_info.get("tier", "free")
    )

    return flags.is_enabled(feature_name, default)
