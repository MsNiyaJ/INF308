# The following program is a tool for making and using flashcards
import random

class Card:

    #initializing counters to 0
    correct = 0
    incorrect = 0

    # A function that initializes the values of question and answer
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    # Displays the question, increments correct or incorrect, 
    # and gives the user feedback.
    def display(self):
        
        # Prints the question on the flash card
        print("\nQuestion:", self.question)
        
        # Prompts the user to answer the question
        print("Your answer:")
        usersAnswer = input('> ')
        
        checkForQuit(usersAnswer)

        # Gives the user feeback and increments correct or incorrect
        if(self.answer == usersAnswer):
            print("Correct! The answer was:", self.answer)
            self.correct = self.correct + 1 
        else:
            print("Incorrect! The answer was:", self.answer)
            self.incorrect = self.incorrect + 1

        return usersAnswer      # used for testing

# Checks if the user wants to end the program
def checkForQuit(userInput):
    if(userInput.lower() == '--quit'):
        exit()

# Opens a file and returns a list of each line. Exits the program if the file can't be found
def openFile(path):

    try:
        file = open(path, "r")
        lines = file.readlines()                # Returns a list of each line in the file
        return lines
    except:
        print("\nFile could not be read. Exiting program...")
        exit()
    
# Turns a .tsv file into a list of Card objects
def createFlashcards(lines):
    flashcards = list()
    
    for line in lines:
        line = line.rstrip()                       # Gets rid of the new line character at the end of the line
        
        flashcard_info = line.split("\t")          # Splits the string by tabs and stores it in a list
        question = flashcard_info[0]               # Stores the question of the flashcard
        answer = flashcard_info[1]                 # Stores the answer of the flashcard
        flashcards.append(Card(question, answer))  #Creates a list of Card objects

    return flashcards

# Prints how many questions a user got right and wrong
def printScore(flashcards):
    
    correct = 0         # Total amount of questions the user got correct
    incorrect = 0       # Total amount of questions the user got wrong

    # Loops through list of object to determine the users score
    for flashcard in flashcards:
        correct = correct + flashcard.correct
        incorrect = incorrect + flashcard.incorrect
    
    numOfQuestions = correct + incorrect
    msg = "You got "+ str(correct) + " / " + str(numOfQuestions) + " questions right!"
    print("\n"+msg)
    return msg
    
# Main function that is called when the program is ran
def running():
    print("\nEnter a .tsv file (E.g. C:\\\\Users\\\\Owner\\\\Documents\\\\flashcards.tsv)")
    path = input("> ")

    lines = openFile(path)
    
    print("\nEnter '--quit' at any time to exit the program")
    entry = input("Press enter to continue...\n> ")
    checkForQuit(entry)

    while(True):
        flashcards = createFlashcards(lines)    # Returns a list of Card objects, resets correct/incorrect back to 0
    
        print("\nShuffling flashcards...")
        random.shuffle(flashcards)

        # Prints a question until a user quits 
        for flashcard in flashcards:
            flashcard.display()

        printScore(flashcards)          

        userInput = input("\nEnter '--quit' to end the program or press enter to start over...\n> ")
        checkForQuit(userInput)

#TEST: Checks if display() works properly
# question = "How many stars are in the American Flag?"
# answer = "50"
# flashcard = Card(question, answer)

# print("\n\nTESTING DISPLAY:")
# usersAnswer = flashcard.display()
# print()

# The program should end if a user enters '--quit'

# if(usersAnswer == '50'):                                
#     print('Expected: Correct = 1, Incorrect = 0')
#     print('Result:   Correct =', flashcard.correct, ", Incorrect =", flashcard.incorrect)
# else:
#     print('Expected: Correct = 0 , Incorrect = 1')
#     print('Result:   Correct =', flashcard.correct, ", Incorrect =", flashcard.incorrect)

running()