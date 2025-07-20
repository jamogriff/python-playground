from .abstract_borrower import AbstractBorrower

class User(AbstractBorrower):

    def __init__(self, name: str):
        super().__init__()
        self._name = name

    @property
    def name(self) -> str:
        return self._name
