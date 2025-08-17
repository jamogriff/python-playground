from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCSVRow(ABC):
    registry: dict[str, AbstractCSVRow] = {}

    # Subclasses must define this
    row_identifier: str

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
    def column_attribute_map(self) -> dict[int, str]:
        """A data map between a CSV column index and
        the corresponding subclass attribute."""

        raise NotImplementedError

    def hydrate_from_row(self, csv_row: list[str]) -> None:
        """Hydrates attributes of a subclass from a CSV row using its column_attribute_map."""

        for column_index, attr in self.column_attribute_map.items():
            setattr(self, attr, csv_row[column_index])
