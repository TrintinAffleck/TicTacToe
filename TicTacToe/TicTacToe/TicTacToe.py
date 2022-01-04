#Variables
game_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_on = True

def clear():
    print("\n"*100)

def display(game_list: list):
    print("Here is the current list")
    print(game_list[7] + '|' + game_list[8] + '|' + game_list[9])
    print(game_list[4] + '|' + game_list[5] + '|' + game_list[6])
    print(game_list[1] + '|' + game_list[2] + '|' + game_list[3])
    

def player_input():

    marker = ' '

    while marker != 'X' or 'O':
        marker = input("Please choose your marker (X or O)")

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)



def position_choice():

    choice = 'wrong'

    while choice not in range(1-10):
        
        choice = input("Pick a position (1-9): ")

        if choice not in range(1-10):
            print("Sorry, invalid choice!")

    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")

    #position = position_choice()
    game_list[position] = user_placement
    print(game_list)
    return game_list

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','y','N','n']:
        
        choice = input("Keep Playing? (Y or N) ")

        if choice not in ['Y','y','N','n']:
            print("Please choose Y or N ")

    if choice == 'Y' or 'y':
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

    display(game_list)
    player_input()

    #position = position_choice()

    #game_list = replacement_choice(game_list, 1)

    #display(game_list)

    #game_on = gameon_choice()