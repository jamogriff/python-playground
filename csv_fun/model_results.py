from dataclasses import dataclass
from .models.milk_feed import MilkFeed
from .models.diaper_change import DiaperChange
from .models.pump import Pump


@dataclass
class ModelResults:
    bottles: list[MilkFeed]
    diapers: list[DiaperChange]
    pumps: list[Pump]
