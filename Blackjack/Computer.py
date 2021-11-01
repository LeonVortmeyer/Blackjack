#Leon Vortmeyer 10.31.2021

from Player import Player

class Computer(Player):
    """The Computer class inherits from the class:`Player` abstract base class.

    :param id: the id of the integer passed to the computer player
    :type id: Integer
    
    :ivar type: string set to "Computer"

    :return: Returns a new instance of the Computer
    :rtype: :class`Computer`
    """


    def __init__(self, id):
        super().__init__(id, f"Computer {id}") #Calls player constructor
        self.type = 'Computer'

        
    def think(self):
        """
        Think is called on an instance of computer and abstracts the computer logic to be used in play_round.
        The basic computer logic is to hit so long as the hand score is less than or equal to 16.
        Think allows us to define various computer classes that inherit from Computer to code up different computer logic.
        Great idea from a classmate in presentation!

        :return: `True` if computer hits, `False` if computer stands
        :rtype: : boolean
        """
        while self.hand.score <= 16:
            return True 
        return False