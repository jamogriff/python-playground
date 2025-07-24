from .book import Book
from .user import User
from .checkout import Checkout

class Library:

    def __init__(self, name: str):
        self._name = name
        self._users = []
        self._books = []
        self._checkouts = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def users(self) -> list:
        return self._users

    @property
    def books(self) -> list:
        return self._books

    @property
    def checkouts(self) -> list:
        return self._checkouts

    def add_user(self, user: User):
        # TODO: check if already present
        self._users.append(user)

    def add_book(self, book: Book):
        # TODO: check if already present
        self._books.append(book)

    def search_catalog(self, query: str, order_by: str, sort_by: str) -> list:
        pass

    def checkout(self, user: User, book: Book):
        self._checkouts.append(Checkout(user, book))

    def is_book_checked_out(self, book: Book) -> bool:
        # TODO search in checkouts 
        pass


