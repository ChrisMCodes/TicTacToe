#!/usr/bin/env

# Tic-Tac-Toe!
# Requires two players

# First a place to store all those Xs and Os
field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
over = False

def display_field(field):
    '''displays the game board and returns True if someone won (or if there is a draw) and False otherwise'''
    # for readability
    # tl = top left, br = bottom right, etc
    winner = False
    tl = field[0]
    tc = field[1]
    tr = field[2]
    ml = field[3]
    mc = field[4]
    mr = field[5]
    bl = field[6]
    bc = field[7]
    br = field[8]

    draw = check_draw(field)
    
    print("----------")
    print("| {} {} {} |".format(tl, tc, tr))
    print("| {} {} {} |".format(ml, mc, mr))
    print("| {} {} {} |".format(bl, bc, br))
    print("----------")

    # Checks for a winner
    if tl == tc and tc == tr and tr != " ":
        print("{} wins!".format(tl))
        winner = True
    elif ml == mc and mc == mr and mr != " ":
        print("{} wins!".format(tl))
        winner = True
    elif bl == bc and bc == br and br != " ":
        print("{} wins!".format(br))
        winner = True
    elif tl == ml and ml == bl and bl != " ":
        print("{} wins!".format(bl))
        winner = True
    elif tc == mc and mc == bc and bc != " ":
        print("{} wins!".format(bc))
        winner = True
    elif tr == mr and mr == br and br != " ":
        print("{} wins!".format(br))
        winner = True
    elif tr == mc and mc == bl and bl != " ":
        print("{} wins!".format(bl))
        winner = True
    elif tl == mc and mc == br and br != " ":
        print("{} wins!".format(br))
        winner = True
    elif draw:
        print("Draw.") 
        winner = True
    else:
        print("No winner yet!")
        winner = False
    return winner


def check_draw(field):
    '''Checks to make sure there is no draw'''
    for i in field:
        if i == " ":
            return False
    return True

def choose_move(field):
    '''Displays a sample field to the user and allows the user to choose their move'''
    choices = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    validate = []
    valid = False

    count = 0
    for i in field:
        if i == " ":
            choices[count] = count + 1
            validate.append(str(choices[count]))
            count += 1
        else:
            holder = i
            choices[count] = holder
            count += 1

    print("Please choose a number for your next move: ")
    print("----------")
    print("| {} {} {} |".format(choices[0], choices[1], choices[2]))
    print("| {} {} {} |".format(choices[3], choices[4], choices[5]))
    print("| {} {} {} |".format(choices[6], choices[7], choices[8]))
    print("----------")


    # some minor exception handling
    while not valid:
        choice = input(">")
        if choice in validate:
            valid == True
            choice = int(choice)
            field = x_or_o(field, choice)
            return field
        else:
            print("Sorry, your input was not recognized.")
    return field

def x_or_o(field, choice):
    '''determines whether it was X or O's turn, completes the board accordingly'''
    count_x = len([i for i in field if i == "X"])
    count_o = len([i for i in field if i == "O"])

    if count_x > count_o:
        field[choice - 1] = "O"
        return field
    else:
        field[choice - 1] = "X"
        return field


# Here's a fun sample new game

while not over:
    field = choose_move(field)
    over = display_field(field)
    
