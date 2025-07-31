import time
from .book import Book
from .user import User
from .checkout import Checkout

class Library:

    def __init__(self, name: str):
        self._name = name
        self._users = []
        self._books = []
        self._checkouts = []

    def __str__(self) -> str:
        return f'{self._name}: {len(self._users)} users, {len(self._books)} books, {len(self._checkouts)} checkouts'

    def __repr__(self) -> str:
        return f'Library(name={self._name}, users={self._users}, books={self._books}, checkouts={self._checkouts})'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Library):
            return NotImplemented
        return self._name == other.name

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

    def search_catalog(self, *, query: str = None, sort_by: str = 'title', order: str = 'desc') -> list:
        # Return early if invalid sort method passed
        # Can't use callable() function in conjunction because apparently the 
        # book properties aren't callable?
        if not hasattr(self._books[0], sort_by):
            raise RuntimeError('Invalid sorting method encountered')

        # Aggregate books by ISBN (i.e. only return a single book if that book has multiple copies)
        # TODO: definitely more Pythonic way to accomplish this
        isbns_encountered = []
        aggregated_books = []
        for book in self._books:
            if book.isbn not in isbns_encountered:
                aggregated_books.append(book)
                isbns_encountered.append(book.isbn)


        if (order != 'desc'):
            aggregated_books.sort(key=lambda b: getattr(b, sort_by), reverse=True)
        else:
            aggregated_books.sort(key=lambda b: getattr(b, sort_by))

        return aggregated_books

    def checkout(self, user: User, book: Book):
        if (self.is_book_checked_out(book)):
            raise RuntimeError('This book is currently checked out')

        self._checkouts.append(Checkout(user, book))

    def return_book(self, book: Book):
        if (not self.is_book_checked_out(book)):
            raise RuntimeError('This book is already in the possession of the library')

        most_recent_book_checkout = self._get_most_recent_checkout(book)
        most_recent_book_checkout.returned = time.time()
        most_recent_book_checkout.is_returned = True

    def is_book_checked_out(self, book: Book) -> bool:
        recent_checkouts = self._sort_checkouts_by_most_recent()
        most_recent_book_checkout = self._get_most_recent_checkout(book)

        if (most_recent_book_checkout == None):
            return False

        return not most_recent_book_checkout.is_returned

    def _get_most_recent_checkout(self, book: Book) -> Book | None:
        recent_checkouts = self._sort_checkouts_by_most_recent()
        # TODO review this incantation
        return next((c for c in recent_checkouts if c.book == book), None)

    def _sort_checkouts_by_most_recent(self) -> list:
        return sorted(self._checkouts, key=lambda c: c.checked_out, reverse=True)


