from sqlalchemy import Column, Integer, Float
from .db import Base
from .abstract_entity import AbstractEntity

class BankAccount(Base, AbstractEntity):
    """A simple facsimile of a bank account where amounts can be withdrawn and deposited.\
    It is constructed with a starting balance and named configuration options."""

    __tablename__ = 'bank_account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Integer) # When to convert?
    interest_rate = Column(Float)
    max_transaction = Column(Integer)

    def __init__(self, opening_balance: float, *, interest_rate: float, max_transaction: float):
        self._assert_positive_amount(opening_balance)
        self._assert_positive_amount(interest_rate)
        self._assert_positive_amount(max_transaction)
        self._balance = opening_balance
        self._interest_rate = interest_rate
        self._max_transaction = max_transaction
        self._transactions = []; # TODO: make one-to-many and persist

    @property
    def balance(self):
        return self._balance

    @property
    def interest_rate(self):
        return self._interest_rate;

    @property
    def max_transaction(self):
        return self._max_transaction;

    @property
    def transactions(self):
        """Every withdrawal or deposit is logged as a transaction."""
        return self._transactions;

    @classmethod
    def make(cls, opening_balance: float, vip_account = False):
        """Factory method for creating accounts and to test out positional and keyword arguments.\
        Use vip_account flag to elevate account configuration."""
        if (vip_account):
            config = {'interest_rate': 0.01, 'max_transaction': 30000.00}
        else:
            config = {'interest_rate': 0.0015, 'max_transaction': 10000.00}

        return cls(opening_balance, **config)

    def withdraw(self, amount: float):
        self._assert_positive_amount(amount)
        self._assert_does_not_exceed_max_transaction(amount);
        new_balance = self._balance - amount
        self._assert_positive_amount(new_balance, 'Balance cannot be negative')
        self._balance = new_balance

    def deposit(self, amount: float):
        self._assert_positive_amount(amount)
        self._assert_does_not_exceed_max_transaction(amount);
        self._balance += amount

    def report_balance(self):
        """Method to print balance."""
        print(f'Remaining balance is {self._balance:.2f}')

    def _assert_positive_amount(self, amount: float, message = 'One cannot attempt a transaction with a negative amount.'):
        if amount < 0:
            raise ValueError(message)

    def _assert_does_not_exceed_max_transaction(self, amount: float):
        if (amount > self._max_transaction):
            raise ValueError(f'Transactions cannot exceed {self._max_transaction:.2f}')


