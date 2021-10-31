#Leon Vortmeyer 10.31.2021

from Modules.Player import Player

class Human(Player):
    
    def __init__(self, id, name):
        super().__init__(id, name)
        self.type = 'Human'

    def play_round(self, Game):        
        if self.hand.bust == True:
            print("Player has busted, and can not continue playning. Moving on...")
            return #if player has busted from a hit, return (for recursive calls)

        while True:
            move = input("Would you like to 'hit' or 'stand'\t")
            if move == "hit" or move == "stand":
                break
            else:
                print("You must choose to 'hit' or 'stand'\n")
        
        if move == "hit":

            #If deck is depleted, add a new deck
            if len(Game.cards) == 0:
                Game.new_deck()
            card = Game.cards.pop(0)
            print(f"\nPlayer {self.name} has decided to hit, they received card {card}\n")
            self.hit(card)

            if self.hand.bust == True:
                print(f"{self.name} has busted with {self.hand.score} points!\n")
                return

            else:
                print(f"{self.name} cards are {repr(self.hand)}")
                print(f"You currently have {self.hand.score}, if you cross 21, you bust\n")
                self.play_round(Game) #recursively calls the play_round if player hits. If player busts, procedure returns from first if statement

        elif move == "stand":
            print("You have chosen to stand.\n")
            print(f"You have {self.hand.score} points. Your points will be compared to other players at the end of the round!\n")
            
    


