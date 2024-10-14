#create gameboard spots for player insertion
gameBoard = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

player = ''
opponent = ''

#method to print game board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def game():
    while (1):
        choice = input("Would you like to go first? (Y/N): ")
        if (choice == 'Y' or choice == 'y'):
            player = 'X'
            opponent = 'O'
            break
        elif (choice == 'N' or choice == 'n'):
            player = 'O'
            opponent = 'X'
            break
        else:
            choice = ''
            print("Please enter a valid input.")


    printBoard(gameBoard)
    placement = input("Select a placement (1-9): ")

    #player choices
    if (placement == '1'):
        gameBoard[1] = player
        printBoard(gameBoard)
    elif (placement == '2'):
        gameBoard[2] = player
        printBoard(gameBoard)
    elif (placement == '3'):
        gameBoard[3] = player
        printBoard(gameBoard)
    elif (placement == '4'):
        gameBoard[4] = player
        printBoard(gameBoard)
    elif (placement == '5'):
        gameBoard[5] = player
        printBoard(gameBoard)
    elif (placement == '6'):
        gameBoard[6] = player
        printBoard(gameBoard)
    elif (placement == '7'):
        gameBoard[7] = player
        printBoard(gameBoard)
    elif (placement == '8'):
        gameBoard[8] = player
        printBoard(gameBoard)
    elif (placement == '9'):
        gameBoard[9] = player
        printBoard(gameBoard)
    else:
        print("Please enter a valid input.")


game()