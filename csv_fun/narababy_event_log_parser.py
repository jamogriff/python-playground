import csv
from .dtos.abstract_csv_row import AbstractCSVRow
from .dtos.narababy_bottle_feed_row import NarababyBottleFeedRow
from .dtos.narababy_diaper_row import NarababyDiaperRow
from .narababy_event_type import NarababyEventType
from .parse_results import ParseResults

class NarababyEventLogParser:

    def parse(self, csv_file_path: str) -> ParseResults:
        # TODO check that it is a CSV
        csv_attributes = self._get_csv_attributes(csv_file_path)

        with open(csv_file_path, "r") as f:
            reader = csv.reader(f, csv_attributes['dialect'])

            if csv_attributes['has_header']:
                header = next(reader)
                print(f"Header: {header}")

            feeds: list[NarababyBottleFeedRow] = []
            diaper_changes: list[NarababyDiaperRow] = []
            row_count = 0
            for row in reader:
                if EventType.BOTTLE_FEED.value in row[0]:
                    feed = NarababyBottleFeedRow()
                    self._populate_event_row(feed, row)
                    feeds.append(feed)
                elif EventType.DIAPER.value in row[0]:
                    diaper = NarababyDiaperRow()
                    self._populate_event_row(diaper, row)
                    diaper_changes.append(diaper)

                row_count += 1

            print("----------------")
            print(f"{len(feeds)} feeds")
            print(f"{len(diaper_changes)} diaper changes")
            print(f"{row_count} total rows processed")
            print("----------------")

            return ParseResults(feeds, diaper_changes, row_count)

    def _populate_event_row(self, event_row: AbstractEventRow, csv_row: list[str]):
        for column_index, attr in event_row.column_attribute_map.items():
            setattr(event_row, attr, csv_row[column_index])

    def _get_csv_attributes(self, csv_file_path: str) -> dict[str, csv.Dialect | bool]:
        csv_sniffer = csv.Sniffer()
        with open(csv_file_path, "r") as f:
            sample = f.read(1024)

        return {
            'dialect': csv_sniffer.sniff(sample),
            'has_header':csv_sniffer.has_header(sample)
        }


