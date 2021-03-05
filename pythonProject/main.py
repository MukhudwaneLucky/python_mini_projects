# Mad libs game

# Ask the user for an input.
# This could be anything such as a name,
# an adjective, a pronoun or even an action.
# Once you get the input, you can rearrange it to build up your own story.

def mad_libs():
    # ask the user for input
    user_input = input("enter a name,an adjective, a pronoun or even an action :")
    # loop back to this point once code finishes
    loop = 1

    while loop < 10:
        # all the questions that the program asks the user
        noun = input("choose a noun : ")
        p_noun = input("choose a plural_noun : ")
        noun2 = input("choose a noun : ")
        place = input("name a place : ")
        adjective = input("choose an adjective (describing word) : ")
        noun3 = input("choose a noun")
        # displays the story based on the users input
        print("---------------------------------------------")
        print("Be kind to your", noun, "- footed", p_noun)
        print("For a duck maybe somebody's", noun2, ",")
        print("Be kind to your", p_noun, "in ", place)
        print("Where the weather is always", adjective, ".")
        print()
        print("you may think that is this the", noun3, ",")
        print("well it is...")
        print("---------------------------------------------")
        # loop back to 'loop = 1'
        loop += 1


# This is a sample Python script.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def even_or_odd():
    # Welcome a user then ask them for a number between 1 and 1000.
    #
    # When the user gives you the number,
    # you check if it's odd or even and
    # then you print a message letting them know.

    # get user input
    print("Welcome to Odd or Even!")
    print("Enter a number between 1 and 1000")
    number_input = int(input("What number are you thinking of?"))

    # check if the number is in range
    if number_input > 1000 or number_input < 1:
        print("Eish...wrong value...try again. Enter a number between 1 and 1000")

    # check if its even or odd
    if number_input % 2 == 0:
        print("That's an Even number")
    else:
        print("That's an Odd number")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome...')
    even_or_odd()
    mad_libs()

