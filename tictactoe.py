import random

#create gameboard spots for player insertion
gameBoard = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}


#store empty keys to wipe board after each game
emptyKeys = []
for keys in gameBoard.keys():
    emptyKeys.append(gameBoard[keys]) 


#declare player and opponent chars
player = 'X'
opponent = 'O'

#method to print game board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def playerWon(gameBoard):
    #horizontal win
    if (gameBoard[1] == player and gameBoard[2] == player and gameBoard[3] == player):
        return True
    elif (gameBoard[4] == player and gameBoard[5] == player and gameBoard[6] == player):
        return True
    elif (gameBoard[7] == player and gameBoard[8] == player and gameBoard[9] == player):
        return True
    
    #vertical win
    elif (gameBoard[1] == player and gameBoard[4] == player and gameBoard[7] == player):
        return True
    elif (gameBoard[2] == player and gameBoard[5] == player and gameBoard[8] == player):
        return True
    elif (gameBoard[3] == player and gameBoard[6] == player and gameBoard[9] == player):
        return True
    
    #diagonal win
    elif (gameBoard[1] == player and gameBoard[5] == player and gameBoard[9] == player):
        return True
    elif (gameBoard[3] == player and gameBoard[5] == player and gameBoard[7] == player):
        return True

    else:
        return False


#method for game functionality
def game():
    #Start game
    while 1:
        printBoard(gameBoard)
        placement = input("Select a placement (1-9): ")

        #insert player decision
        if (placement == '1'):
            gameBoard[1] = player  
        elif (placement == '2'):
            gameBoard[2] = player 
        elif (placement == '3'):
            gameBoard[3] = player
        elif (placement == '4'):
            gameBoard[4] = player   
        elif (placement == '5'):
            gameBoard[5] = player      
        elif (placement == '6'):
            gameBoard[6] = player       
        elif (placement == '7'):
            gameBoard[7] = player   
        elif (placement == '8'):
            gameBoard[8] = player 
        elif (placement == '9'):
            gameBoard[9] = player
        else:
            print("Please make a valid selection.")
        
        printBoard(gameBoard)

        #check for winner
        if (playerWon(gameBoard)):
            print("You won!\n")
            break

        oppChoice = random.randint(1,9)

    #When game ends, ask if user would like to play again?
    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain == 'Y' or playAgain == 'y':
        print("Board reset")
    elif playAgain == 'N' or playAgain == 'n':
        return 0

game()