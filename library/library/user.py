from .abstract_borrower import AbstractBorrower

class User(AbstractBorrower):

    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def __str__(self) -> str:
        return f'{self._name}'

    def __repr__(self) -> str:
        return f'User(name={self._name})'

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self._name == other.name

    @property
    def name(self) -> str:
        return self._name
