import time
from .book import InventoryItem
from .user import User

class Checkout:
    """Many-to-many between users and book inventory items"""

    def __init__(self, user: User, inventory_item: InventoryItem):
        self._user = user
        self._inventory_item = inventory_item
        self.checked_out = time.time()
        self.returned = None
