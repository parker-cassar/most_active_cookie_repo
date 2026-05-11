import subprocess
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
PROJECT_DIR = TESTS_DIR.parent
MOST_DAY_COOOKIE_SCRIPT = PROJECT_DIR / "most_day_cookie"


@pytest.mark.parametrize("fixture,date,expected", [
    (
        "tests/csv_fixtures/cookie_log.csv",
        "2018-12-08",
        "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n",
    ),
    (
        "tests/csv_fixtures/cookie_log.csv",
        "2018-12-09",
        "AtY0laUfhglK3lC7\n",
    ),
    (
        "tests/csv_fixtures/all_one_day.csv",
        "2018-12-09",
        "LpQ3uD7fZk2mWxNt\n",
    ),
    (
        "tests/csv_fixtures/all_tied_one_day.csv",
        "2018-12-08",
        "Tz7rBnGk4mVxLqP2\n3HjZcA8fDb6WuNpQ\nmK9vXqR2nPwL5sYt\n",
    ),
    (
        "tests/csv_fixtures/one_row.csv",
        "2018-12-09",
        "5UAVanZf6UtGyKVS\n",
    ),
    ("tests/csv_fixtures/empty.csv", "2018-12-09", "No cookies on 2018-12-09\n"),
    ("tests/csv_fixtures/empty_untyped", "2018-12-09", "No cookies on 2018-12-09\n"),
])
def test_cli_returns_most_active(fixture, date, expected):
    completed_process = subprocess.run([str(MOST_DAY_COOOKIE_SCRIPT), fixture, "-d", date], capture_output=True, text=True)
    output = completed_process.stdout
    
    # print(type(expected),type(output), output == expected, '\n', f"output={output} == expected={expected}")
    assert(output == expected)
    