import random

#Variables
game_list = [' ']*10
game_on = True

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
        return ('X','O')
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

    if playerwon == False:
        print("Its a Tie!")
        gameon_choice()

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
    pos = 'Placeholder'
    while int(pos)not in range(1,10) or not space_check(board, pos):
        pos = int(input("Please enter an available position on the board (1-9): "))

    print(pos)
    return pos

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','y','N','n']:
        
        choice = input("Keep Playing? (Y or N) ")

        if choice not in ['Y','y','N','n']:
            print("Please choose Y or N ")

    if choice in ['Y','y']:
        return True
    game_on = False
    return False
pos_choice(game_list)
#Function Calls
#while game_on:
    #display(game_list)
    #full_board_check(game_list)
    #player_input()
    #place_marker(game_list, 'X' , 2)
    #win_check(game_list," ")
    #gameon_choice()
    #space_check(game_list,1)
    #full_board_check(game_list)
    #pos_choice(game_list)
    #game_on = gameon_choice()