"""License key generation for Flaco AI."""

import hmac
import hashlib
from datetime import datetime
from typing import Optional


class LicenseKeyGenerator:
    """Generate and verify HMAC-signed license keys."""

    def __init__(self, secret_key: str):
        """Initialize license generator.

        Args:
            secret_key: Secret key for HMAC signing (FLACO_LICENSE_SECRET)
        """
        self.secret_key = secret_key

    def generate_license_key(self, email: str, tier: str, expires: datetime) -> str:
        """Generate HMAC-signed license key.

        Format: FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX
        Where X = HMAC-SHA256(email:tier:expires)[:24]

        Args:
            email: Customer email
            tier: License tier (pro, enterprise)
            expires: Expiry datetime

        Returns:
            License key string
        """
        # Create message to sign
        expires_str = expires.isoformat()
        message = f"{email}:{tier}:{expires_str}".encode()

        # Generate HMAC signature
        signature = hmac.new(
            self.secret_key.encode(),
            message,
            hashlib.sha256
        ).hexdigest()

        # Format as FLACO-XXXXXXXX-XXXXXXXX-XXXXXXXX
        key = f"FLACO-{signature[:8].upper()}-{signature[8:16].upper()}-{signature[16:24].upper()}"

        return key

    def verify_license_key(self, email: str, license_key: str, tier: Optional[str] = None,
                          expires: Optional[datetime] = None) -> bool:
        """Verify a license key against email/tier/expires.

        Args:
            email: Customer email
            license_key: License key to verify
            tier: Expected tier (if known)
            expires: Expected expiry (if known)

        Returns:
            True if license key is valid
        """
        if not license_key.startswith("FLACO-"):
            return False

        # If tier/expires not provided, we can't fully verify
        # (you'd need to look them up from database)
        if tier and expires:
            expected_key = self.generate_license_key(email, tier, expires)
            return hmac.compare_digest(license_key, expected_key)

        # Partial verification - just check format
        parts = license_key.split("-")
        if len(parts) != 4:
            return False

        if parts[0] != "FLACO":
            return False

        # Check each part is 8 hex characters
        for part in parts[1:]:
            if len(part) != 8 or not all(c in "0123456789ABCDEF" for c in part):
                return False

        return True
