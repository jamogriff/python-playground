import datetime
from .dtos.narababy_pump_row import NarababyPumpRow
from .datetime_service import DatetimeService
from .caregiver import Caregiver

class Pump:
    """An occurrance of pumping milk."""

    def __init__(self, caregiver: Caregiver, datetime: datetime.datetime):
        self.caregiver = caregiver
        self.datetime = datetime

    @classmethod
    def from_narababy_pump_row(cls, narababy_row: NarababyPumpRow) -> Pump:
        return cls(
            Caregiver(narababy_row.caregiver),
            DatetimeService.get_from_narababy_event(narababy_row.datetime, narababy_row.timezone)
        )
