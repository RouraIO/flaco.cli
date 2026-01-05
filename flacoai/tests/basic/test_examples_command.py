from __future__ import annotations

from flacoai.commands import Commands
from flacoai.licensing.license_manager import LicenseManager, LicenseTier


class DummyIO:
    def __init__(self):
        self.outputs: list[str] = []
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.assistant: list[str] = []
        self.pretty = False
        self.verbose = False

    def tool_output(self, *messages, **kwargs):
        self.outputs.append(" ".join(str(m) for m in messages).strip())

    def tool_error(self, message="", **kwargs):
        self.errors.append(str(message))

    def tool_warning(self, message="", **kwargs):
        self.warnings.append(str(message))

    def assistant_output(self, message, pretty=None):
        self.assistant.append(str(message))


def test_examples_free_renders_markdown():
    io = DummyIO()
    cmds = Commands(io=io, coder=None)
    cmds.cmd_examples("")

    assert io.assistant
    assert "Flaco AI Examples (FREE)" in io.assistant[0]


def test_examples_pro_locked_on_free(monkeypatch, tmp_path):
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.setattr(LicenseManager, "get_tier", lambda self: LicenseTier.FREE)

    io = DummyIO()
    cmds = Commands(io=io, coder=None)
    cmds.cmd_examples("pro")

    assert not io.assistant
    assert any("PRO examples" in o for o in io.outputs)


def test_examples_pro_fetches_for_pro(monkeypatch, tmp_path):
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.setattr(LicenseManager, "get_tier", lambda self: LicenseTier.PRO)
    monkeypatch.setattr(LicenseManager, "fetch_pro_examples_markdown", lambda self: "# PRO")

    io = DummyIO()
    cmds = Commands(io=io, coder=None)
    cmds.cmd_examples("pro")

    assert io.assistant
    assert io.assistant[0].startswith("# PRO")
