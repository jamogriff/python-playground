import datetime
from .volume_unit import VolumeUnit
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .caregiver import Caregiver
from .datetime_service import DatetimeService

class MilkFeed:
    """An event where a baby consumed milk."""

    def __init__(self, volume: float, unit: VolumeUnit, caregiver: Caregiver, datetime: datetime.datetime):
        self.volume = volume
        self.unit = unit
        self.cargiver = caregiver
        self.datetime = datetime

    @classmethod
    def from_narababy_bottle_feed_row(cls, narababy_row: NarababyBottleFeedRow) -> self:
        #TODO need to sum all feed rows
        return cls(
            float(narababy_row.volume),
            VolumeUnit.try_from(narababy_row.unit),
            Caregiver(narababy_row.caregiver)
            DatetimeService.get_from_narababy_event(narababy_row.datetime, narababy_row.timezone)
        )
