class Leaderboard:
    """The Leaderboard class houses game statistics that are saved from round to round.
    
    :param players: a list of players from whom to construct the leaderboard
    :type players: [class:`Player`]

    :ivar entires: a list of tuples (class:`Player1, integer), where integer represents wins
    :ivar round_count: integer tracking the number of rounds played

    :return: Returns a new instance of the Leaderboard
    :rtype: :class`Leaderboard`
    """
    
    def __init__(self, players):
        self.entries = [(player, 0) for player in players]
        self.round_count = 0

    def update_standings(self):
        """Updates the leaderboard standings with the new win values at the end of the round.
        """
        for entry in self.entries:
            entry = (entry[0], entry[0].wins)

    def print_leaderboard(self):
        """Prints the leaderboard standings in order from most wins to least wins.
        """
        print(f"{self.round_count} round(s) have been played!\n")
        print(f"The current standings are: \n")

        sorted_leaderboard = sorted(self.entries, key=lambda entry: entry[0].wins, reverse=True)
        for i, entry in enumerate(sorted_leaderboard):
            print(f"{i+1}. {entry[0].name} ({entry[0].wins} win(s))\n")

    