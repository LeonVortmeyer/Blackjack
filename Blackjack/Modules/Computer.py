#Leon Vortmeyer 10.31.2021

from Modules.Player import Player

class Computer(Player):
    def __init__(self, id):
        super().__init__(id, f"Computer {id}")
        self.type = 'Computer'

        
    def think(self):
        """
        Think is called on an instance of computer and abstracts the computer logic to be used in play_round.
        Think returns True if the computer will hit, and false is the computer will stand.
        The basic computer logic is to hit so long as the hand score is less than or equal to 16.
        Think allows us to define various computer classes that inherit from Computer to code up different computer logic.
        Great idea from a classmate in presentation!
        """
        while self.hand.score <= 16:
            return True 
        return False

    def play_round(self, Game): 

            while self.think():
                if len(Game.cards) == 0:
                    Game.new_deck()
                card = Game.cards.pop(0)
                self.hit(card)
                print(f"Computer has hit and received card {repr(card)}")

            if self.hand.bust == True:
                print(f"Computer has busted with {self.hand.score} points!\n")
                return
            else:
                print(f"Computer has chosen to stand with {self.hand.score} points.\n")