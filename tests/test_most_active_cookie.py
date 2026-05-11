import subprocess
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
PROJECT_DIR = TESTS_DIR.parent
most_active_COOOKIE_SCRIPT = PROJECT_DIR / "most_active_cookie"

ts = "tests/sample_csv_logs"
# (fixture_path, date, expected_output)
TEST_CASES_VALID_CSV_INPUT = [
    (f"{ts}/cookie_log.csv", "2018-12-08", "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG"),
    (f"{ts}/cookie_log.csv", "2018-12-09", "AtY0laUfhglK3lC7"),
    (f"{ts}/all_one_day.csv", "2018-12-09", "LpQ3uD7fZk2mWxNt"),
    (f"{ts}/all_tied_one_day.csv", "2018-12-08", "Tz7rBnGk4mVxLqP2\n3HjZcA8fDb6WuNpQ\nmK9vXqR2nPwL5sYt"),
    (f"{ts}/one_row.csv", "2018-12-09", "5UAVanZf6UtGyKVS"),
    (f"{ts}/empty.csv", "2018-12-09", ""),
    (f"{ts}/empty_no_extension", "2018-12-09", ""),
    (f"{ts}/empty_no_header(choosing_to_treat_as_valid).csv", "2018-12-09", ""),
]

@pytest.mark.parametrize("sample_csv_log,date,expected", TEST_CASES_VALID_CSV_INPUT)
def test_valid_csv_input(sample_csv_log, date, expected):
    args = [str(most_active_COOOKIE_SCRIPT), sample_csv_log, "-d", date]
    completed_process = subprocess.run(args, capture_output=True, text=True)
    assert completed_process.returncode == 0, f"\n Crashed with error:\n{completed_process.stderr}"
    assert completed_process.stdout == expected