from .abstract_csv_row import AbstractCSVRow


class NarababyDiaperRow(AbstractCSVRow):
    row_identifier: str = "Diaper"

    description: str | None
    datetime: str
    timezone: str
    caregiver: str

    def __str__(self) -> str:
        return f"{self.datetime} by {self.caregiver}"

    def __repr__(self) -> str:
        return f"NarababyDiaperRow(description={self.description}, datetime={self.datetime}, timezone={self.timezone}, caregiver={self.caregiver})"

    # @property
    # def row_identifier(self) -> str:
    #     return 'Diaper'

    @property
    def column_attribute_map(self) -> dict[int, str]:
        return {2: "datetime", 4: "caregiver", 7: "timezone", 10: "description"}
