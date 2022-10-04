import datetime

def current_date_time_str() -> str:
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")

def datetime_add_microsecond_time_delta(
    x:datetime=datetime.datetime.now(),
    delta:int=0,
) -> datetime.datetime:
    return x + datetime.timedelta(milliseconds=delta)