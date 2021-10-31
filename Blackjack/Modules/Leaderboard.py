class Leaderboard:
    def __init__(self, players):
        self.entries = [(player, 0) for player in players]
        self.round_count = 0

    def update_standings(self):
        for entry in self.entries:
            entry = (entry[0], entry[0].wins)

    def print_leaderboard(self):
        print(f"{self.round_count} round(s) have been played!\n")
        print(f"The current standings are: \n")
        sorted_leaderboard = sorted(self.entries, key=lambda entry: entry[1], reverse=True)
        for i, entry in enumerate(sorted_leaderboard):
            print(f"{i+1}. {entry[0].name} ({entry[0].wins} win(s))\n")

    