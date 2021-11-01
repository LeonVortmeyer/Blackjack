#Leon Vortmeyer 10.31.2021

from Card import Card
from Computer import Computer
from Dealer import Dealer
from Human import Human
from Leaderboard import Leaderboard
from random import randint


class Game:
    """The Game class houses the highest level attributes and methods required to play a terminal-based game of blackjack

    :param human_player_count: the number of human players with which to instantiate the game, defaults to 1
    :type human_player_count: Integer
    :param computer_player_count: the number of human players with which to instantiate the game, defaults to 1
    :type computer_player_count: Integer

    :ivar cards: An array of class:`Card` objects that at instantiation represent the full 52 cards in a standard deck
    :ivar human_players: An array of class:`Human` objects representing all human players
    :ivar computer_players: An array of class:`Computer` objects representing all computer players
    :ivar leaderboard: An class:`Leaderboard` object with all players (including dealer)

    
    :return: Returns a new instance of the game class with an unshuffled deck and empty leaderboard
    :rtype: :class`Game`
    """

    suits = ["S", "H", "D", "C"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    dealer = Dealer() #Instantiates the dealer

    def __init__(self, human_player_count=1, computer_player_count=1):

        self.print_intro()

        print(f"""\nWelcome to terminal Blackjack! In just a moment you'll be on your way.\n
        You initiated a game with {human_player_count} human player(s) and {computer_player_count} computer player(s).\n
        Please now name your human players:\n
        """)
        
        #Instance attributes
        self.cards = [Card(value + '-' + suit) for suit in self.suits for value in self.values] #creates an unshuffled deck
        
        human_players = []
        for i in range(human_player_count):
            name = input(f"\nName of human player {i+1}:\t") #get human player names
            human_players.append(Human(i+1, name))
        
        computer_players = []
        for i in range(computer_player_count):
            computer_players.append(Computer(i))
        
        
        self.human_players = human_players 
        self.computer_players = computer_players 
        self.leaderboard = Leaderboard(human_players + computer_players + [self.dealer]) #create leaderboard


    @classmethod
    def start_game(cls):
        """A command-line friendly game constructing class method that allows users to specify and name their human
        and computer based players when initializing a new game. An alternative to calling the Game() initialization method.

        :return: Returns a new instance of the game class with an unshuffled deck and empty leaderboard
        :rtype: :class`Game`
        """

        cls.print_intro()

        #Word art sourced from https://fsymbols.com/text-art/

        print("""\nWelcome to terminal Blackjack! In just a moment you'll be on your way.\n
        Before we start the game, we'll need to know how many people are playing...\n
        Let us know the number of human players you have (1 to 5) and computer players you'd like to play with (1 to 5)!\n
        """)
       
        while True:
            try:
                human_count = int(input(f"How many human players?\t")) #Prompt user for human players
                if human_count in list(range(1, 6)): #Game must have between 1 and 5 human players
                    break
                else:
                    print("There can only be 1 to 5 human players in the game\n")
            except ValueError: #Integer not provided
                print("There must be an interger value of human players from 1 to 5\n")
        
        while True:
            try:
                computer_count = int(input(f"\nHow many computer players? \t"))
                if computer_count in list(range(1, 6)): #Game must have between 1 and 5 computer players
                    break
                else:
                        print("There can only be 1 to 5 computer players in the game\n")
            except ValueError: #Integer not provided
                print("There must be an interger value of computer players from 1 to 5\n")
        
        game = cls(human_count, computer_count) #intantiate game from user input

        print("\n --- Your game has been constructed! Get ready to play! --- \n")

        return game

    def list_all_players(self):
        """Returns a list of all players in the game instance
        :return: A list of all players in the game instance
        :rtype: List[class:`Player`]
        """
        return self.human_players + self.computer_players + [self.dealer]

    def shuffle(self):
        """Shuffles the game instance cards, and places the shuffled deck in the self.cards attribute
        """
        cards_copy = self.cards
        self.cards = []
        for _ in range(len(cards_copy)):
            index = randint(1, len(cards_copy)) - 1
            shuffled_card = cards_copy.pop(index)
            self.cards.append(shuffled_card)

    def new_deck(self):
        """The new_deck is an instance method that takes no parameters, but resets the game's self.cards attribute to a new shuffled deck.
        The method is called should the game's deck reach a length of 0.
        """
        self.cards = [Card(value + '-' + suit) for suit in self.suits for value in self.values]
        self.shuffle()

    def deal(self):
        """The deal method is called at the start of the game and sends 2 cards to each player in the game.
        """
        deal_array = self.list_all_players()
        for _ in range(2): #deal 2 cards to every player
            for player in deal_array:
                #If the deck is emptied, use a new deck 
                if len(self.cards) == 0:
                    self.new_deck()

                card = self.cards.pop(0)
                player.hand.add_card(card)

    def give_info_to_player(self, player):
        """An instance method called at the beginning of every player's turn to provide the player with necessary game info:
        their hand and the hands of their competitors.

        :param player: the player whose current turn it is
        :type player: class:`player`
        """
        internal_hand = player.hand.print_hand() #The player's hand
 
        print(f"########## Player: {player.name} ({player.type}) TURN ##########\n")

        if player == self.dealer: #The dealer flips over their facedown card
            print(f"The dealer flips their facedown card - their cards are {internal_hand} and has {player.hand.score} points.")
        else:
            print(f"Your cards are {internal_hand}, you have {player.hand.score} points. Cross 21, you bust!\n")

        print("The table looks like this:\n")    
        for other_player in self.list_all_players(): #print competitor hands
            if other_player == self.dealer:
                other_player_hand = other_player.hand.print_hand(dealer_external=True)
            else:
                other_player_hand = other_player.hand.print_hand(dealer_external=False)
            if other_player == player: #don't reprint the current player's hand
                continue

            print(f"* {other_player.name} * \n")
            if other_player.hand.bust == True:
                print(f"{other_player.name} has busted with cards {other_player_hand}\n")
                continue
            else:
                print(f"{other_player.name} has not busted. Their cards are {other_player_hand}\n")


    def declare_winner(self):
        """An instance method called at the end of every round that determines the winner and updates the class:`Leaderboard` attribute.
        """
        players_not_bust = list(filter(lambda player: player.hand.bust == False, self.list_all_players()))
        if len(players_not_bust) == 0:
            print(f"This round has no winners")
            return
        else: #if there is a winner(s), determine the max score (of those not busted)
            max_score = 0
            for player in players_not_bust:
                if player.hand.score > max_score:
                    max_score = player.hand.score
            winners = []
            for player in players_not_bust: #find all players with max score
                if player.hand.score == max_score:
                    winners.append(player)

            if len(winners) == 1:
                print(f"The winner of this round is {winners[0].name} with {max_score} points\n")
                winners[0].wins += 1 #increment wins for winnters

            else:
                print(f"There are {len(winners)} winners of this round with {max_score} points! They are:\n")
                for winner in winners:
                    print(f"* {winner.name} *")
                    winner.wins += 1
        self.leaderboard.round_count += 1 #increment round_count
        self.leaderboard.update_standings()
        self.leaderboard.print_leaderboard()

    def reset_game(self):
        """An instance method called at the end of every round that takes all player cards and sets up a fresh deck.
        """
        self.cards = [Card(value + '-' + suit) for suit in self.suits for value in self.values]
        for player in self.list_all_players():
            player.hand.cards = []


    def play(self):
        """The play method is called in the executable file blackjack.py. It shuffles the deck, and deals cards, then has 
        every player play their round before declaring a winner and printing the current leaderboard standings. 
        The method then prompts the admin human user if they would like to play another round.
        """
        self.shuffle()
        self.deal()
        
        for player in self.list_all_players():
            self.give_info_to_player(player)
            player.play_round(self)
        
        self.declare_winner()

        while True:
            play_another_round = input('That was fun! Would you like to play another round [Yes / No]?').lower()
            if play_another_round == 'yes' or play_another_round == 'no':
                break
            else:
                print("You must answer 'Yes' or 'No'!")
        
        if play_another_round == 'yes':
            self.reset_game() #reset the deck and hands
            self.play() #recursively call play_game
        
        else:
            print("It was great playing with you! Here are the final standings: \n")
            self.leaderboard.print_leaderboard()

    def print_intro(self):
        print("""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")

        #Word art sourced from https://fsymbols.com/text-art/

