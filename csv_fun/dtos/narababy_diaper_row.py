from .abstract_csv_row import AbstractCSVRow


class NarababyDiaperRow(AbstractCSVRow):
    row_identifier: str = "Diaper"
    description: str | None

    def __str__(self) -> str:
        return f"{self.datetime} by {self.caregiver}"

    def __repr__(self) -> str:
        return f"NarababyDiaperRow(description={self.description}, datetime={self.datetime}, timezone={self.timezone}, caregiver={self.caregiver})"

    @property
    def unique_column_attribute_map(self) -> dict[int, str]:
        return {10: "description"}
