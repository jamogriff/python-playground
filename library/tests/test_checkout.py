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

        library.checkout(user, book)
        # TODO check against checkout to ensure transfers

        # TODO check syntax
        #self.assertRaises(RuntimeError, library.checkout_book, user_2, book)




