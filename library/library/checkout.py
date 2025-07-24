import time
from .book import Book
from .user import User

class Checkout:
    """Many-to-many between users and books to log\
       when a checkout occurred and whether a given book\
       has been returned."""

    def __init__(self, user: User, book: Book):
        self._user = user
        self._book = book
        self.checked_out = time.time()
        self.returned = None
        self.is_returned = False

    @property
    def user(self) -> User:
        return self._user

    @property
    def book(self) -> Book:
        return self._book
