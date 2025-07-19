from unittest import TestCase
from library.book import Book

class TestBook(TestCase):

    def test_properties(self):
        book = Book('Gone With the Wind: A Meditation on Winning', 'Charles Barkley')

        self.assertEqual(book.title, 'Gone With the Wind: A Meditation on Winning')
        self.assertEqual(book.author, 'Charles Barkley')
        self.assertFalse(book.checked_out)

