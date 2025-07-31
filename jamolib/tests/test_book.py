from unittest import TestCase
from uuid import UUID
from jamolib.models.book import Book

class TestBook(TestCase):

    def test_book_properties(self):
        book = Book('123-2938-29283', 'Gone With the Wind: A Meditation on Winning', 'Charles Barkley')

        self.assertIsInstance(book.id, UUID)
        self.assertEqual(book.isbn, '123-2938-29283')
        self.assertEqual(book.title, 'Gone With the Wind: A Meditation on Winning')
        self.assertEqual(book.author, 'Charles Barkley')

