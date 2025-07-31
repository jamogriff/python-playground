from unittest import TestCase
from jamolib.models.user import User


class TestUser(TestCase):

    def test_properties(self):
        user = User("Seymour Butts")

        self.assertEqual(user.name, "Seymour Butts")
