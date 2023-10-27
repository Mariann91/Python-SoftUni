from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str) -> None:
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):

        for current_player in self.players:

            if current_player.name == player_name:

                self.players.remove(current_player)
                current_player.guild = Player.DEFAULT_GUILD

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):

        output = "\n".join([current_player.player_info() for current_player in self.players])

        return f"Guild: {self.name}\n" +\
               f"{output}"
      
