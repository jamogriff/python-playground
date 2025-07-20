from __future__ import annotations # Used to avoid circular references/or classes not initialized yet
from dataclasses import dataclass

class Book:

    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
        self.inventory_items = []

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    def add_inventory_item(self, inventory_item: InventoryItem):
        self.inventory_items.append(inventory_item)


@dataclass
class InventoryItem:
    id: str
    book: Book

