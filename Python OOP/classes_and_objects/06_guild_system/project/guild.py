from player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            else:
                return f"Player {player.name} is in another guild."
        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        for member in self.players:
            if member.name == player_name:
                self.players.remove(member)
                member.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f'Guild: {self.name}']
        for member in self.players:
            result.append(Player.player_info(member))

        return "\n".join(result)
