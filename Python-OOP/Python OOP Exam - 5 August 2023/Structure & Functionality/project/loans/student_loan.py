from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self, interest_rate: float = 1.5, amount: float = 2000):
        super().__init__(interest_rate, amount)
        self.interest_rate = interest_rate
        self.amount = amount

    @property
    def interest_rate_added_percent(self):
        return 0.2
