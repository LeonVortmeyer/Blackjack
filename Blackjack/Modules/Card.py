#Leon Vortmeyer 10.31.2021

class Card:

    #Instantiate value_map
    suits = ["S", "H", "D", "C"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    value_map = {value: int(value) for value in values if value.isdigit()}
    value_map["J"] = 10
    value_map["Q"] = 10
    value_map["K"] = 10
    value_map["A"] = {"low": 1, "high": 11}

    #Instantiate repr_map
    suit_names = {"S":"Spades", "H": "Hearts", "D": "Diamonds", "C": "Clubs"}
    value_names = {"A": "Ace", "2": "Two", "3": "Three", "4": "Four", "5": "Five", 
    "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", 
    "J": "Jack", "Q": "Queen","K": "King"}

    
    def __init__(self, string):
        self.string = string
        self.rank = string.split("-")[0]
        self.suit = string.split("-")[1]
        self.value = Card.value_map[self.rank]
    
    def __repr__(self):
        value_char = self.string.split("-")[0]
        suit_char = self.string.split("-")[1]
        return '-- ' + Card.value_names[value_char] + ' of ' + Card.suit_names[suit_char] + ' --'





        

        





        