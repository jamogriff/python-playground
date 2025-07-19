class Book:

    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
        self.checked_out = False

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    
