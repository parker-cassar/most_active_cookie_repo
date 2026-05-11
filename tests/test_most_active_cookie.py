import subprocess
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
PROJECT_DIR = TESTS_DIR.parent
most_active_COOOKIE_SCRIPT = PROJECT_DIR / "most_active_cookie"

tf = "tests/csv_fixtures"
# (fixture_path, date, expected_output)
TEST_CASES = [
    (f"{tf}/cookie_log.csv", "2018-12-08", "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n"),
    (f"{tf}/cookie_log.csv", "2018-12-09", "AtY0laUfhglK3lC7\n"),
    (f"{tf}/all_one_day.csv", "2018-12-09", "LpQ3uD7fZk2mWxNt\n"),
    (f"{tf}/all_tied_one_day.csv", "2018-12-08", "Tz7rBnGk4mVxLqP2\n3HjZcA8fDb6WuNpQ\nmK9vXqR2nPwL5sYt\n"),
    (f"{tf}/one_row.csv", "2018-12-09", "5UAVanZf6UtGyKVS\n"),
    (f"{tf}/empty.csv", "2018-12-09", "No cookies on 2018-12-09\n"),
    (f"{tf}/empty_no_extension", "2018-12-09", "No cookies on 2018-12-09\n"),
]

@pytest.mark.parametrize("fixture,date,expected", TEST_CASES)
def test_cli_returns_most_active(fixture, date, expected):
    args = [str(most_active_COOOKIE_SCRIPT), fixture, "-d", date]
    completed_process = subprocess.run(args, capture_output=True, text=True)
    assert completed_process.returncode == 0, f"\n CLI crashed with error:\n{completed_process.stderr}"
    assert completed_process.stdout == expected