from dataclasses import dataclass
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .dtos.narababy_diaper_row import NarababyDiaperRow

@dataclass
class ParseResults:
    feeds: list[NarababyBottleFeedRow]
    diaper_changes: list[NarababyDiaperRow]
    rows_processed: int
