class Player:
    def __init__(self, name, number, age, ppg):
        self.name = name
        self.number = number
        self.age = age
        self.ppg = ppg

    def get_ppg(self):
        return self.ppg


class Roster:
    def __init__(self, name, max_players):
        self.name = name
        self.max_players = max_players
        self.players = []
        self.is_active = False

    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)
            return True
        else:
            return False

    def get_average_ppg(self):
        value = 0
        for player in self.players:
            value += player.get_ppg()
        return value / len(self.players)


p = Player("Jaylen Brown", 7, 24, 46)
p2 = Player("Jayson Tatum", 0, 23, 21)
p3 = Player("Robert Williams", 46, 22, 15)

celtics = Roster("Boston Celtics", 17)
celtics.add_player(p)
celtics.add_player(p2)
celtics.add_player(p3)
print(celtics.get_average_ppg())
