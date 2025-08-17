from enum import Enum


class VolumeUnit(Enum):
    """Unit of volume (e.g. mL, OZ)."""

    MILLILITER = "ML"
    OUNCE = "FLOZ"

    @classmethod
    def try_from(cls, value: str) -> VolumeUnit | None:
        try:
            return cls(value)
        except ValueError:
            return None
