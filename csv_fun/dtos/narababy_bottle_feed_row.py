from .abstract_csv_row import AbstractCSVRow

class NarababyBottleFeedRow(AbstractCSVRow):
    volume: float
    unit: str
    datetime: str
    timezone: str
    caregiver: str

    def __str__(self) -> str:
        return f"{self.volume} {self.unit} at {self.datetime} by {self.caregiver}"

    def __repr__(self) -> str:
        return f"NarababyBottleFeedRow(volume={self.volume}, unit={self.unit}, datetime={self.datetime}, caregiver={self.caregiver})"

    @property
    def column_attribute_map(self) -> dict[int, str]:
        return {
            2: 'datetime',
            4: 'caregiver',
            7: 'timezone',
            8: 'volume',
            9: 'unit'
        }

