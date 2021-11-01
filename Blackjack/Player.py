#Leon Vortmeyer 10.31.2021

from abc import ABC, abstractmethod
from Hand import Hand

class Player(ABC):
    """The abstract base class (inherits from ABC) from which class:`Human`, class:`Computer`, and class:`Dealer` all inherit
    Each player is initialized with 0 wins and an empty hand represented by [].

    :param id: the id of the integer passed to the player
    :type id: Integer

    :param name: the name of the player
    :type name: String

    :ivar id: set equal to id param
    :ivar name: set equal to name param
    :ivar hand: the class:`Hand` object of the player, instantiated with []
    :ivar wins: integer tracking the number of player wins, instantiated with 0

    :return: Returns a new instance of the Player
    :rtype: :class`Player`
    """
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = Hand([])
        self.wins = 0

    def hit(self, card):
        """The hit method defines the logic of adding a card to the hand.

        :param card: the card pulled from the deck which will be added to the player's hand (the 'hitting' card)
        :type card: class:`Card`
        """
        self.hand.add_card(card)

    @abstractmethod
    def think(self): #defines player logic
        """A required method for all classes that inherit from class:`Player` that defines their play logic."""
        pass

    def play_round(self, Game):
        """The play_round method organizes the play logic of the game.

        :param Game: the current Game instance in which the player is playing. This is important for tracking the deck and hand score.
        :type Game: class:`Game`
        """
        while self.think():
            if len(Game.cards) == 0:
                Game.new_deck()
            card = Game.cards.pop(0)
            self.hit(card)
            print(f"{self.name} has hit and received card {repr(card)}")
            print(f"{self.name} now has {self.hand.score} points.\n")
            if self.hand.bust == True:
                break

        if self.hand.bust == True:
            print(f"{self.name} has busted with {self.hand.score} points!\n")
            return
        else:
            print(f"{self.name} has chosen to stand with {self.hand.score} points.\n")
            print(f"{self.name}'s points will be compared to other players at the end of the round!\n")  


    
    