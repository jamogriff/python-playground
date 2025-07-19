from .book import Book

class AbstractBorrower:

    def __init__(self):
        # TODO, make this a set
        self._books_borrowed = []

    def get_borrowed_books(self) -> list[Book]:
        return self._books_borrowed

    def borrow_book(self, book: Book):
        self._books_borrowed.append(book)

    def return_book(self, book: Book):
        # TODO find book and split by index
        pass
