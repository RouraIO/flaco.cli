from __future__ import annotations

import os
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional, Tuple


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
    """Durable storage for issued licenses, device activations, and rate limiting.

    Defaults to SQLite at `db_path`. If `db_url` (or env `DATABASE_URL`) is provided and
    looks like Postgres, uses Postgres instead. This avoids data loss on ephemeral filesystems.
    """

    def __init__(self, db_path: str, *, db_url: Optional[str] = None) -> None:
        env_url = (os.getenv("DATABASE_URL") or "").strip()
        db_url = (db_url or env_url).strip() or None

        if db_url and db_url.startswith("postgres"):
            self._impl: Any = PostgresLicenseStore(db_url)
        else:
            self._impl = SqliteLicenseStore(db_path)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._impl, name)


class SqliteLicenseStore:
    """Durable SQLite storage.

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


class PostgresLicenseStore:
    """Durable Postgres storage (recommended on Render).

    Requires `psycopg2-binary` in requirements. Import is lazy so SQLite users don't need it.
    """

    def __init__(self, db_url: str) -> None:
        self.db_url = db_url
        self._psycopg2 = None
        self._init_db()

    def _pg(self):
        if self._psycopg2 is None:
            import psycopg2  # type: ignore

            self._psycopg2 = psycopg2
        return self._psycopg2

    def _connect(self):
        pg = self._pg()
        conn = pg.connect(self.db_url, connect_timeout=10)
        conn.autocommit = True
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS processed_events (
                        event_id TEXT PRIMARY KEY,
                        created_at TEXT NOT NULL
                    )
                    """
                )
                cur.execute(
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
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS rate_limits (
                        key TEXT PRIMARY KEY,
                        window_start BIGINT NOT NULL,
                        count INTEGER NOT NULL
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS device_activations (
                        id SERIAL PRIMARY KEY,
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

                cur.execute(
                    "CREATE INDEX IF NOT EXISTS idx_device_activations_key ON device_activations(license_key)"
                )
                cur.execute(
                    "CREATE INDEX IF NOT EXISTS idx_device_activations_email ON device_activations(customer_email)"
                )
                cur.execute(
                    "CREATE INDEX IF NOT EXISTS idx_licenses_email_key ON licenses(customer_email, license_key)"
                )
                cur.execute("CREATE INDEX IF NOT EXISTS idx_licenses_key ON licenses(license_key)")

    # -------------------------
    # Stripe idempotency
    # -------------------------

    def mark_event_processed(self, event_id: str) -> bool:
        if not event_id or event_id == "unknown":
            return True

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO processed_events(event_id, created_at)
                    VALUES (%s, %s)
                    ON CONFLICT (event_id) DO NOTHING
                    """,
                    (event_id, datetime.utcnow().isoformat()),
                )
                return bool(cur.rowcount)

    def is_event_processed(self, event_id: str) -> bool:
        if not event_id or event_id == "unknown":
            return False
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT 1 FROM processed_events WHERE event_id = %s",
                    (event_id,),
                )
                return bool(cur.fetchone())

    # -------------------------
    # License storage
    # -------------------------

    def get_license(self, subscription_id: str) -> Optional[StoredLicense]:
        if not subscription_id:
            return None

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                    FROM licenses
                    WHERE subscription_id = %s
                    """,
                    (subscription_id,),
                )
                row = cur.fetchone()

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
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                    FROM licenses
                    WHERE lower(customer_email) = %s AND license_key = %s
                    """,
                    (customer_email, license_key),
                )
                row = cur.fetchone()

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
        customer_email = (customer_email or "").strip().lower()
        tier = (tier or "").strip().lower()
        if not customer_email or not tier:
            return None

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at
                    FROM licenses
                    WHERE lower(customer_email) = %s AND lower(tier) = %s
                    ORDER BY created_at DESC
                    LIMIT 1
                    """,
                    (customer_email, tier),
                )
                row = cur.fetchone()

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
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE licenses SET email_sent_at = %s WHERE subscription_id = %s",
                    (sent_at_iso, subscription_id),
                )

    def mark_license_resent(self, subscription_id: str, resent_at_iso: Optional[str] = None) -> None:
        if not subscription_id:
            return
        resent_at_iso = resent_at_iso or datetime.utcnow().isoformat()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE licenses SET last_resent_at = %s WHERE subscription_id = %s",
                    (resent_at_iso, subscription_id),
                )

    def update_license_email(self, subscription_id: str, new_email: str) -> None:
        new_email = (new_email or "").strip()
        if not subscription_id or not new_email:
            return
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE licenses SET customer_email = %s WHERE subscription_id = %s",
                    (new_email, subscription_id),
                )

    def allow_request(self, key: str, *, limit: int, window_seconds: int) -> bool:
        key = (key or "").strip()
        if not key or limit <= 0 or window_seconds <= 0:
            return True

        now = int(time.time())
        window_start = now - (now % window_seconds)

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT window_start, count FROM rate_limits WHERE key = %s",
                    (key,),
                )
                row = cur.fetchone()

                if (not row) or int(row[0]) != window_start:
                    cur.execute(
                        """
                        INSERT INTO rate_limits(key, window_start, count)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (key) DO UPDATE SET window_start = EXCLUDED.window_start, count = EXCLUDED.count
                        """,
                        (key, window_start, 1),
                    )
                    return True

                count = int(row[1]) + 1
                cur.execute(
                    "UPDATE rate_limits SET count = %s WHERE key = %s",
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
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO device_activations(
                        license_key, subscription_id, customer_email, device_id,
                        device_fingerprint_hash, device_name, platform, app_version,
                        created_at, last_seen_at
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (license_key, device_id) DO UPDATE SET
                        subscription_id=EXCLUDED.subscription_id,
                        customer_email=EXCLUDED.customer_email,
                        device_fingerprint_hash=EXCLUDED.device_fingerprint_hash,
                        device_name=EXCLUDED.device_name,
                        platform=EXCLUDED.platform,
                        app_version=EXCLUDED.app_version,
                        last_seen_at=EXCLUDED.last_seen_at
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
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT license_key, subscription_id, customer_email, device_id,
                           device_fingerprint_hash, device_name, platform, app_version,
                           created_at, last_seen_at
                    FROM device_activations
                    WHERE lower(customer_email) = %s AND license_key = %s
                    ORDER BY last_seen_at DESC
                    """,
                    (customer_email, license_key),
                )
                rows = cur.fetchall() or []

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
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM device_activations WHERE lower(customer_email) = %s AND license_key = %s",
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
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO licenses(subscription_id, customer_email, tier, billing, license_key, expires_iso, created_at, email_sent_at, last_resent_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (subscription_id) DO NOTHING
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
                created = bool(cur.rowcount)

        existing = self.get_license(subscription_id)
        if not existing:
            raise RuntimeError("Failed to read license after insert/check")

        return existing, created
