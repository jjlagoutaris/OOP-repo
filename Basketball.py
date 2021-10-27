# class Player:
#     def __init__(self, name, number, age, ppg):
#         self.name = name
#         self.number = number
#         self.age = age
#         self.ppg = ppg
#
#     def get_ppg(self):
#         return self.ppg
#
#
# class Roster:
#     def __init__(self, name, max_players):
#         self.name = name
#         self.max_players = max_players
#         self.players = []
#         self.is_active = False
#
#     def add_player(self, player):
#         if len(self.players) < self.max_players:
#             self.players.append(player)
#             return True
#         else:
#             return False
#
#     def get_average_ppg(self):
#         value = 0
#         for player in self.players:
#             value += player.get_ppg()
#         return value / len(self.players)
#
#
# p = Player("Jaylen Brown", 7, 24, 46)
# p2 = Player("Jayson Tatum", 0, 23, 21)
# p3 = Player("Robert Williams", 46, 22, 15)
#
# celtics = Roster("Boston Celtics", 17)
# celtics.add_player(p)
# celtics.add_player(p2)
# celtics.add_player(p3)
# print(celtics.get_average_ppg())

# class Player:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#     def get_age(self):
#         return self.age
#
#
# class Team:
#     def __init__(self, name, max_players):
#         self.name = name
#         self.max_players = max_players
#         self.players = []
#
#     def add_player(self, player):
#         if len(self.players) < self.max_players:
#             self.players.append(player)
#             return True
#         return False
#
#     def get_avg_age(self):
#         value = 0
#         for player in self.players:
#             value += player.get_age()
#         if len(self.players) > 0:
#             return value / len(self.players)
#         else:
#             print("There are no players on this roster. ")
#
#
# p1 = Player("J L", 24, "SG")
# p2 = Player("J T", 23, "SF")
#
# t1 = Team("C", 2)
# t1.add_player(p1)
# t1.add_player(p2)
# print(t1.get_avg_age())


