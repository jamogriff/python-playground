from __future__ import annotations
import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from ..dtos.narababy_pump_row import NarababyPumpRow
from ..utils import datetime_utils as date
from .caregiver import Caregiver
from .base import Base


class Pump(Base):
    """An occurrance of pumping milk."""

    __tablename__ = "pump"

    id: Mapped[int] = mapped_column(primary_key=True)
    caregiver_id: Mapped[int] = mapped_column(ForeignKey("caregiver.id"))
    datetime: Mapped[datetime.datetime] = mapped_column(DateTime)

    caregiver: Mapped[Caregiver] = relationship(back_populates="pumps")


    def __init__(self, caregiver: Caregiver, datetime: datetime.datetime):
        self.caregiver = caregiver
        self.datetime = datetime

    @classmethod
    def from_narababy_pump_row(cls, narababy_row: NarababyPumpRow) -> Pump:
        return cls(
            Caregiver(narababy_row.caregiver),
            date.create_date_from_narababy_event(
                narababy_row.datetime, narababy_row.timezone
            ),
        )
