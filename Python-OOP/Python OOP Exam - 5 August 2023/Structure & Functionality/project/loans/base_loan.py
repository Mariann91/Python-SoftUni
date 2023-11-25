from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float) -> None:
        self.interest_rate = interest_rate
        self.amount = amount

    @property
    @abstractmethod
    def interest_rate_added_percent(self):
        ...

    def increase_interest_rate(self) -> None:
        self.interest_rate += self.interest_rate_added_percent
      
