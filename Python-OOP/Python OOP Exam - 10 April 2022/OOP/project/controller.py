class Controller:
    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    @staticmethod
    def find_player(name, players):

        for player in players:

            if player.name == name:
                return player

    def add_player(self, *players):
        added_player_names = []

        for player in players:

            if player not in self.players:
                self.players.append(player)
                added_player_names.append(player.name)

        return f"Successfully added: {', '.join(added_player_names)}"

    def add_supply(self, *supplies):
        [self.supplies.append(supply) for supply in supplies]

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.find_player(player_name, self.players)

        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        if not player:
            return

        if sustenance_type not in ["Food", "Drink"]:
            return

        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(index)

                if player.stamina + supply.energy > 100:
                    player.stamina = 100

                else:
                    player.stamina += supply.energy

                return f"{player.name} sustained successfully with {supply.name}."

        raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self.find_player(first_player_name, self.players)
        second_player = self.find_player(second_player_name, self.players)

        sorted_players = sorted([first_player, second_player], key=lambda x: x.stamina)

        message_zero_stamina_players = []

        for player in sorted_players:

            if player.stamina == 0:
                message_zero_stamina_players.append(f"Player {player.name} does not have enough stamina.")

        if message_zero_stamina_players:
            return "\n".join(message_zero_stamina_players)

        if sorted_players[1].stamina - sorted_players[0].stamina / 2 <= 0:
            winner = sorted_players[0].name

            return f"Winner: {winner}"
        else:
            sorted_players[1].stamina -= sorted_players[0].stamina / 2

        if sorted_players[0].stamina - sorted_players[1].stamina / 2 <= 0:
            winner = sorted_players[1].name

            return f"Winner: {winner}"
        else:
            sorted_players[0].stamina -= sorted_players[1].stamina / 2

        new_sorted_list = sorted([first_player, second_player], key=lambda x: -x.stamina)

        winner = new_sorted_list[0].name

        return f"Winner: {winner}"

    def next_day(self):

        for player in self.players:
            damage = player.age * 2

            if player.stamina - damage < 0:
                player.stamina = 0
            else:
                player.stamina -= damage

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        players = "\n".join([str(player) for player in self.players])
        supplies = "\n".join([supply.details() for supply in self.supplies])

        return f"{players}\n{supplies}"
