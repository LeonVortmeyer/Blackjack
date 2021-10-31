#Leon Vortmeyer 10.31.2021

from abc import ABC, abstractmethod
from Modules.Hand import Hand

class Player(ABC):
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = Hand([])
        self.wins = 0

    def hit(self, card):
        self.hand.add_card(card)

    @abstractmethod
    def play_round(game):
        pass    


    
    