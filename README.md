A Python CLI for finding the most active cookie(s) on a given UTC date from a cookie log CSV.

## Quick Start

### Prerequisites

- Python 3.10+ (or any version supporting `datetime.fromisoformat` and `date.fromisoformat`)

### Run the program

```bash
./most_active_cookie cookie_log.csv -d 2018-12-09
```

or:

```bash
python3 most_active_cookie cookie_log.csv -d 2018-12-09
```

If needed, make the script executable:

```bash
chmod +x most_active_cookie
```

## Input / Output

Command:

```bash
./most_active_cookie <cookie_log.csv> -d <YYYY-MM-DD>
```

Input contract:

- CSV rows are expected in descending timestamp order (newest first).
- Header is expected as `cookie,timestamp`.
- `cookie` is treated as an opaque string.
- `timestamp` is expected to be ISO 8601 (for example `2018-12-09T14:19:00+00:00`).
- `-d` is interpreted as a UTC date.

Output contract:

- Prints the most active cookie(s) for the requested date to stdout.
- If multiple cookies tie for max count, prints all tied cookies, one per line.
- Tie order follows first-seen order in the file for that date.
- Prints nothing when there are no rows for the requested date.

## Testing

Run:

```bash
pytest -q
```

Current test coverage validates:

- Various prompts on different CSVs
- Tie handling
- Single-row CSV files
- CSV Files without extension
- Empty CSV file

Adding new tests:

- Add a CSV fixture under `tests/sample_csv_logs/`.
- Keep fixture rows in descending timestamp order to match runtime assumptions.
- Reuse the same two-column shape used by current fixtures: `cookie,timestamp`.
- Add a tuple to `TEST_CASES_VALID_CSV_INPUT` in `tests/test_most_active_cookie.py`:
  - `(fixture_path, date_arg, expected_stdout)`
- Format `expected_stdout` exactly as the CLI prints it (newline-separated values, no trailing newline).

Example:

```python
(f"{tf}/my_case.csv", "2018-12-09", "cookieA\ncookieB")
```

## Design

- `build_parser()` isolates command line parsing concerns.
- `get_reader()` encapsulates CSV header handling.
- `get_most_active_cookies()` contains the core domain logic and is unit-test friendly.
- The algorithm is linear over the scanned section of the file:
  - **Time complexity:** `O(n)` in scanned rows
  - **Space complexity:** `O(k)` for distinct cookies on the requested day
- Because rows are sorted descending by timestamp, scanning stops early when a row is older than the target date.

## Project Layout

- `most_active_cookie` - executable script and core logic
- `tests/test_most_active_cookie.py` - Command line integration-style tests
- `tests/sample_csv_logs/` - CSV files covering normal and edge scenarios

## Potential Extensions

- Optimize for repeated queries on the same dataset (e.g. ingest into SQLite with an index on the timestamp's date)
- Optimize for very large files on a single query (e.g. binary-search the start of the target date, since input is sorted descending by timestamp)
- Strict CSV schema validation and explicit error reporting for malformed rows
- Configurable handling for malformed rows (skip with warning or fail fast)
- Explicit exit code mapping for argument errors, file I/O errors and malformed input rows
