import random

#Variables
game_list = [' ','X',' ',' ',' ',' ',' ',' ',' ',' ']
game_on = True

def clear():
    #To clear the screen
    print("\n"*100)

def display(game_list: list):
    print("Here is the current list")
    #Printing list into 3x3 rows AKA TicTacToe board
    print(game_list[7] + '|' + game_list[8] + '|' + game_list[9])
    print(game_list[4] + '|' + game_list[5] + '|' + game_list[6])
    print(game_list[1] + '|' + game_list[2] + '|' + game_list[3])
    

def player_input():

    marker = " "
    #If players input is not x or o keep asking for input
    while marker not in ['X','x','O','o']:
        marker = input("Please choose your marker (X or O)")
        
    player1 = marker

    #Setting player markers
    if player1 in ['X','x']:
        print("You chose X as your marker")
        player1 = 'X'
        player2 = 'O'
    else:
        print("You chose O as your marker")
        player1 = 'O'
        player2 = 'X'

    return (player1,player2)

def place_marker(board, marker: str, position: int):
    
    board = game_list
    board[position] = marker

    return game_list


def position_choice(position: int):

    choice = 'wrong'

    while choice not in range(1-10):
        
        choice = input("Pick a position (1-9): ")

        if choice not in range(1-10):
            print("Sorry, invalid choice!")
    position = int(choice)
    return position


def win_check(board, mark: str):
    board = game_list
    mark = player_input()
    print(mark)
    playerwon = False
    #Checking for X or O's in a row
    if board[1] == board[2] == board[3] == mark: #BottomRow
        playerwon = True
    if board[1] == board[4] == board[7] == mark: #LeftSide
        playerwon = True
    if board[3] == board[6] == board[9] == mark: #RightSide
        playerwon = True
    if board[7] == board[8] == board[9] == mark: #TopRow
        playerwon = True
    if board[7] == board[5] == board[3] == mark: #LeftDiagonal
        playerwon = True
    if board[9] == board[5] == board[1] == mark: #RightDiangonal
        playerwon = True
    if board[4] == board[5] == board[6] == mark: #HorizonalRow
        playerwon = True
    if board[2] == board[5] == board[8] == mark: #VerticalRow
        playerwon = True

    if playerwon == False:
        print("Its a Tie!")
        gameon_choice()
    

def choose_first():
    return random.randint(1,2)
    
def space_check(board, position: int) -> bool:
    board = game_list
    if board[position] in ['X', 'O']:
        return True
    return False

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','y','N','n']:
        
        choice = input("Keep Playing? (Y or N) ")

        if choice not in ['Y','y','N','n']:
            print("Please choose Y or N ")

    if choice in ['Y','y']:
        return True
    return False

def user_choice():

    #Validating User Input
    while True:
        choice = input('Please enter a number. (1-9)')
        #Digit Check
        if choice.isdigit():
            #Range Check
            if int(choice) in range(1,10):
                return int(choice)
            print('You are out of acceptable range. (1-9)')
            continue
        print('Sorry! that was not a digit.')

#Function Calls
while game_on:
    
    #display(game_list)
    #player_input()
    #place_marker(game_list,'S',1)
    #win_check(game_list," ")
    #gameon_choice()
    #space_check(game_list,2)
    #game_on = gameon_choice()