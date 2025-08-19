from .parse_results import ParseResults
from .dtos.narababy_event_row import NarababyEventRow
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .dtos.narababy_pump_row import NarababyPumpRow
from .dtos.narababy_diaper_row import NarababyDiaperRow
from .models.milk_feed import MilkFeed
from .models.diaper_change import DiaperChange
from .models.pump import Pump

class ModelFactory:
    """Class to create models with refined data from ParseResults"""

    def __init__(self, parse_results: ParseResults):
        self.data: list[NarababyEventRow] = parse_results.data

    def __call__(self) -> dict[str, MilkFeed | DiaperChange | Pump]:
        feeds: list[MilkFeed] = []
        diaper_changes: list[DiaperChange] = []
        pumps: list[Pump] = []
        for event in self.data:
            if isinstance(event, NarababyBottleFeedRow):
                feeds.append(MilkFeed.from_narababy_bottle_feed_row(event))
            elif isinstance(event, NarababyDiaperRow):
                diaper_changes.append(DiaperChange.from_narababy_diaper_row(event))
            elif isinstance(event, NarababyPumpRow):
                pumps.append(Pump.from_narababy_pump_row(event))

        return {
            'diapers': diaper_changes,
            'bottles': feeds,
            'pumps': pumps
        }

