"""License validation and management for Flaco AI tiers."""

import json
import os
import hashlib
import hmac
from pathlib import Path
from datetime import datetime
from enum import Enum
from typing import Optional, Dict


class LicenseTier(Enum):
    """License tiers for Flaco AI."""
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class LicenseManager:
    """Manages license validation and tier checking."""

    # Secret key for signing licenses (in production, use env var)
    # This should be kept secret and not committed to git
    SECRET_KEY = os.getenv("FLACO_LICENSE_SECRET", "CHANGE_ME_IN_PRODUCTION")

    def __init__(self, io=None):
        """Initialize license manager.

        Args:
            io: IO object for output
        """
        self.io = io
        self.license_file = Path.home() / ".flaco" / "license.json"
        self.license_file.parent.mkdir(parents=True, exist_ok=True)
        self._cached_license = None

    def get_tier(self) -> LicenseTier:
        """Get current license tier.

        Returns:
            LicenseTier enum value
        """
        license_data = self.load_license()

        if not license_data:
            return LicenseTier.FREE

        # Check if license is valid
        if not self.validate_license(license_data):
            if self.io:
                self.io.tool_error("Invalid license key. Reverting to FREE tier.")
            return LicenseTier.FREE

        tier_str = license_data.get("tier", "free").lower()

        try:
            return LicenseTier(tier_str)
        except ValueError:
            return LicenseTier.FREE

    def has_feature(self, feature_name: str) -> bool:
        """Check if current tier has access to feature.

        Args:
            feature_name: Name of feature to check

        Returns:
            True if feature is available
        """
        tier = self.get_tier()

        # Define feature access by tier
        features = {
            LicenseTier.FREE: {
                "basic_analyzers",
                "review",
                "ci_integration",
                "baseline",
                "github_export",
                "custom_rules",
                "smart_context",
                "basic_fix",
            },
            LicenseTier.PRO: {
                # All free features +
                "basic_analyzers",
                "review",
                "ci_integration",
                "baseline",
                "github_export",
                "custom_rules",
                "smart_context",
                "basic_fix",
                # Pro features
                "premium_analyzers",
                "crash_prediction",
                "memory_leak_detection",
                "security_scoring",
                "technical_debt",
                "performance_profiling",
                "advanced_fix",
                "batch_fix",
                "github_app",
                "slack_notifications",
                "local_dashboard",
            },
            LicenseTier.ENTERPRISE: {
                # All pro features +
                "basic_analyzers",
                "review",
                "ci_integration",
                "baseline",
                "github_export",
                "custom_rules",
                "smart_context",
                "basic_fix",
                "premium_analyzers",
                "crash_prediction",
                "memory_leak_detection",
                "security_scoring",
                "technical_debt",
                "performance_profiling",
                "advanced_fix",
                "batch_fix",
                "github_app",
                "slack_notifications",
                "local_dashboard",
                # Enterprise features
                "cloud_dashboard",
                "sso_saml",
                "on_premises",
                "custom_analyzers",
                "priority_support",
                "dedicated_account_manager",
            },
        }

        tier_features = features.get(tier, set())
        return feature_name in tier_features

    def load_license(self) -> Optional[Dict]:
        """Load license from file.

        Returns:
            License data dict or None
        """
        if self._cached_license:
            return self._cached_license

        if not self.license_file.exists():
            return None

        try:
            with open(self.license_file, 'r') as f:
                license_data = json.load(f)

            self._cached_license = license_data
            return license_data

        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to load license: {e}")
            return None

    def save_license(self, email: str, key: str, tier: str, expires: str) -> bool:
        """Save license to file.

        Args:
            email: User email
            key: License key
            tier: License tier (free/pro/enterprise)
            expires: Expiration date (YYYY-MM-DD)

        Returns:
            True if saved successfully
        """
        license_data = {
            "email": email,
            "key": key,
            "tier": tier,
            "expires": expires,
            "activated": datetime.now().isoformat(),
        }

        try:
            with open(self.license_file, 'w') as f:
                json.dump(license_data, f, indent=2)

            self._cached_license = license_data

            if self.io:
                self.io.tool_output(f"✓ License activated for {email} ({tier} tier)")

            return True

        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to save license: {e}")
            return False

    def validate_license(self, license_data: Dict) -> bool:
        """Validate license key and expiration.

        Args:
            license_data: License data dict

        Returns:
            True if license is valid
        """
        if not license_data:
            return False

        # Check required fields
        required_fields = ["email", "key", "tier", "expires"]
        if not all(field in license_data for field in required_fields):
            return False

        # Check expiration
        try:
            expires = datetime.fromisoformat(license_data["expires"])
            if datetime.now() > expires:
                if self.io:
                    self.io.tool_error("License has expired")
                return False
        except Exception:
            return False

        # Validate signature (simple HMAC-based validation)
        expected_signature = self._generate_signature(
            license_data["email"],
            license_data["tier"],
            license_data["expires"]
        )

        if not hmac.compare_digest(license_data["key"], expected_signature):
            if self.io and self.io.verbose:
                self.io.tool_error("Invalid license signature")
            return False

        return True

    def _generate_signature(self, email: str, tier: str, expires: str) -> str:
        """Generate license key signature.

        Args:
            email: User email
            tier: License tier
            expires: Expiration date

        Returns:
            License key signature
        """
        message = f"{email}:{tier}:{expires}".encode()
        signature = hmac.new(
            self.SECRET_KEY.encode(),
            message,
            hashlib.sha256
        ).hexdigest()

        return f"FLACO-{signature[:8].upper()}-{signature[8:16].upper()}-{signature[16:24].upper()}"

    def generate_license_key(self, email: str, tier: str, expires: str) -> str:
        """Generate a new license key (for internal use/sales).

        Args:
            email: User email
            tier: License tier (free/pro/enterprise)
            expires: Expiration date (YYYY-MM-DD)

        Returns:
            License key string
        """
        return self._generate_signature(email, tier, expires)

    def activate_license(self, email: str, key: str) -> bool:
        """Activate a license key.

        Args:
            email: User email
            key: License key

        Returns:
            True if activated successfully
        """
        # Parse tier and expiration from key validation
        # In a real system, you'd verify this against a server

        # For now, trust the key format and validate signature
        # You would typically hit a license server here

        # Decode tier from a validation service (placeholder)
        # In production, this would be an API call to your license server
        tier = "pro"  # Default to pro for now
        expires = "2027-01-03"  # 1 year from now

        # Create license data
        license_data = {
            "email": email,
            "key": key,
            "tier": tier,
            "expires": expires,
        }

        # Validate the key
        if not self.validate_license(license_data):
            if self.io:
                self.io.tool_error("Invalid license key")
            return False

        # Save license
        return self.save_license(email, key, tier, expires)

    def deactivate_license(self) -> bool:
        """Deactivate current license (revert to free).

        Returns:
            True if deactivated successfully
        """
        if self.license_file.exists():
            try:
                self.license_file.unlink()
                self._cached_license = None

                if self.io:
                    self.io.tool_output("✓ License deactivated. Reverted to FREE tier.")

                return True

            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Failed to deactivate license: {e}")
                return False

        return True

    def get_license_info(self) -> Dict:
        """Get current license information.

        Returns:
            Dict with license info
        """
        license_data = self.load_license()
        tier = self.get_tier()

        if not license_data:
            return {
                "tier": tier.value,
                "email": None,
                "expires": None,
                "status": "free",
            }

        try:
            expires = datetime.fromisoformat(license_data["expires"])
            days_remaining = (expires - datetime.now()).days

            status = "active" if days_remaining > 0 else "expired"

            return {
                "tier": tier.value,
                "email": license_data.get("email"),
                "expires": license_data.get("expires"),
                "days_remaining": max(0, days_remaining),
                "status": status,
                "activated": license_data.get("activated"),
            }

        except Exception:
            return {
                "tier": tier.value,
                "email": license_data.get("email"),
                "expires": license_data.get("expires"),
                "status": "invalid",
            }
