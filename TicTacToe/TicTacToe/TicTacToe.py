row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    return 

def user_choice():
    #VARIABLES

    #Initial
    choice = 'WRONG'
    acceptable_range = range(0,11)
    within_range = False

    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE==False
    while choice.isdigit() == False or within_range == False:

        choice = input("Please Enter a number (0-10): ")

        #DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range == True
            else:
                print("You are out of the acceptable range (0-10)")
                within_range = False

    return int(choice)
user_choice()
display(row1,row2,row3)