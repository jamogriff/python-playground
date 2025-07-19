import unittest
from jamobank.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_account_properties(self):
        account = BankAccount.make(100)
        self.assertEqual(account.balance, 100)
        self.assertEqual(account.interest_rate, 0.0015)
        self.assertEqual(account.max_transaction, 10000)

        high_yield_account = BankAccount.make(10000, True)
        self.assertEqual(high_yield_account.balance, 10000)
        self.assertEqual(high_yield_account.interest_rate, 0.01)
        self.assertEqual(high_yield_account.max_transaction, 30000)

    def test_account_withdrawal(self):
        account = BankAccount.make(1000)
        account.withdraw(500)
        self.assertEqual(account.balance, 500.00)

    def test_errors_raised_for_invalid_withdrawal(self):
        account = BankAccount.make(1000)
        self.assertRaises(ValueError, account.withdraw, 2200)
        self.assertRaises(ValueError, account.withdraw, -200)

    def test_account_deposit(self):
        account = BankAccount.make(1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500.00)

    def test_errors_raised_for_invalid_deposit(self):
        account = BankAccount.make(1000)
        self.assertRaises(ValueError, account.deposit, 6632200)



if __name__ == '__main__':
    unittest.main()

