import uuid


class Book:
    """Represents a physical/digital book that is able to be\
       transfered between a user and a library."""

    def __init__(self, isbn: str, title: str, author: str):
        self._id = uuid.uuid4()
        self._isbn = isbn
        self._title = title
        self._author = author

    def __str__(self) -> str:
        return f"{self._title} by {self._author} ({self._id})"

    def __repr__(self) -> str:
        return f"Book(id={self._id}, isbn={self._isbn}, title={self._title}, author={self._author})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self._id == other.id

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
