from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1000)

    @property
    def win_team_advantage(self):
        return 115
