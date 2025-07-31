from unittest import TestCase
from jamolib.models.checkout import Checkout
from jamolib.models.user import User
from jamolib.models.book import Book
from jamolib.models.library import Library
from jamolib.tests.factories.library_factory import LibraryFactory

class TestCheckout(TestCase):

    def setUp(self):
        self.library = LibraryFactory.make('Arvada Heritage Library')

    def test_user_able_to_checkout(self):
        user = self.library.users[0]
        book = self.library.books[0]
        user_2 = self.library.users[1]

        self.assertFalse(self.library.is_book_checked_out(book))
        self.library.checkout(user, book)
        self.assertTrue(self.library.is_book_checked_out(book))

        # Another user cannot checkout that book while its checked out
        self.assertRaises(RuntimeError, self.library.checkout, user_2, book)

    def test_user_able_to_return_book(self):
        user = self.library.users[0]
        book = self.library.books[0]
        user_2 = self.library.users[1]

        self.library.checkout(user, book)

        # Another user cannot checkout that book while its checked out
        self.assertRaises(RuntimeError, self.library.checkout, user_2, book)

        self.library.return_book(book)
        self.library.checkout(user_2, book)


