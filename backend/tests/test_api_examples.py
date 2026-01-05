import os
from datetime import datetime, timedelta

import pytest


@pytest.fixture(autouse=True)
def _env(monkeypatch, tmp_path):
    monkeypatch.setenv("FLACO_TESTING", "1")
    monkeypatch.setenv("STRIPE_SECRET_KEY", "sk_test_testing")
    monkeypatch.setenv("STRIPE_WEBHOOK_SECRET", "whsec_testing")
    monkeypatch.setenv("FLACO_LICENSE_SECRET", "test_secret")

    db_path = tmp_path / "licenses.sqlite3"
    monkeypatch.setenv("LICENSE_DB_PATH", str(db_path))

    pro_path = tmp_path / "examples_pro.md"
    pro_path.write_text("# PRO EXAMPLES\n\nHello", encoding="utf-8")
    monkeypatch.setenv("PRO_EXAMPLES_PATH", str(pro_path))


@pytest.fixture()
def client():
    # Import after env setup so app module reads env
    from backend.app import app

    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c


def _issue_license(*, subscription_id: str, email: str, tier: str = "pro") -> str:
    from backend.license_generator import LicenseKeyGenerator
    from backend.license_store import LicenseStore
    from backend.app import LICENSE_DB_PATH

    store = LicenseStore(LICENSE_DB_PATH)
    gen = LicenseKeyGenerator(secret_key=os.environ["FLACO_LICENSE_SECRET"])
    expires = datetime.now() + timedelta(days=30)
    key = gen.generate_license_key(email=email, tier=tier, expires=expires)

    store.create_license_if_missing(
        subscription_id=subscription_id,
        customer_email=email,
        tier=tier,
        billing="monthly",
        license_key=key,
        expires_iso=expires.isoformat(),
    )
    return key


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "healthy"


def test_examples_pro_requires_email_and_key(client):
    resp = client.post("/api/examples/pro", json={})
    assert resp.status_code == 400


def test_examples_pro_denies_invalid_license(client):
    resp = client.post("/api/examples/pro", json={"email": "a@b.com", "license_key": "FLACO-00000000-00000000-00000000"})
    assert resp.status_code == 403


def test_examples_pro_allows_pro_license(client):
    email = "pro@example.com"
    key = _issue_license(subscription_id="sub_123", email=email, tier="pro")

    resp = client.post("/api/examples/pro", json={"email": email, "license_key": key})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["success"] is True
    assert "# PRO EXAMPLES" in data["markdown"]


def test_verify_license_returns_tier_and_expires(client):
    email = "user@example.com"
    key = _issue_license(subscription_id="sub_456", email=email, tier="enterprise")

    resp = client.post("/api/verify-license", json={"email": email, "license_key": key})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["success"] is True
    assert data["valid"] is True
    assert data["tier"] == "enterprise"
    assert data["email"] == email
