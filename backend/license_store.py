from __future__ import annotations

import os
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class StoredLicense:
    subscription_id: str
    customer_email: str
    tier: str
    billing: str
    license_key: str
    expires_iso: str
    created_at: str
    email_sent_at: Optional[str] = None
    last_resent_at: Optional[str] = None


@dataclass(frozen=True)
class StoredActivation:
    license_key: str
    subscription_id: str
    customer_email: str
    device_id: str
    device_fingerprint_hash: str
    device_name: Optional[str]
    platform: Optional[str]
    app_version: Optional[str]
    created_at: str
    last_seen_at: str


class LicenseStore:
    """Durable SQLite storage for issued licenses, device activations, and rate limiting.

    Use LICENSE_DB_PATH to place the sqlite DB on a persistent disk in production.
    """

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

        db_dir = os.path.dirname(db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, timeout=15)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS processed_events (
                    event_id TEXT PRIMARY KEY,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS licenses (
                    subscription_id TEXT PRIMARY KEY,
                    customer_email TEXT NOT NULL,
                    tier TEXT NOT NULL,
                    billing TEXT NOT NULL,
                    license_key TEXT NOT NULL,
                    expires_iso TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    email_sent_at TEXT,
                    last_resent_at TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS rate_limits (
                    key TEXT PRIMARY KEY,
                    window_start INTEGER NOT NULL,
                    count INTEGER NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS device_activations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    license_key TEXT NOT NULL,
                    subscription_id TEXT NOT NULL,
                    customer_email TEXT NOT NULL,
                    device_id TEXT NOT NULL,
                    device_fingerprint_hash TEXT NOT NULL,
                    device_name TEXT,
                    platform TEXT,
                    app_version TEXT,
                    created_at TEXT NOT NULL,
                    last_seen_at TEXT NOT NULL,
                    UNIQUE(license_key, device_id)
                )
                """
            )

            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_device_activations_key ON device_activations(license_key)"
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_device_activations_email ON device_activations(customer_email)"
            )

            # Lightweight migrations for existing DBs
            try:
                conn.execute("ALTER TABLE licenses ADD COLUMN email_sent_at TEXT")
            except sqlite3.OperationalError:
                pass

            try:
                conn.execute("ALTER TABLE licenses ADD COLUMN last_resent_at TEXT")
            except sqlite3.OperationalError:
                pass

            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_licenses_email_key ON licenses(customer_email, license_key)"
            )
            conn.execute("CREATE INDEX IF NOT EXISTS idx_licenses_key ON licenses(license_key)")

    # -------------------------
    # Stripe idempotency
    # -------------------------

    def mark_event_processed(self, event_id: str) -> bool:
        if not event_id or event_id == "unknown":
            return True

        try:
            with self._connect() as conn:
                conn.execute(
                    "INSERT INTO processed_events(event_id, created_at) VALUES (?, ?)",
                    (event_id, datetime.utcnow().isoformat()),
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def is_event_processed(self, event_id: str) -> bool:
        if not event_id or event_id == "unknown":
            return False
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM processed_events WHERE event_id = ?",
                (event_id,),
            ).fetchone()
        return bool(row)

    # -------------------------
    # License storage
    # -------------------------

    def get_license(self, subscription_id: str) -> Optional[StoredLicense]:
        if not subscription_id:
            return None

        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                FROM licenses
                WHERE subscription_id = ?
                """,
                (subscription_id,),
            ).fetchone()

        if not row:
            return None

        return StoredLicense(
            subscription_id=row[0],
            customer_email=row[1],
            tier=row[2],
            billing=row[3],
            license_key=row[4],
            expires_iso=row[5],
            created_at=row[6],
            email_sent_at=row[7],
            last_resent_at=row[8],
        )

    def get_license_by_email_and_key(self, customer_email: str, license_key: str) -> Optional[StoredLicense]:
        customer_email = (customer_email or "").strip().lower()
        license_key = (license_key or "").strip().upper()
        if not customer_email or not license_key:
            return None

        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                FROM licenses
                WHERE lower(customer_email) = ? AND license_key = ?
                """,
                (customer_email, license_key),
            ).fetchone()

        if not row:
            return None

        return StoredLicense(
            subscription_id=row[0],
            customer_email=row[1],
            tier=row[2],
            billing=row[3],
            license_key=row[4],
            expires_iso=row[5],
            created_at=row[6],
            email_sent_at=row[7],
            last_resent_at=row[8],
        )

    def get_latest_license_for_email_and_tier(self, customer_email: str, tier: str) -> Optional[StoredLicense]:
        """Return the most recently-created license row for an email+tier.

        Useful for guarding against accidental re-issuance (multiple subscriptions/checkout sessions).
        """
        customer_email = (customer_email or "").strip().lower()
        tier = (tier or "").strip().lower()
        if not customer_email or not tier:
            return None

        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                FROM licenses
                WHERE lower(customer_email) = ? AND lower(tier) = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (customer_email, tier),
            ).fetchone()

        if not row:
            return None

        return StoredLicense(
            subscription_id=row[0],
            customer_email=row[1],
            tier=row[2],
            billing=row[3],
            license_key=row[4],
            expires_iso=row[5],
            created_at=row[6],
            email_sent_at=row[7],
            last_resent_at=row[8],
        )

    def mark_license_email_sent(self, subscription_id: str, sent_at_iso: Optional[str] = None) -> None:
        if not subscription_id:
            return
        sent_at_iso = sent_at_iso or datetime.utcnow().isoformat()
        with self._connect() as conn:
            conn.execute(
                "UPDATE licenses SET email_sent_at = ? WHERE subscription_id = ?",
                (sent_at_iso, subscription_id),
            )

    def mark_license_resent(self, subscription_id: str, resent_at_iso: Optional[str] = None) -> None:
        if not subscription_id:
            return
        resent_at_iso = resent_at_iso or datetime.utcnow().isoformat()
        with self._connect() as conn:
            conn.execute(
                "UPDATE licenses SET last_resent_at = ? WHERE subscription_id = ?",
                (resent_at_iso, subscription_id),
            )

    def update_license_email(self, subscription_id: str, new_email: str) -> None:
        new_email = (new_email or "").strip()
        if not subscription_id or not new_email:
            return
        with self._connect() as conn:
            conn.execute(
                "UPDATE licenses SET customer_email = ? WHERE subscription_id = ?",
                (new_email, subscription_id),
            )

    def allow_request(self, key: str, *, limit: int, window_seconds: int) -> bool:
        key = (key or "").strip()
        if not key or limit <= 0 or window_seconds <= 0:
            return True

        now = int(time.time())
        window_start = now - (now % window_seconds)

        with self._connect() as conn:
            row = conn.execute(
                "SELECT window_start, count FROM rate_limits WHERE key = ?",
                (key,),
            ).fetchone()

            if not row or int(row[0]) != window_start:
                conn.execute(
                    "INSERT OR REPLACE INTO rate_limits(key, window_start, count) VALUES (?, ?, ?)",
                    (key, window_start, 1),
                )
                return True

            count = int(row[1]) + 1
            conn.execute(
                "UPDATE rate_limits SET count = ? WHERE key = ?",
                (count, key),
            )
            return count <= limit

    # -------------------------
    # Device activations
    # -------------------------

    def upsert_activation(
        self,
        *,
        license_key: str,
        subscription_id: str,
        customer_email: str,
        device_id: str,
        device_fingerprint_hash: str,
        device_name: Optional[str] = None,
        platform: Optional[str] = None,
        app_version: Optional[str] = None,
    ) -> None:
        now = datetime.utcnow().isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO device_activations(
                    license_key, subscription_id, customer_email, device_id,
                    device_fingerprint_hash, device_name, platform, app_version,
                    created_at, last_seen_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(license_key, device_id) DO UPDATE SET
                    subscription_id=excluded.subscription_id,
                    customer_email=excluded.customer_email,
                    device_fingerprint_hash=excluded.device_fingerprint_hash,
                    device_name=excluded.device_name,
                    platform=excluded.platform,
                    app_version=excluded.app_version,
                    last_seen_at=excluded.last_seen_at
                """,
                (
                    license_key,
                    subscription_id,
                    customer_email,
                    device_id,
                    device_fingerprint_hash,
                    device_name,
                    platform,
                    app_version,
                    now,
                    now,
                ),
            )

    def list_activations(self, *, customer_email: str, license_key: str) -> List[StoredActivation]:
        customer_email = (customer_email or "").strip().lower()
        license_key = (license_key or "").strip().upper()
        if not customer_email or not license_key:
            return []

        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT license_key, subscription_id, customer_email, device_id,
                       device_fingerprint_hash, device_name, platform, app_version,
                       created_at, last_seen_at
                FROM device_activations
                WHERE lower(customer_email) = ? AND license_key = ?
                ORDER BY last_seen_at DESC
                """,
                (customer_email, license_key),
            ).fetchall()

        return [
            StoredActivation(
                license_key=row[0],
                subscription_id=row[1],
                customer_email=row[2],
                device_id=row[3],
                device_fingerprint_hash=row[4],
                device_name=row[5],
                platform=row[6],
                app_version=row[7],
                created_at=row[8],
                last_seen_at=row[9],
            )
            for row in rows
        ]

    def reset_activations(self, *, customer_email: str, license_key: str) -> int:
        customer_email = (customer_email or "").strip().lower()
        license_key = (license_key or "").strip().upper()
        if not customer_email or not license_key:
            return 0

        with self._connect() as conn:
            cur = conn.execute(
                "DELETE FROM device_activations WHERE lower(customer_email) = ? AND license_key = ?",
                (customer_email, license_key),
            )
            return int(cur.rowcount or 0)

    def create_license_if_missing(
        self,
        *,
        subscription_id: str,
        customer_email: str,
        tier: str,
        billing: str,
        license_key: str,
        expires_iso: str,
    ) -> Tuple[StoredLicense, bool]:
        if not subscription_id:
            raise ValueError("subscription_id is required for durable licensing")

        created = False
        try:
            with self._connect() as conn:
                conn.execute(
                    """
                    INSERT INTO licenses(subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        subscription_id,
                        customer_email,
                        tier,
                        billing,
                        license_key,
                        expires_iso,
                        datetime.utcnow().isoformat(),
                        None,
                        None,
                    ),
                )
            created = True
        except sqlite3.IntegrityError:
            created = False

        existing = self.get_license(subscription_id)
        if not existing:
            raise RuntimeError("Failed to read license after insert/check")

        return existing, created
