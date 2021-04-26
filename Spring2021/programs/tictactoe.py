# The following program is a two-player tic tac toe game that will have the players try to get 
# three Xs or Os in a row to win the game. If no gets three in a row the players tied the game.

# A class that gives the player a shape (X or O), name, and score.
class Player:

    def __init__(self, shape, name):
        self.shape = shape
        self.score = 0
        self.getName(name)

    # Gives a point to the winner of each round.
    def addPoints(self):
        self.score += 1

    # Changes a players shape to X or O
    def changeShape(self):
        if(self.shape == 'X'): self.shape = 'O'
        else: self.shape = 'X'

    # Gets each players name and updates the object
    def getName(self, player):
        
        while True:
            player_name = input('\n' + player + ', enter your name:\n> ')
            player_name = player_name.strip()
            
            # If the user doesn't enter a name set it to a default value
            if(len(player_name) == 0):
                self.name = player
                break
            # The player's name can not be greater than 20 characters
            elif(len(player_name) not in range(0, 21)):
                print('\nInvalid entry: Your name must be less than 21 characters.')
            else:
                self.name = player_name
                break

# Displays the board
def displayBoard(board):
    print()
    rowIndex = 0        # Counts the number of rows
    for row in board:
        print(*row, sep = " | ")   # Separates every cell in a row by |
        
        if(rowIndex != 2):
            print('----------')
        
        rowIndex += 1
    print()

# Displays the name of the player whose turn it is
def displayTurn(player):
    print()
    print(player.name + '\'s turn (' + player.shape + ')')
        
# Determines which player makes the first move by seeing which player's shape is an X        
def getPlayerWithFirstMove(player1, player2):
    if(player1.shape == 'X'):
        return player1
    else:
        return player2


# Replaces a value in the board with the player's shape
def updateBoard(shape, board, player_cell):
    
    # Loops through the board to find the matching cell and stores the shape at that cell
    for row in range(0, 3):
        for cell in range(0, 3): 
            if board[row][cell] == player_cell:
                board[row][cell] = shape     # Stores the shape in the correct cell    

# Gets the value of the cell
def getCellValue(cell, board):
    
    i = 1
    cell = int(cell)
    
    # Loops through each cell in the board to find the one that 
    # matches the players input. Then return that cells value
    for row in board:
        for col in row:
            if(cell == i):
                return col
            i += 1

# Ensures the the cell exists and that it is not already full. 
# Returns False if the input is valid. Returns True if the input is invalid.
def validateInput(cell, board):
    
    # If the cell entered is a number between 1 - 10
    if(cell.isnumeric() and int(cell) in range(1, 10)):

        # if the cell is full print an error message, then return 
        value = getCellValue(cell, board)
        if(value == 'X' or value == 'O'):
            print('Oops! This cell is already full!\n')
            return True

        return False
    else:
        print('Invalid number entered.\n')
        return True

# Prompts the user to make a move and then updates the board
def makeAMovePrompt(player, board):
    invalid = True

    while invalid:
        print('Enter a number between 1 - 9 to place a ' + player.shape + ' onto the board.')
        cell = input('> ')
        invalid = validateInput(cell, board)
    
    updateBoard(player.shape, board, cell)

# Alternates between X and O after each turn in a round 
def switchPlayer(player, player1, player2):
    if player.name == player1.name:
        return player2
    else:
        return player1    

# Returns true if a player has three shapes in a row
def rowWin(board, player):
    
    for row in board:
        if all(values == player.shape for values in row):     # If all elements in the row equal each other
            return True

    return False

# Returns true if a player has three shapes in a column
def columnWin(board, player):
    
    valuesInCol = list()     # List of all the values in a column

    j = 0
    while (j < 3):
        for i in range(0, 3):
            valuesInCol.append(board[i][j])     # Adds each value in the column to a list
        
        # If all values in the column equal each other, return True
        if all(values == player.shape for values in valuesInCol):
            return True

        j += 1              # Move to the next column if a win wasn't found
        valuesInCol = []    # Resets the list so it can store the next set of values
        
    return False

# Returns true if a player has three shapes in a diagonal
def diagonalWin(board, player):
    # All possible combinations of a diagonal win
    diagonal1 = [[0, 0],[1, 1], [2, 2]]
    diagonal2 = [[0, 2], [1, 1], [2, 0]]
    
    lst = list()    # List that stores every value in a diagonal
    
    # Stores each value in the diagonal in a list
    for values in diagonal1:
        i = values[0]
        j = values[1]
        lst.append(board[i][j])

    # If all values in the diagonal equal each other, return True
    if all(values == player.shape for values in lst):
        return True

    lst = []    # Resets the list back to empty
    
    for values in diagonal2:
        i = values[0]
        j = values[1]
        lst.append(board[i][j])
    
    # If all values in the diagonal equal each other, return True
    if all(values == player.shape for values in lst):
        return True

    return False

# Checks the board to see if a player won the round, returns True if a winner was found
def getRoundWinner(board, player):
    winFound = False
    
    if(rowWin(board, player)):
        winFound = True
    elif(columnWin(board, player)):
        winFound = True
    elif(diagonalWin(board, player)):
        winFound = True

    return winFound

# Resets the board and starts a new game. Returns when the round is over.
def startRound(player1, player2):
    
    # The board resets after every round.
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    # player is the person who is currently making a move
    player = getPlayerWithFirstMove(player1, player2)
    displayBoard(board)     

    # There are only 9 moves in a round
    for moves in range(9):
        displayTurn(player)
        makeAMovePrompt(player, board)
        displayBoard(board)
        winnerFound = getRoundWinner(board, player)

        # Gives the winner of the round a point and displays their name
        if(winnerFound == True):
            print(player.name + ' wins!\n')
            player.addPoints()
            break

        player = switchPlayer(player, player1, player2)

# Asks user if they want to quit. 
# Returns False if they enter N, Returns True if they enter Y
def askForQuit():
    while True:
        response = input('\nWould you like to play another game? Y or N\n> ')
        if (response.upper() == 'N'):
            return False
        elif (response.upper() == 'Y'):
            return True

def printScores(player1, player2):
    print('Scores\n------')
    print(player1.name + ': ' + str(player1.score))
    print(player2.name + ': ' + str(player2.score))

def main():

    # Creating players and getting their names
    player1 = Player('X', 'Player1')
    player2 = Player('O', 'Player2')
    
    print('\n\nLet\'s Play Tic-Tac-Toe!')

    # Creates new rounds until a user quits the game
    running = True
    while running:
        startRound(player1, player2)
        printScores(player1, player2)
        
        running = askForQuit()

        # Changes the shape of each player
        player1.changeShape()
        player2.changeShape()

main()