from __future__ import annotations
import datetime
from ..dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .caregiver import Caregiver
from ..utils import datetime_utils as date
from ..utils import volume_utils as vol


class MilkFeed:
    """An event where a baby consumed milk."""

    def __init__(
        self,
        volume: float,
        unit: vol.VolumeUnit,
        caregiver: Caregiver,
        datetime: datetime.datetime,
    ):
        self.volume = volume
        self.unit = unit
        self.caregiver = caregiver
        self.datetime = datetime

    @classmethod
    def from_narababy_bottle_feed_row(
        cls, narababy_row: NarababyBottleFeedRow
    ) -> MilkFeed:
        return cls(
            narababy_row.get_total_metric_volume(),
            vol.VolumeUnit.MILLILITER,
            Caregiver(narababy_row.caregiver),
            date.create_date_from_narababy_event(
                narababy_row.datetime, narababy_row.timezone
            ),
        )
