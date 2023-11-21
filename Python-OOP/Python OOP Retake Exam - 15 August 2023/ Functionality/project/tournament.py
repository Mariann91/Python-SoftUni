from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str) -> str:

        try:
            equipment = Tournament.VALID_EQUIPMENT_TYPES[equipment_type]()

        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        try:
            team = Tournament.VALID_TEAM_TYPES[team_type](
                name=team_name,
                country=country,
                advantage=advantage,
            )

        except KeyError:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = [team for team in self.teams if team.name == team_name][0]

        for eq in reversed(self.equipment):

            if eq.__class__.__name__ == equipment_type and team.budget >= eq.price:
                self.equipment.remove(eq)
                team.equipment.append(eq)

                team.budget -= eq.price

                return f"Successfully sold {equipment_type} to {team_name}."

        raise Exception("Budget is not enough!")

    def remove_team(self, team_name: str):

        try:
            team = [team for team in self.teams if team.name == team_name][0]

        except IndexError:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for eq in self.equipment:

            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = [team for team in self.teams if team.name == team_name1][0]
        second_team = [team for team in self.teams if team.name == team_name2][0]

        if first_team.__class__.__name__ in Tournament.VALID_TEAM_TYPES and \
                second_team.__class__.__name__ in Tournament.VALID_TEAM_TYPES \
                and first_team.__class__.__name__ != second_team.__class__.__name__:

            raise Exception("Game cannot start! Team types mismatch!")

        first_team_score = first_team.advantage + sum(eq.protection for eq in first_team.equipment)
        second_team_score = second_team.advantage + sum(eq.protection for eq in second_team.equipment)

        if first_team_score == second_team_score:
            return "No winner in this game."

        if first_team_score > second_team_score:
            first_team.win()

            return f"The winner is {first_team.name}."

        second_team.win()

        return f"The winner is {second_team.name}."

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda x: x.wins, reverse=True)

        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:"
        ]

        [result.append(team.get_statistics()) for team in sorted_teams]

        return "\n".join(result)
