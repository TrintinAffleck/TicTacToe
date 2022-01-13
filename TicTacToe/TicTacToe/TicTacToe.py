import random

#Variables
game_list = [' ']*10

def clear():
    #To clear the screen
    print("\n"*24)

def display(board):
    #Printing list into 3x3 rows AKA TicTacToe board
    clear()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("Here is the current list")
    
def player_input():
    ''' 
    OUTPUT
    (Player1 Marker, Player2 Marker)
    '''
    marker = ""
    #While not X or O keep asking for input
    while marker != 'X' and marker != 'O':
        marker = input("Player1: Choose Marker (X or O) ").upper()

    if marker == 'X':
        return('X','O')
    return ('O','X')

def place_marker(board, marker: str, position: int):
    board = game_list
    board[position] = marker

    return board

def win_check(board, mark: str):
    #Checking for X or O's in a row
    return (board[1] == board[2] == board[3] == mark or #BottomRow
    board[1] == board[4] == board[7] == mark or #LeftSide
    board[3] == board[6] == board[9] == mark or #RightSide
    board[7] == board[8] == board[9] == mark or #TopRow
    board[7] == board[5] == board[3] == mark or #LeftDiagonal
    board[9] == board[5] == board[1] == mark or #RightDiangonal
    board[4] == board[5] == board[6] == mark or #HorizonalRow
    board[2] == board[5] == board[8] == mark) #VerticalRow


def choose_first():
    rand = random.randint(1,2)
    if rand == 1:
        return "Player 1"
    return "Player 2"
    

def space_check(board, position: int) -> bool:
    '''
    OUTPUT
    Returns True if the position on the board is empty
    Returns False if the position is not an empty string/space
    '''
    return board[position] == ' '

def full_board_check(board):
    board = game_list
    for i in range(1,10):
        if space_check(board,i): #BOARD HAS IS NOT FULL
            return False
    #BOARD IS FULL
    return True

def pos_choice(board):
    #Asking for position check from user
    pos = 0
    ranges = ['1','2','3','4','5','6','7','8','9'] #Positions on the board
    while pos not in ranges or space_check(board, pos) == False: #If space is between 1-9 or not available
        pos = input("Please enter an available position on the board (1-9): ")
        if pos not in ranges:
            print("Invalid position")
        elif pos in ranges:
            pos = int(pos)
            if space_check(board,pos): #return if there is space 
                return pos
            elif not space_check(board,pos): #continue the while loop if there is no space on the board
                print('{} is not an available position'.format(pos))
                continue
    

def gameon_choice():
    choice = input("Play again? (Yes or No) ")
    if choice == 'Yes' or choice == 'yes':
        return True
    return False

#Function Calls
while True:
    #PLAYGAME
    #SETTING UP THE BOARD
    print("Welcome to Tic Tac Toe")

    player1marker,player2marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to play? (y or n) ")

    if play_game in ['Y','y']:
        game_on = True
    else:
        game_on = False

    while game_on:
        #PLAYER1 TURN
        if turn == 'Player 1':
            #Show the board
            display(game_list)
            #Choose a position
            print(f"{turn}s' turn")
            p1pos = pos_choice(game_list)
            #Place the marker on the position
            place_marker(game_list,player1marker,p1pos)
            #Check if they won
            if win_check(game_list,player1marker):
                display(game_list)
                print("Player 1 has won!")
                game_on = False
            else:
                #Or check if tie
                if full_board_check(game_list):
                    display(game_list)
                    print("Its a tie!")
                    game_on == False
                    break
                else:
                    #No tie and no win? Next player
                    turn = 'Player 2'
        #PLAYER2 TURN
        else:
            display(game_list)
            print(f"{turn} 's' turn")
            p2pos = pos_choice(game_list)
            place_marker(game_list,player2marker,p2pos)

            if win_check(game_list,player2marker):
                display(game_list)
                print("Player 2 has won!")
                game_on == False

            else:
                if full_board_check(game_list):
                    display(game_list)
                    print("Its a tie!")
                    break
                else:
                    turn = 'Player 1'
                    
    #Leave the game
    if not gameon_choice():
        break
    