import datetime

def current_date_time_str() -> str:
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")