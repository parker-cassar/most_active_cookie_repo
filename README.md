# Most Active Cookie

Small Python CLI for finding the most active cookie(s) on a given UTC date from a cookie log CSV.

## Problem

Given a CSV file in this format (sorted in descending timestamp order):

```csv
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
...

cookie: cookie identifier (treated as an opaque string)
timestamp: ISO 8601 datetime string with UTC offset (for example, 2018-12-09T14:19:00+00:00)

Return the cookie(s) that appear most often for a requested day.

If there is a tie, print all tied cookies, one per line. Program prints cookies in first timestamp ascending order.

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

## Testing

Run:

```bash
pytest -q
```

Current test coverage validates:

- canonical prompt example behavior
- tie handling
- single-row input
- empty file behavior
- files without extension
- empty file without header

## Design Notes

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
- `tests/csv_fixtures/` - fixture files covering normal and edge scenarios

## Extension Ideas

Potential enhancements:

- strict CSV schema validation and explicit error reporting for malformed rows
- optional tie ordering mode (for example alphabetic sort) for stable output
- configurable handling for malformed rows (skip with warning or fail fast)
- explicit exit code mapping for argument errors, file I/O errors and malformed input rows