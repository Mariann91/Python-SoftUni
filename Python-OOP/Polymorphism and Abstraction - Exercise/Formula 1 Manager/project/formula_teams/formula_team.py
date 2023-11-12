from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):

        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int) -> str:
        ...

    @staticmethod
    def calculate_sponsor_money(place, info):
        earned_money = 0

        for key, value in info.items():

            if place in value:
                earned_money += key

        return earned_money
