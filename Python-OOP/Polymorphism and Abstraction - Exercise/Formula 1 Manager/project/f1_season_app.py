from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):

        if team_name != "Red Bull" and team_name != "Mercedes":
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget=budget)

        if team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget=budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):

        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        team_with_better_pos = "Mercedes"

        if red_bull_pos < mercedes_pos:
            team_with_better_pos = "Red Bull"

        return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " \
               f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. {team_with_better_pos} " \
               f"is ahead at the {race_name} race."
