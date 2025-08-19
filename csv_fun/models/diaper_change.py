from __future__ import annotations
import datetime
from ..dtos.narababy_diaper_row import NarababyDiaperRow
from ..utils import datetime_utils as date
from .caregiver import Caregiver

class DiaperChange:
    """An occurrance of a baby soiling themselves and getting cleaned."""

    def __init__(self, caregiver: Caregiver, datetime: datetime.datetime, is_poop: bool, is_pee: bool):
        self.caregiver = caregiver
        self.datetime = datetime
        self.is_poop = is_poop
        self.is_pee = is_pee

    @classmethod
    def from_narababy_diaper_row(cls, narababy_row: NarababyDiaperRow) -> DiaperChange:
        return cls(
            Caregiver(narababy_row.caregiver),
            date.create_date_from_narababy_event(narababy_row.datetime, narababy_row.timezone),
            narababy_row.description and 'Dirty' in narababy_row.description,
            narababy_row.description and 'Wet' in narababy_row.description
        )
