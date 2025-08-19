from .narababy_event_row import NarababyEventRow


class NarababyPumpRow(NarababyEventRow):
    row_identifier: str = "Pump"

    def __str__(self) -> str:
        return f"{self.datetime} by {self.caregiver}"

    def __repr__(self) -> str:
        return f"NarababyPumpRow(datetime={self.datetime}, caregiver={self.caregiver})"

    @property
    def column_attribute_map(self) -> dict[int, str]:
        return super().column_attribute_map
