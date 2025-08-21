from __future__ import annotations
import datetime
from sqlalchemy import Enum, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from ..dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .caregiver import Caregiver
from ..utils import datetime_utils as date
from ..utils import volume_utils as vol
from .base import Base


class MilkFeed(Base):
    """An event where a baby consumed milk."""

    __tablename__ = "feed"

    id: Mapped[int] = mapped_column(primary_key=True)
    caregiver_id: Mapped[int] = mapped_column(ForeignKey("caregiver.id"))
    volume: Mapped[float] = mapped_column(Float)
    unit: Mapped[vol.VolumeUnit] = mapped_column(Enum(vol.VolumeUnit, name="volume_unit"))
    datetime: Mapped[datetime.datetime] = mapped_column(DateTime)
    
    caregiver: Mapped[Caregiver] = relationship(back_populates="feeds")

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
