from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    RACE_EXPENSES = 200_000

    first_sponsor = {
        1_000_000: [1],
        500_000: [2, 3]
    }

    second_sponsor = {
        100_000: [1, 2, 3, 4, 5],
        50_000: [6, 7]
    }

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        first_sponsor_money = self.calculate_sponsor_money(race_pos, MercedesTeam.first_sponsor)

        second_sponsor_money = self.calculate_sponsor_money(race_pos, MercedesTeam.second_sponsor)

        earned_money = first_sponsor_money + second_sponsor_money

        revenue = earned_money - MercedesTeam.RACE_EXPENSES
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
