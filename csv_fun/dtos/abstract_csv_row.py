from abc import ABC, abstractmethod

class AbstractCSVRow(ABC):

    @property
    @abstractmethod
    def column_attribute_map(self) -> dict[int, str]:
        """A data map between a CSV column index and 
        the corresponding subclass attribute."""

        raise NotImplementedError("Subclasses must implement.")

