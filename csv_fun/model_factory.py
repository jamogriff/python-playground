from .parse_results import ParseResults
from .dtos.narababy_event_row import NarababyEventRow
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .dtos.narababy_pump_row import NarababyPumpRow
from .dtos.narababy_diaper_row import NarababyDiaperRow
from .milk_feed import MilkFeed
from .diaper_change import DiaperChange
from .pump import Pump

class ModelFactory:
    """Class to create models with refined data from ParseResults"""

    def __init__(self, parse_results: ParseResults):
        self.data: list[NarababyEventRow] = parse_results.data

    def __call__(self) -> list[]:
        feeds: list[MilkFeed] = []
        diaper_changes: list[DiaperChange] = []
        pumps: list[Pump] = []
        for event in self.data:
            if event instanceof NarababyBottleFeedRow:
                feeds.append(MilkFeed.from_narababy_bottle_feed_row(event))
            elif event instanceof NarababyDiaperRow:
                diaper_changes.append(DiaperChange.from_narababy_diaper_row(event))
            elif event instanceof NarababyPumpRow:
                pumps.append(Pump.from_narababy_pump_row(event))

        return {
            'diapers': diaper_changes,
            'bottles': feeds,
            'pumps': pumps
        }




