import code
from .narababy_event_log_parser import NarababyEventLogParser
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .dtos.narababy_diaper_row import NarababyDiaperRow

if __name__ == "__main__":
    p = NarababyEventLogParser()
    file_path = "csv_fun/data/export_jack.csv"
    local_namespace = dict(globals(), **locals())
    code.interact(banner="Lettuce Analyze", local=local_namespace)
