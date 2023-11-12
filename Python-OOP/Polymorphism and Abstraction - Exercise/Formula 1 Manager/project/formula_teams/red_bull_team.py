from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    RACE_EXPENSES = 250_000

    first_sponsor = {
        1_500_000: [1],
        800_000: [2]
    }

    second_sponsor = {
        20_000: [1, 2, 3, 4, 5, 6, 7, 8],
        10_000: [9, 10]
    }

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        first_sponsor_money = self.calculate_sponsor_money(race_pos, RedBullTeam.first_sponsor)

        second_sponsor_money = self.calculate_sponsor_money(race_pos, RedBullTeam.second_sponsor)

        earned_money = first_sponsor_money + second_sponsor_money

        revenue = earned_money - RedBullTeam.RACE_EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
