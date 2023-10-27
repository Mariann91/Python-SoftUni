from typing import Dict


class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost) -> str:

        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:

        output = "\n".join([f"==={skill} - {skill_mana}" for skill, skill_mana in self.skills.items()])

        return f"Name: {self.name}\n" + \
               f"Guild: {self.guild}\n" + \
               f"HP: {self.hp}\n" + \
               f"MP: {self.mp}\n" + \
               f"{output}\n"
      
