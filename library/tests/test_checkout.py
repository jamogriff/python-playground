from unittest import TestCase
from library.checkout import Checkout
from library.user import User
from library.book import Book
from library.library import Library
from tests.factories.library_factory import LibraryFactory

class TestCheckout(TestCase):

    def test_user_able_to_checkout(self):
        library = LibraryFactory.make('Arvada Heritage Library')
        user = library.users[0]
        book = library.books[0]
        user_2 = library.users[1]

        self.assertFalse(library.is_book_checked_out(book))
        library.checkout(user, book)
        self.assertTrue(library.is_book_checked_out(book))

        # Another user cannot checkout that book while its checked out
        self.assertRaises(RuntimeError, library.checkout, user_2, book)

    def test_user_able_to_return_book(self):
        library = LibraryFactory.make('Arvada Heritage Library')
        user = library.users[0]
        book = library.books[0]
        user_2 = library.users[1]

        library.checkout(user, book)

        # Another user cannot checkout that book while its checked out
        self.assertRaises(RuntimeError, library.checkout, user_2, book)

        library.return_book(book)
        library.checkout(user_2, book)


