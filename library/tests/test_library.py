from tests.factories.library_factory import LibraryFactory
from unittest import TestCase

#TODO: leverage set_up method to bootstrap library instance
class TestLibrary(TestCase):
    def test_catalog_search_results_are_aggregated(self):
        library = LibraryFactory.make('Jeffco')
        catalog = library.search_catalog()

        # 20 individual books and 1 book with 4 copies
        self.assertEqual(len(catalog), 21)

    def test_catalog_can_be_searched(self):
        library = LibraryFactory.make('Jeffco')
        catalog = library.search_catalog(query='Griffith')

        self.assertEqual(len(catalog), 1)

    def test_catalog_search_results_are_sorted(self):
        library = LibraryFactory.make('Jeffco')
        catalog_sorted_by_title = library.search_catalog()
        catalog_sorted_by_title_in_opposite_order = library.search_catalog(order='asc')
        catalog_sorted_by_author = library.search_catalog(sort_by='author')

        # TODO: I think you could use the next iterator to assert the entirety of each lists order. Likely cleaner than the following

        self.assertTrue(ord(catalog_sorted_by_title[0].title[0]) < ord(catalog_sorted_by_title[-1].title[0]))
        self.assertTrue(ord(catalog_sorted_by_title_in_opposite_order[0].title[0]) > ord(catalog_sorted_by_title_in_opposite_order[-1].title[0]))
        self.assertTrue(ord(catalog_sorted_by_author[0].author[0]) < ord(catalog_sorted_by_author[-1].author[0]))
