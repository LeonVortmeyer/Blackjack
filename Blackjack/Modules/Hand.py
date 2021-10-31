#Leon Vortmeyer 10.31.2021

class Hand:
    
    def __init__(self, cards):
        self.cards = cards
        self.score = Hand.hand_score(cards)[0]
        self.bust = Hand.hand_score(cards)[1]

    def __repr__(self):
        hand_repr = 'Player Hand: \n'
        for card in self.cards:
            hand_repr += repr(card) + '\n'
        return hand_repr

    def print_hand(self, dealer_external=False):
        """
        Prints the calling player's hand. If dealer_external is True, prints with a facedown first card. If external is False, prints all cards
        faceup. The default implementation sets external to False (faceup printing).
        """
        statement = '\n'
        if dealer_external == False:
            statement += repr(self.cards[0]) + '\n' #if internal, print first card faceup
        else:
            statement += '-- Facedown card --\n' #if external, print first card as facedown

        for card in self.cards[1:]:
            statement += repr(card) + '\n' #print all remaining cards faceup regardless if external or internal
        return statement
    
    def add_card(self, card):
        self.cards.append(card)
        self.score, self.bust = self.hand_score(self.cards) #recalculate score and bust attributes when card is appended

    
    @staticmethod    
    def hand_score(cards):
        """
        A static method that takes in a card array and calculates a score and bust boolean for the hand.
        """
        points = 0
        aces_count = 0
        for card in cards:
                try:
                    points += card.value
                except TypeError: #Ace is used with 'low' and 'high' dict
                    aces_count += 1
        if aces_count == 0:
            if points > 21:
                bust = True
                return (points, bust)
            else:
                bust = False
                return (points, bust)
        for _ in range(aces_count):
            if points + aces_count > 21:
                bust = True
                return (points, bust)
            else: #there exists a way to fit aces
                points_available = 21 - points
                high_aces_used = points_available // 11
                points = points + high_aces_used * 11 + (aces_count - high_aces_used)
                bust = False
                return (points, bust)