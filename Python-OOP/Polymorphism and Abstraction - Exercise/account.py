from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount):
        self._transactions.append(transaction_amount)
        account_balance = self.amount + sum(self._transactions)

        if account_balance < 0:
            raise ValueError("sorry cannot go in debt!")

        return f"New balance: {account_balance}"

    def add_transaction(self, amount):

        if not isinstance(amount, int):
            raise ValueError( "please use int for amount")

        self._transactions.append(amount)
        account_balance = self.amount + sum(self._transactions)

        if account_balance < 0:
            raise ValueError("sorry cannot go in debt!")

        return f"New balance: {account_balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):

        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, account_two):
        result_account_name = f"{self.owner}&{account_two.owner}"
        result_account_amount = self.amount + account_two.amount

        new_account = Account(owner=result_account_name, amount=result_account_amount)
        new_account._transactions.extend(self._transactions)
        new_account._transactions.extend(account_two._transactions)

        return new_account
      
