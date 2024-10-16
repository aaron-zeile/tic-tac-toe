import random
import time

# declare player and opponent chars
player = 'X'
opponent = 'O'

# declare variables for scorekeeping
#wins = 0
#losses = 0

# method to print game board
def printBoard(board):
    #print("Score: ", wins, "W  ", losses, "L")
    #print("     ")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    #separator for cleaner look
    print("-----")

#method to check for winner
def winner(board):
#PLAYER WINS
    # horizontal win
    if (board[1] == player and board[2] == player and board[3] == player):
        return player
    elif (board[4] == player and board[5] == player and board[6] == player):
        return player
    elif (board[7] == player and board[8] == player and board[9] == player):
        return player
    
    # vertical win
    elif (board[1] == player and board[4] == player and board[7] == player):
        return player
    elif (board[2] == player and board[5] == player and board[8] == player):
        return player
    elif (board[3] == player and board[6] == player and board[9] == player):
        return player
    
    # diagonal win
    elif (board[1] == player and board[5] == player and board[9] == player):
        return player
    elif (board[3] == player and board[5] == player and board[7] == player):
        return player

#OPPONENT WINS
    # horizontal win
    if (board[1] == opponent and board[2] == opponent and board[3] == opponent):
        return opponent
    elif (board[4] == opponent and board[5] == opponent and board[6] == opponent):
        return opponent
    elif (board[7] == opponent and board[8] == opponent and board[9] == opponent):
        return opponent
    
    # vertical win
    elif (board[1] == opponent and board[4] == opponent and board[7] == opponent):
        return opponent
    elif (board[2] == opponent and board[5] == opponent and board[8] == opponent):
        return opponent
    elif (board[3] == opponent and board[6] == opponent and board[9] == opponent):
        return opponent
    
    # diagonal win
    elif (board[1] == opponent and board[5] == opponent and board[9] == opponent):
        return opponent
    elif (board[3] == opponent and board[5] == opponent and board[7] == opponent):
        return opponent
    
#NO WINNER
    else:
        return

#method to get the player's spot choice
def player_turn(board, available_spots):
    # loop to validate player input
    while 1:
        placement = input("Select a placement (1-9): ")

        # insert player decision
        if (placement == '1' and 1 in available_spots):
            board[1] = player
            available_spots.remove(1)
            break

        elif (placement == '2' and 2 in available_spots):
            board[2] = player
            available_spots.remove(2)
            break

        elif (placement == '3' and 3 in available_spots):
            board[3] = player
            available_spots.remove(3)
            break

        elif (placement == '4' and 4 in available_spots):
            board[4] = player 
            available_spots.remove(4) 
            break

        elif (placement == '5' and 5 in available_spots):
            board[5] = player 
            available_spots.remove(5)  
            break

        elif (placement == '6' and 6 in available_spots):
            board[6] = player  
            available_spots.remove(6)
            break

        elif (placement == '7' and 7 in available_spots):
            board[7] = player 
            available_spots.remove(7)
            break

        elif (placement == '8' and 8 in available_spots):
            board[8] = player 
            available_spots.remove(8)
            break

        elif (placement == '9' and 9 in available_spots):
            board[9] = player
            available_spots.remove(9)
            break

        else:
            print("Please make a valid selection.")

        printBoard(board)

# method to run opponent's turn (computer)
def opponent_turn(board, available_spots):
    # generate random element from array for opponent turn
    if (available_spots):
        choice = random.choice(available_spots)

    # remove spot that opponent chose
    available_spots.remove(choice)

    # place opponent's choice
    if (choice == 1):
        board[1] = opponent

    elif (choice == 2):
        board[2] = opponent

    elif (choice == 3):
        board[3] = opponent

    elif (choice == 4):
        board[4] = opponent 

    elif (choice == 5):
        board[5] = opponent 

    elif (choice == 6):
        board[6] = opponent  

    elif (choice == 7):
        board[7] = opponent 

    elif (choice == 8):
        board[8] = opponent 

    elif (choice == 9):
        board[9] = opponent

    printBoard(board)


# method to run game
def game():
    # create blank dictionary to store and display X's and O's
    gameBoard = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    
    # array to keep track of open spots
    open_spots = [1,2,3,4,5,6,7,8,9]

    # print starting board
    printBoard(gameBoard)

    # play game
    while 1:
        # get choice from user
        player_turn(gameBoard, open_spots)

        # check if player won
        if (winner(gameBoard) == player):
            print("You won!")
            break
        if (not open_spots):
            printBoard(gameBoard)
            print("Cat's game!")
            break

        # pause program to emulate computer thinking
        time.sleep(1.25)
        # run opponent's turn
        opponent_turn(gameBoard, open_spots)

        # check if opponent won
        if (winner(gameBoard) == opponent):
            print("You lost!")
            break
        if (not open_spots):
            printBoard(gameBoard)
            print("Cat's game!")
            break
    
    # game end menu
    while 1:
        # when game ends, ask if user would like to play again
        playAgain = input("Would you like to play again? (Y/N): ")
        
        # if yes, restart game
        if playAgain == 'Y' or playAgain == 'y':
            game()
        # if no, end program
        elif playAgain == 'N' or playAgain == 'n':
            return 0
        # if invalid response, ask for input again
        else:
            print("Please give a valid response.")

# run game method
game()