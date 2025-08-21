from __future__ import annotations
import datetime
from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, ForeignKey
from ..dtos.narababy_diaper_row import NarababyDiaperRow
from ..utils import datetime_utils as date
from .caregiver import Caregiver
from .base import Base


class DiaperChange(Base):
    """An occurrance of a baby soiling themselves and getting cleaned."""

    __table_name__ = "diaper_change"

    id: Mapped[int] = mapped_column(primary_key=True)
    caregiver_id: Mapped[int] = mapped_column(ForeignKey("caregiver.id"))
    datetime: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_poop: Mapped[bool] = mapped_column(Boolean)
    is_pee: Mapped[bool] = mapped_column(Boolean)

    caregiver: Mapped[Caregiver] = relationship(back_populates="diaper_changes")

    def __init__(
        self,
        caregiver: Caregiver,
        datetime: datetime.datetime,
        is_poop: bool,
        is_pee: bool,
    ):
        self.caregiver = caregiver
        self.datetime = datetime
        self.is_poop = is_poop
        self.is_pee = is_pee

    @classmethod
    def from_narababy_diaper_row(cls, narababy_row: NarababyDiaperRow) -> DiaperChange:
        return cls(
            Caregiver(narababy_row.caregiver),
            date.create_date_from_narababy_event(
                narababy_row.datetime, narababy_row.timezone
            ),
            "Dirty" in narababy_row.description if narababy_row.description else False,
            "Wet" in narababy_row.description if narababy_row.description else False,
        )
