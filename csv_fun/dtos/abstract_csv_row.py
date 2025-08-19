from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCSVRow(ABC):
    registry: dict[str, AbstractCSVRow] = {}
    datetime: str
    timezone: str
    caregiver: str
    baby: str
    note: str
    row_identifier: str # Subclasses must define this

    SHARED_COLUMN_ATTRIBUTE_MAP: dict[int, str] = {
        1: "baby",
        2: "datetime",
        4: "caregiver",
        6: "note",
        7: "timezone"
    }

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "row_identifier"):
            raise TypeError(
                f"{cls.__name__} must define a class attribute 'row_identifier'."
            )
        AbstractCSVRow.registry[cls.row_identifier] = cls

    # Using property results in property objects as keys
    # in the registry, which at initial glance do not return
    # the string values they hold
    # @property
    # @abstractmethod
    # def row_identifier(self) -> str:
    #     """The row identifier in a CSV row that corresponds
    #     with a given subclass."""

    #     raise NotImplementedError

    @property
    @abstractmethod
    def unique_column_attribute_map(self) -> dict[int, str]:
        """Subclasses must define their own unique mappings between
        a CSV column index and their corresponding attribute."""

        raise NotImplementedError
        
    @property
    def column_attribute_map(self) -> dict[int, str]:
        """Merge subclass attribute maps with shared attribute map."""

        return {**self.SHARED_COLUMN_ATTRIBUTE_MAP, **self.unique_column_attribute_map}

    def hydrate_from_row(self, csv_row: list[str]) -> None:
        """Hydrates attributes of a subclass from a CSV row using its column_attribute_map."""

        for column_index, attr in self.column_attribute_map.items():
            setattr(self, attr, csv_row[column_index])
