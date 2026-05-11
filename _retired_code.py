from bisect import bisect_left, bisect_right
from datetime import datetime
from typing import Iterator

def get_day_cookies_bin_search(cookie_log_reader : Iterator[list[str]], date : datetime.date) -> list[str]:
    next(cookie_log_reader) # skip header line
    cookie_dates_asc_order = [col[::-1] for col in zip(*cookie_log_reader)]
    cookies, dates = cookie_dates_asc_order
    
    str_to_date = lambda s: datetime.fromisoformat(s).date()
    first_valid_index = bisect_left(dates, date, key=lambda d: str_to_date(d))
    last_valid_index = bisect_right(dates, date, key=lambda d: str_to_date(d), lo=first_valid_index) - 1

    valid_cookies_desc_order = cookies[first_valid_index : last_valid_index + 1][::-1]
    return valid_cookies_desc_order