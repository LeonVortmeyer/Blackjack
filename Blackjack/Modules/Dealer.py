#Leon Vortmeyer 10.31.2021

from Player import Player

class Dealer(Player):
    """The Dealer class inherits from the class:`Player` abstract base class.
    
    :return: Returns a new instance of the Dealer
    :rtype: :class`Dealer`
    """
    
    def __init__(self):
        super().__init__(0, "Dealer")
        self.type = 'Dealer'


    def think(self):
        """
        Think is called on an instance of Dealer and abstracts the Dealer logic to be used in play_round.
        The Dealer logic is forced to hit so long as the hand score is less than or equal to 17.

        :return: `True` if Dealer hits, `False` if Dealer stands
        :rtype: : boolean
        """
        while self.hand.score <= 17:
            return True 
        return False





