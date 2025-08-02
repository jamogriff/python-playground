import time
from jamolib.models.book import Book
from jamolib.models.user import User


class Checkout:
    """Many-to-many between users and books to log\
       when a checkout occurred and whether a given book\
       has been returned."""

    def __init__(self, user: User, book: Book):
        self._user = user
        self._book = book
        self.checked_out = time.time()
        self.returned: None | float = None
        self.is_returned = False

    def __str__(self) -> str:
        return f"{self._user.name} checked out {self._book.title} at {self.checked_out}"

    def __repr__(self) -> str:
        return f"Checkout(user={self._user}, book={self._book}, checked_out={self.checked_out}, returned={self.returned}, is_returned={self.is_returned})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Checkout):
            return NotImplemented
        return self._user.name == other.user.name and self._book.id == other.book.id

    @property
    def user(self) -> User:
        return self._user

    @property
    def book(self) -> Book:
        return self._book
