class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        player_name = player.username
        usernames = [p.username for p in self.players]
        if player_name in usernames:
            raise ValueError(f"Player {player_name} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player_username):
        if player_username == "":
            raise ValueError("Player cannot be an empty string!")
        player = self.find(player_username)
        self.players.remove(player)
        self.count -= 1

    def find(self, username):
        return [p for p in self.players if p.username == username][0]
