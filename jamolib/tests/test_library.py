from jamolib.tests.factories.library_factory import LibraryFactory
from unittest import TestCase


class TestLibrary(TestCase):
    # Why is this method camelcase... denoting special?
    def setUp(self):
        self.library = LibraryFactory.make("JeffCo Library")

    def test_catalog_search_results_are_aggregated(self):
        catalog = self.library.search_catalog()

        # 20 individual books and 1 book with 4 copies
        self.assertEqual(len(catalog), 21)

    def test_catalog_can_be_searched(self):
        catalog = self.library.search_catalog(query="Jamison Griffith")

        self.assertEqual(len(catalog), 1)

    def test_catalog_search_results_are_sorted(self):
        catalog_sorted_by_title = self.library.search_catalog()
        catalog_sorted_by_title_in_opposite_order = self.library.search_catalog(
            order="asc"
        )
        catalog_sorted_by_author = self.library.search_catalog(sort_by="author")

        self.assertTrue(
            ord(catalog_sorted_by_title[0].title[0])
            < ord(catalog_sorted_by_title[-1].title[0])
        )
        self.assertTrue(
            ord(catalog_sorted_by_title_in_opposite_order[0].title[0])
            > ord(catalog_sorted_by_title_in_opposite_order[-1].title[0])
        )
        self.assertTrue(
            ord(catalog_sorted_by_author[0].author[0])
            < ord(catalog_sorted_by_author[-1].author[0])
        )
