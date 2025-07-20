from unittest import TestCase
from library.book import Book, InventoryItem

class TestBook(TestCase):

    def test_book_properties(self):
        book = Book('Gone With the Wind: A Meditation on Winning', 'Charles Barkley')

        self.assertEqual(book.title, 'Gone With the Wind: A Meditation on Winning')
        self.assertEqual(book.author, 'Charles Barkley')

    def test_inventory_items(self):
        book = Book('The Bible', 'Joshua')
        inventory_items = [InventoryItem(n, book) for n in range(8)]

        for item in inventory_items:
            book.add_inventory_item(item)

        self.assertEqual(len(book.inventory_items), 8)

