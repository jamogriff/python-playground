from dataclasses import dataclass
from .dtos.abstract_csv_row import AbstractCSVRow


@dataclass
class ParseResults:
    data: list[AbstractCSVRow]
    rows_processed: int
    time_elapsed: int
