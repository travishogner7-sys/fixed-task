import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Prerequisite: the report must exist at /app/report.json, the exact path
    stated in instruction.md and declared in task.toml artifacts."""
    assert REPORT.exists(), "no /app/report.json found"


def test_report_is_valid_json_object():
    """Prerequisite: instruction.md requires 'a single JSON object' at that path."""
    assert isinstance(_load(), dict), "report.json is not a JSON object"


def test_required_keys_present():
    """Prerequisite: report.json must contain the three keys instruction.md's
    numbered criteria (1-3) define: total_requests, unique_ips, top_path."""
    assert {"total_requests", "unique_ips", "top_path"} <= _load().keys()


def test_total_requests_correct():
    """Criterion 1 (instruction.md): total_requests must equal the number of
    non-empty log lines (6)."""
    assert _load()["total_requests"] == 6


def test_unique_ips_correct():
    """Criterion 2 (instruction.md): unique_ips must equal the count of distinct
    client IP addresses, the first whitespace-separated field per line (3)."""
    assert _load()["unique_ips"] == 3


def test_top_path_correct():
    """Criterion 3 (instruction.md): top_path must equal the most-requested
    path across all requests ("/index.html")."""
    assert _load()["top_path"] == "/index.html"
