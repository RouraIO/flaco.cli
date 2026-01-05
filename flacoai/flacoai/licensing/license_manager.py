"""License validation and management for Flaco AI tiers."""

import json
import os
import hashlib
import hmac
from pathlib import Path
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, Dict
import platform
import subprocess

try:
    import requests  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    class _MissingRequests:
        def __getattr__(self, _name: str):
            raise RuntimeError(
                "Networked license operations require the 'requests' package. "
                "Install CLI requirements (for example: `pip install -r requirements.txt`) and try again."
            )

    requests = _MissingRequests()  # type: ignore


class LicenseTier(Enum):
    """License tiers for Flaco AI."""
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class LicenseManager:
    """Manages license validation and tier checking."""

    # Secret key for signing licenses (in production, use env var)
    # This should be kept secret and not committed to git
    DEFAULT_SECRET_SENTINEL = "CHANGE_ME_IN_PRODUCTION"
    SECRET_KEY = os.getenv("FLACO_LICENSE_SECRET", DEFAULT_SECRET_SENTINEL)

    LICENSE_SERVER_URL = os.getenv(
        "FLACO_LICENSE_SERVER_URL", "https://flaco-license-server.onrender.com"
    ).rstrip("/")

    def __init__(self, io=None):
        """Initialize license manager.

        Args:
            io: IO object for output
        """
        self.io = io
        self.license_file = Path.home() / ".flaco" / "license.json"
        self.license_file.parent.mkdir(parents=True, exist_ok=True)
        self.device_file = Path.home() / ".flaco" / "device.json"
        self._cached_license = None

    def _get_or_create_device_id(self) -> str:
        try:
            if self.device_file.exists():
                data = json.loads(self.device_file.read_text() or "{}")
                device_id = (data.get("device_id") or "").strip()
                if device_id:
                    return device_id
        except Exception:
            pass

        # Create a random UUID (no hardware fingerprint stored locally)
        import uuid

        device_id = str(uuid.uuid4())
        try:
            self.device_file.parent.mkdir(parents=True, exist_ok=True)
            self.device_file.write_text(json.dumps({"device_id": device_id}, indent=2))
        except Exception:
            pass
        return device_id

    def _get_hardware_fingerprint_source(self) -> str:
        """Best-effort hardware-ish fingerprint source string.

        We only send/store a SHA256 hash of this string server-side.
        """
        parts = [
            platform.system() or "",
            platform.release() or "",
            platform.machine() or "",
        ]

        try:
            node = platform.node() or ""
            if node:
                parts.append(node)
        except Exception:
            pass

        # macOS: IOPlatformUUID is stable per machine
        if platform.system().lower() == "darwin":
            try:
                out = subprocess.check_output(
                    ["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"],
                    stderr=subprocess.DEVNULL,
                    text=True,
                    timeout=2,
                )
                for line in out.splitlines():
                    if "IOPlatformUUID" in line:
                        # ... "IOPlatformUUID" = "XXXXXXXX-...."
                        val = line.split("=")[-1].strip().strip('"')
                        if val:
                            parts.append(val)
                        break
            except Exception:
                pass

        # Linux: /etc/machine-id
        if platform.system().lower() == "linux":
            try:
                mid = Path("/etc/machine-id").read_text().strip()
                if mid:
                    parts.append(mid)
            except Exception:
                pass

        return "|".join(p for p in parts if p)

    def _device_payload(self) -> Dict:
        device_id = self._get_or_create_device_id()
        fp_source = self._get_hardware_fingerprint_source()
        fp_hash = hashlib.sha256(fp_source.encode("utf-8")).hexdigest() if fp_source else ""
        return {
            "device_id": device_id,
            "device_fingerprint_hash": fp_hash,
            "device_name": platform.node() or None,
            "platform": f"{platform.system()} {platform.release()}".strip(),
            "app_version": os.getenv("SETUPTOOLS_SCM_PRETEND_VERSION") or None,
        }

    def get_tier(self) -> LicenseTier:
        """Get current license tier.

        Returns:
            LicenseTier enum value
        """
        license_data = self.load_license()

        if not license_data:
            return LicenseTier.FREE

        # Prefer server-backed validation when configured.
        if self.LICENSE_SERVER_URL:
            if not self.validate_with_server(license_data):
                if self.io:
                    self.io.tool_error("Invalid license key. Reverting to FREE tier.")
                return LicenseTier.FREE

        # Fallback local validation
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

        # Validate signature (HMAC-based) only if a real secret is configured.
        # Many local/dev installs won't have FLACO_LICENSE_SECRET set, so we fall back
        # to format+expiry validation to avoid bricking activation.
        if self.SECRET_KEY != self.DEFAULT_SECRET_SENTINEL:
            expected_signature = self._generate_signature(
                license_data["email"],
                license_data["tier"],
                license_data["expires"],
            )

            if not hmac.compare_digest(license_data["key"], expected_signature):
                if self.io and getattr(self.io, "verbose", False):
                    self.io.tool_error("Invalid license signature")
                return False

        return True

    def validate_with_server(self, license_data: Dict) -> bool:
        """Validate license against the license server DB.

        Returns False if server confirms invalid.
        If server is unreachable, falls back to local validation.
        """

        if not license_data:
            return False

        email = (license_data.get("email") or "").strip()
        key = (license_data.get("key") or "").strip()
        if not email or not key:
            return False

        grace_days = int(os.getenv("FLACO_OFFLINE_GRACE_DAYS", "7") or "7")

        try:
            payload = {
                "email": email,
                "license_key": key,
            }
            payload.update(self._device_payload())

            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/verify-license",
                json=payload,
                timeout=10,
            )
            resp.raise_for_status()
            payload = resp.json() or {}

            if not payload.get("success"):
                return False

            valid = bool(payload.get("valid"))
            if valid:
                # Update local cache timestamps + authoritative tier/expiry
                try:
                    license_data["tier"] = (payload.get("tier") or license_data.get("tier") or "free")
                    license_data["expires"] = (payload.get("expires") or license_data.get("expires"))
                    license_data["last_verified_at"] = datetime.now().isoformat()
                    with open(self.license_file, 'w') as f:
                        json.dump(license_data, f, indent=2)
                    self._cached_license = license_data
                except Exception:
                    pass
            return valid
        except Exception as e:
            # Offline grace: if we successfully verified recently, keep working.
            last_verified_at = (license_data.get("last_verified_at") or "").strip()
            if last_verified_at:
                try:
                    last_dt = datetime.fromisoformat(last_verified_at)
                    if datetime.now() - last_dt <= timedelta(days=grace_days):
                        return self.validate_license(license_data)
                except Exception:
                    pass

            if self.io and getattr(self.io, "verbose", False):
                self.io.tool_warning(f"License server validation failed: {e}")
            return self.validate_license(license_data)

    def _cache_dir(self) -> Path:
        d = Path.home() / ".flaco" / "cache"
        try:
            d.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        return d

    def get_cached_pro_examples_markdown(self) -> Optional[str]:
        """Return cached PRO examples markdown if present."""
        try:
            p = self._cache_dir() / "examples_pro.md"
            if p.exists():
                return p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return None
        return None

    def fetch_pro_examples_markdown(self) -> Optional[str]:
        """Fetch PRO examples from the license server (gated by tier).

        Returns markdown on success; otherwise returns None.
        Also updates the local cache if a document is fetched.
        """

        license_data = self.load_license()
        if not license_data:
            return None

        if not self.LICENSE_SERVER_URL:
            return None

        email = (license_data.get("email") or "").strip()
        key = (license_data.get("key") or "").strip()
        if not email or not key:
            return None

        try:
            payload = {"email": email, "license_key": key}
            payload.update(self._device_payload())

            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/examples/pro",
                json=payload,
                timeout=10,
            )

            if resp.status_code == 403:
                return None

            resp.raise_for_status()
            data = resp.json() or {}
            md = (data.get("markdown") or "").strip()
            if not data.get("success") or not md:
                return None

            try:
                (self._cache_dir() / "examples_pro.md").write_text(md, encoding="utf-8")
            except Exception:
                pass

            return md
        except Exception:
            return None

    def _is_valid_license_key_format(self, key: str) -> bool:
        if not isinstance(key, str) or not key.startswith("FLACO-"):
            return False
        parts = key.split("-")
        if len(parts) != 4 or parts[0] != "FLACO":
            return False
        for part in parts[1:]:
            if len(part) != 8:
                return False
            try:
                int(part, 16)
            except ValueError:
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
        # Basic input validation
        if not self._is_valid_license_key_format(key):
            if self.io:
                self.io.tool_error("Invalid license key format")
            return False

        # Server-backed activation: validate key against the license server DB and
        # store the tier/expiry returned by the server.
        try:
            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/verify-license",
                json={"email": email, "license_key": key},
                timeout=15,
            )
            resp.raise_for_status()
            payload = resp.json() or {}

            if not payload.get("success"):
                if self.io:
                    self.io.tool_error("License server returned an error")
                return False

            if not payload.get("valid"):
                if self.io:
                    self.io.tool_error(payload.get("message") or "Invalid license key")
                return False

            tier = (payload.get("tier") or "pro").lower()
            expires = payload.get("expires")
            if not expires:
                # Defensive fallback if server doesn't return expiry
                expires = (datetime.now() + timedelta(days=365)).date().isoformat()

            ok = self.save_license(email, key, tier, expires)
            if not ok:
                return False

            # Record device activation (unlimited devices, but tracked)
            try:
                act_payload = {"email": email, "license_key": key}
                act_payload.update(self._device_payload())
                act_resp = requests.post(
                    f"{self.LICENSE_SERVER_URL}/api/activate-device",
                    json=act_payload,
                    timeout=15,
                )
                # Ignore failure here; license is still activated locally.
                if act_resp.ok:
                    try:
                        ld = self.load_license() or {}
                        ld["last_verified_at"] = datetime.now().isoformat()
                        with open(self.license_file, 'w') as f:
                            json.dump(ld, f, indent=2)
                        self._cached_license = ld
                    except Exception:
                        pass
            except Exception:
                pass

            return True
        except Exception as e:
            if self.io:
                self.io.tool_error(f"License activation error: {e}")
            return False

    def list_devices(self) -> Optional[list]:
        license_data = self.load_license() or {}
        email = (license_data.get("email") or "").strip()
        key = (license_data.get("key") or "").strip()
        if not email or not key:
            if self.io:
                self.io.tool_error("No active license found.")
            return None

        try:
            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/list-devices",
                json={"email": email, "license_key": key},
                timeout=15,
            )
            resp.raise_for_status()
            payload = resp.json() or {}
            if not payload.get("success"):
                return None
            return payload.get("devices") or []
        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to list devices: {e}")
            return None

    def reset_devices(self) -> bool:
        license_data = self.load_license() or {}
        email = (license_data.get("email") or "").strip()
        key = (license_data.get("key") or "").strip()
        if not email or not key:
            if self.io:
                self.io.tool_error("No active license found.")
            return False

        try:
            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/reset-devices",
                json={"email": email, "license_key": key},
                timeout=15,
            )
            if resp.status_code == 429:
                if self.io:
                    self.io.tool_error("Rate limited. Please wait and try again.")
                return False
            resp.raise_for_status()
            payload = resp.json() or {}
            return bool(payload.get("success"))
        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to reset devices: {e}")
            return False

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

    def resend_license_email(self, email: Optional[str] = None, key: Optional[str] = None) -> bool:
        """Ask the license server to resend the license email (rate-limited server-side)."""
        license_data = self.load_license() or {}
        email = (email or license_data.get("email") or "").strip()
        key = (key or license_data.get("key") or "").strip()
        if not email or not key:
            if self.io:
                self.io.tool_error("No license info found. Provide: /license resend <email> <key>")
            return False

        try:
            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/resend-license",
                json={"email": email, "license_key": key},
                timeout=15,
            )
            if resp.status_code == 429:
                if self.io:
                    self.io.tool_error("Rate limited. Please wait and try again.")
                return False
            resp.raise_for_status()
            payload = resp.json() or {}
            ok = bool(payload.get("success"))
            if ok and self.io:
                self.io.tool_output("✓ License email requested")
            return ok
        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to request resend: {e}")
            return False

    def change_license_email(self, new_email: str) -> bool:
        """Change the email associated with this license on the server and update local state."""
        license_data = self.load_license() or {}
        email = (license_data.get("email") or "").strip()
        key = (license_data.get("key") or "").strip()
        new_email = (new_email or "").strip()

        if not email or not key:
            if self.io:
                self.io.tool_error("No active license found. Activate first.")
            return False
        if not new_email:
            if self.io:
                self.io.tool_error("New email is required")
            return False

        try:
            resp = requests.post(
                f"{self.LICENSE_SERVER_URL}/api/change-license-email",
                json={"email": email, "license_key": key, "new_email": new_email},
                timeout=15,
            )
            if resp.status_code == 429:
                if self.io:
                    self.io.tool_error("Rate limited. Please wait and try again.")
                return False
            resp.raise_for_status()
            payload = resp.json() or {}
            if not payload.get("success"):
                if self.io:
                    self.io.tool_error("Failed to change email")
                return False

            # Update local license.json to keep CLI consistent.
            license_data["email"] = payload.get("email") or new_email
            with open(self.license_file, 'w') as f:
                json.dump(license_data, f, indent=2)
            self._cached_license = license_data
            if self.io:
                self.io.tool_output(f"✓ License email updated to {license_data['email']}")
            return True
        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to change email: {e}")
            return False

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
