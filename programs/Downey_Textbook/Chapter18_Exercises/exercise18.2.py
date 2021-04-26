# Write a Deck method called deal_hands that takes two parameters, 
# the number of hands and the number of cards per hand. It should 
# create the appropriate number of Hand objects, deal the appropriate 
# number of cards per hand, and return a list of Hands.

# class Card with attributes suit_names, rank_names, suit, and rank
class Card:

    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

# class Deck with the attribute cards
class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)        
                self.cards.append(card)     # Creates a list of card objects
        print('Deck created...')

    # creates the appropriate number of Hand objects, deals the appropriate 
    # number of cards per hand, and returns a list of Hands.
    def deal_hands(self, num_of_hands, cards_per_hand):
        print('Dealing cards...')
        hands = []
        
        # For each number of hands create a Hand object
        for n in range(num_of_hands):
            hand = Hand()
            
            # For each Hand object, deal the given number of cards per hand
            for c in range(cards_per_hand):
                hand.cards.append(self.cards.pop())       # Adds the last card in the deck to the hand
            
            hands.append(hand)                            # Adds the hand object to a list hands

        return hands                                      # Returns a list of Hands

#class Hand with the attributes cards
class Hand:
    
    def __init__(self):
        self.cards = []


def test(num1, num2):
    print()
    print("Testing program...")
    deck = Deck()                   # Create a deck
    hands = deck.deal_hands(num1, num2)   # Deal 7 cards to 5 different hands     

    count = 1       # Counts the number of hands there are

    for hand in hands:              # For each hand in the list of hand objects
        print('Hand', count, ':')
        for card in hand.cards:     # For each card in the hand, print the card
            print(card)
        print()
        count += 1                  # increment count

test(5, 7)
test(2, 13)