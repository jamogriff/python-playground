class Library:

    def __init__(self, name: str):
        self._name = name
        self.users = []
        self.books = []

    @property
    def name(self) -> str:
        return self._name

    def search_catalog(self, query: str, order_by: str, sort_by: str) -> List:
        pass

    def check_out_book(self, user: User, book: Book)
        pass
