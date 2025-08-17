import code
from .narababy_event_log_parser import NarababyEventLogParser

if __name__ == "__main__":
    p = NarababyEventLogParser()
    file_path = 'csv_fun/export_jack.csv'
    local_namespace = dict(globals(), **locals())
    code.interact(banner="Lettuce Analyze", local=local_namespace)
