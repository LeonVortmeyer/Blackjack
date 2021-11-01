#Leon Vortmeyer 10.31.2021

class Hand:
    """
    Organizes all Hand related logic since this is common to all players (calculating scores, hand string representations, etc.)
    The hand stores attributes for the hands current score (recalculated after every hit), as well as the bust status as a boolean.

    :param cards: A list of card objects or [], defaults to []
    :type cards: [`class`:Card]

    :ivar cards: set equal to cards parameter
    :ivar score: Integer represnting the hand's current score
    :ivar bust: boolean representing the hand's current bust status

    :return: Returns a new instance of Hand
    :rtype: :class`Hand`
    """
    
    def __init__(self, cards=[]):
        self.cards = cards
        self.score = Hand.hand_score(cards)[0]
        self.bust = Hand.hand_score(cards)[1]

    def __repr__(self):
        """
        Defines a string representation for the Hand instance.
        """

        hand_repr = 'Player Hand: \n'
        for card in self.cards:
            hand_repr += repr(card) + '\n'
        return hand_repr

    def print_hand(self, dealer_external=False):
        """
        Prints the calling player's hand. If dealer_external is True, prints with a facedown first card. If external is False, prints all cards
        faceup. The default implementation sets external to False (faceup printing).

        :param dealer_external: A boolean of whether the hand is printed with the first card facedown (dealer hand shown to other players) defaults to `False`
        :type cards: boolean

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
        """
        Adds card to the hand and recalculates score and bust attributes.

        :param card: The card added to the hand
        :type card: class:`Card`

        """
        self.cards.append(card)
        self.score, self.bust = self.hand_score(self.cards) #recalculate score and bust attributes when card is appended

    
    @staticmethod    
    def hand_score(cards):
        """
        A static method that takes in a card array and calculates a score and bust boolean for the hand.

        :param cards: An array of card objects
        :type cards: [class:`Card`]

        :return: Returns a tuple of hand score and bust boolean
        :rtype: (int, boolean)
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
        #for _ in range(aces_count):
        if points + aces_count > 21: #there is no way to fit aces without busting
            bust = True
            return (points, bust)
        else: #there exists a way to fit aces
            points_available = 21 - points
            high_aces_used = points_available // 11
            points = points + high_aces_used * 11 + (aces_count - high_aces_used)
            bust = False
            return (points, bust)