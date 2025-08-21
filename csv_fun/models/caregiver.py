from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Caregiver(Base):
    """An individual providing services to baby."""

    __table_name__ = "caregiver"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    feeds: Mapped[List["MilkFeed"]] = relationship(back_populates="caregiver")
    diaper_changes: Mapped[List["DiaperChange"]] = relationship(back_populates="caregiver")
    pumps: Mapped[List["Pump"]] = relationship(back_populates="caregiver")

    def __init__(self, name: str):
        self.name = name
