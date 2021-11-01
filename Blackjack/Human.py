#Leon Vortmeyer 10.31.2021

from Player import Player

class Human(Player):
    """The Human class inherits from the class:`Player` abstract base class.

    :param id: the id of the integer passed to the human player
    :type id: Integer

    :param name: the id of the integer passed to the human player
    :type name: string

    :ivar type: set equal to 'Human' (string)
    
    
    :return: Returns a new instance of Human
    :rtype: :class`Human`
    """
    
    def __init__(self, id, name):
        super().__init__(id, name) #Calls player constructor
        self.type = 'Human'

    def think(self):
        """
        Think is called on an instance of class:`Human` and abstracts the human logic to be used in play_round (class:`Player` method).
        The player is prompted to hit or stand from the command line and their response is used in the class:`Player`'s play_round method.

        :return: `True` if human hits, `False` if human stands
        :rtype: : boolean
        """
        while True:
            move = input("Would you like to 'hit' or 'stand'\t")
            if move == "hit" or move == "stand":
                break
            else:
                print("You must choose to 'hit' or 'stand'\n")
        
        if move == "hit":
            return True
        
        else:
            return False