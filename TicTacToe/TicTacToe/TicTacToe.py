#Variables
game_list = [0,1,2]
game_on = True

def display(game_list: list):
    print("Here is the current list")
    print(game_list)

def position_choice():

    choice = 'wrong'

    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0','1','2']:
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

    position = position_choice()

    game_list = replacement_choice(game_list, 1)

    display(game_list)

    game_on = gameon_choice()