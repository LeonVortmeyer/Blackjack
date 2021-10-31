#Leon Vortmeyer 10.31.2021

from Modules.Player import Player

class Dealer(Player):
    
    def __init__(self):
        super().__init__(0, "Dealer")
        self.type = 'Dealer'

    def play_round(self, Game): 
        while self.hand.score < 17:
            if len(Game.cards) == 0:
                Game.new_deck()
            card = Game.cards.pop(0)
            print(f"Dealer hits and receives {card}\n")
            self.hit(card)
            
        if self.hand.score <= 21:
            print(f"The Dealer has {self.hand.score} and now stands.\n")
        else:
            self.bust = True
            print(f"The Dealer has {self.hand.score} and busts.\n")




