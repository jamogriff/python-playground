import datetime
from zoneinfo import ZoneInfo

class DatetimeService:

    @classmethod
    def get_from_narababy_event(cls, date: str, timezone: str) -> datetime.datetime:
        datetime_format = "%Y-%m-%d %H:%M:%S" 
        datetime = datetime.datetime.strptime(date, datetime_format)
        return datetime.replace(tzinfo=ZoneInfo(timezone))
