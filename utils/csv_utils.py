from datetime import timedelta, date, datetime

def convert_date_to_week_range(date_to_convert: str) -> str:
    date_obj = datetime.strptime(date_to_convert, '%m/%d/%Y')
    start_of_week = date_obj - timedelta(days=date_obj.weekday())
    return start_of_week.strftime('%m/%d/%Y')

def parse_date(date_str: str) -> datetime:
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)

def parse_to_date_only(date_and_hour: datetime) -> date:
    date_format = '%m/%d/%Y'
    return date_and_hour.strftime(date_format)