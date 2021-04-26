# War (cardgame): 2-player game 
# How to play: Players will split a deck of cards evenly. Each player will flip their
# top card. The player with the highest card gets both cards. The game ends when
# one player has all the cards (winner) and the other player has no cards (loser)

import random

# Creates a list of strings that represent cards in a deck
def createADeck(deck):
    
    for i in range(1, 14):
        if i == 1:
            card = 'A'
        elif i == 11:
            card = 'J'
        elif i == 12:
            card = 'Q'
        elif i == 13:
            card = 'K'
        else:
            card = str(i)

        # Adds the card with different suits to the deck
        deck.append(card + " Hearts")
        deck.append(card + " Spades")    
        deck.append(card + " Clubs")
        deck.append(card + " Diamonds")

# Converts the card values to numerical values
def convertValuesToInt(value):
    if value == 'A ':
        return 1
    elif value == 'J ':
        return 11
    elif value == 'Q ':
        return 12
    elif value == 'K ':
        return 13
    else:
        return int(value)

# Returns the winner of the round
def getWinnerOfRound(p1_card, p2_card):

    #Gets the first two characters of the string
    p1_card_val = p1_card[:2]
    p2_card_val = p2_card[:2]
    
    p1_card_val = convertValuesToInt(p1_card_val)
    p2_card_val = convertValuesToInt(p2_card_val)
    
    if (p1_card_val > p2_card_val):
        return "player1"
    elif (p2_card_val > p1_card_val): 
        return "player2"
    else:
        return "tie"

# Moves all cards played in the round to the back of the winners deck
def collectCards(winnersDeck, played_cards):
    
    # Shuffles each card before the winner puts it at the end of their hand
    random.shuffle(played_cards)

    len_pc = len(played_cards) 

    # Adds the played cards to the winners deck
    for i in range(len_pc):
        winnersDeck.append(played_cards[i])

# Continuously flips cards until one card is higher than the other.
def declareWar(player1, player2, played_cards):
    
    while True:

        # If a player runs out of cards during war they lose the game
        # Its a tie if both players run out of cards
        if(len(player1) == 0 and len(player2) == 0):
            print("You both ran out of cards!")
            break
        elif(len(player1) == 0):
            print("Oh no! Player1 ran out of cards during war!")
            break
        elif(len(player2) == 0):
            print("Oh no! Player2 ran out of cards during war!")
            break

        print("Engaging in battle...who will get all the cards?")
        print("Played cards:", played_cards)

        # Prints the cards played during war
        print("\nplayer1:", player1[0])
        print("player2:", player2[0])

        # Removes the the top card of each player
        p1_card = player1.pop(0)
        p2_card = player2.pop(0)

        # Adds the top card of each player to the played cards list
        played_cards.append(p1_card)
        played_cards.append(p2_card)

        # Winner of the round
        winner = getWinnerOfRound(p1_card, p2_card)

        # Winner takes all played cards and places them to the back of their deck
        if (winner == "player1"):
            print(winner, "is the winner of the round! You get an additional", len(played_cards), "cards!")
            collectCards(player1, played_cards)
            break
        elif (winner == "player2"):
            print(winner, "is the winner of the round! You get an additional", len(played_cards), "cards!")
            collectCards(player2, played_cards)
            break
        else:
            print("What are the odds?! There is another tie! Drawing next cards...")
            input("\nPress Enter to continue...\n")

def displayWinnerOfGame(p1_deck_size, p2_deck_size):
    if(p1_deck_size > p2_deck_size):
        print("Player1 is the winner of the game! Thanks for playing!")
    elif(p2_deck_size > p1_deck_size):
        print("Player2 is the winner of the game! Thanks for playing!")
    else:
        print("You both are winners! Congrats! Thanks for playing!")

# ***********************************************************************
deck = []       #initialize a deck of cards list

createADeck(deck)

# Shuffles the deck of cards 
shuffledDeck = [] + deck
random.shuffle(shuffledDeck)

# Splits the deck in half and assigns a half to each player
player1 = shuffledDeck[:26]
player2 = shuffledDeck[26:]

# Start the game
print("\nWelcome to War! (The Card Game)")

rules = """\nHow to play: Players will split the deck evenly. Each player will flip their
top card. The player with the highest card gets both cards. The game ends when
one player has all the cards (winner) and the other player has no cards (loser)"""

# Displays the rules of the game
print("\r", rules)

input("\nPress Enter to start the game...\n")

# Cards will be drawn until someone quits or the winner is found
while True:

    played_cards = []       #A list of all cards played in the round

    # Removes the the top card of each player
    p1_card = player1.pop(0)
    p2_card = player2.pop(0)

    # Displays which cards each player played
    print("player1:", p1_card)
    print("player2:", p2_card)

    # Adds the top card of each player to the played cards list
    played_cards.append(p1_card)
    played_cards.append(p2_card)
    
    # Winner of the round
    winner = getWinnerOfRound(p1_card, p2_card)

    # If the game is tied we keep flipping cards until a winner is found
    if (winner == "tie"):
        print("Looks like there is a tie! Time to declare war!...")
        input("\nPress Enter to continue...\n")
        declareWar(player1, player2, played_cards)

    # Else the winner takes both cards and places them to the back of the deck
    elif (winner == "player1"):
        print(winner, "is the winner of the round!")
        collectCards(player1, played_cards)

    elif (winner == "player2"):
        print(winner, "is the winner of the round!")
        collectCards(player2, played_cards)

    p1_deck_size = len(player1)
    p2_deck_size = len(player2)

    # Displays how many cards each player has at the end of each round
    print()
    print("player1 has", p1_deck_size, "cards remaining")
    print("player2 has", p2_deck_size, "cards remaining")

    # Ends the game once one of the players have 0 cards
    if(p1_deck_size == 0 or p2_deck_size == 0):
        print("Game over...Someone ran out of cards!")
        input("\nPress Enter to continue...\n")
        break

    entry = input("\nType 'Quit' to end the game, or press Enter to continue...\n")

    if(entry.lower() == "quit"):
        print()
        break

displayWinnerOfGame(p1_deck_size, p2_deck_size)