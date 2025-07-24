import uuid

class Book:
    """Represents a physical/digital book that is able to be\
       transfered between a user and a library."""

    def __init__(self, isbn: str, title: str, author: str):
        self._id = uuid.uuid4()
        self._isbn = isbn
        self._title = title
        self._author = author

    @property
    def id(self) -> str:
        return self._id

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author
