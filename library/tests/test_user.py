from unittest import TestCase
from library.user import User

class TestUser(TestCase):

    def test_properties(self):
        user = User('Seymour Butts')

        self.assertEqual(user.name, 'Seymour Butts')
        self.assertEqual(user.get_borrowed_books(), [])

