# import libraries
import csv
import string


# Biography info
# Ask a user for their personal information
# one question at a time. Then check that the
# information they entered is valid. Finally,
# print a summary of all the information they entered back to them.
def biography_info():
    # ask the user for input
    print("Welcome to your Autobiography")
    print("answer the following question to auto generate your personal biography")
    first_name = input("what is your name? : ")
    last_name = input("what is your last name? : ")
    dob_year = int(input("what year were you born? : "))
    print("Jan., Feb., Mar., Apr., May., Jun., Jul., Aug., Sep., Oct., Nov., Dec.,")
    dob_month = input("which month were you born in? : ")
    dob_date = int(input("enter the date you were born : "))
    print("Monday., Tuesday., Wednesday., Thursday., Friday., Saturday., Sunday.,")
    dob_day = input("which day were you born? : ")
    address = input("where do you live? : ")
    personal_goal = input("do you have any personal goals? : ")
    print("okay, thank you for your answers...wait while we create your profile")
    print("loading.....%")
    print("loading..........%")
    print("loading.................%")
    print("done")
    print("*****************************************************************************")
    print("- Name          : ", last_name, first_name)
    print("- DOB           : ", dob_month, ", ", dob_date, " (", dob_day, ") ,", dob_year)
    print("- Address       : ", address)
    print("- Personal Goal : ", personal_goal)
    print("*****************************************************************************")


# Word count
# Ask the user what's on their mind.
# Then after the user responds,
# count the number of words in the sentence and print that as an output.
def word_counter():
    # Ask the user what's on their mind.
    # user_input = input("what's on your mind : ")
    translator = str.maketrans('', '', string.punctuation)
    word_count = {}
    text = open('declaration.txt').read()
    words = text.split()
    for word in words:
        word = word.translate(translator).lower()
        count = word_count.get(word, 0)
        count += 1
        word_count[word] = count

    word_count_list = sorted(word_count, key=word_count.get, reverse=True)
    for word in word_count_list[:10]:
        print(word, word_count[word])

    output_file = open('words.csv', 'w')
    writer = csv.writer(output_file)
    writer.writerow(['word', 'count'])
    for word in word_count_list:
        writer.writerow([word, word_count[word]])


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

    while loop < 2:
        # all the questions that the program asks the user
        noun = input("choose a noun : ")
        p_noun = input("choose a plural_noun : ")
        noun2 = input("choose a noun : ")
        place = input("name a place : ")
        adjective = input("choose an adjective (describing word) : ")
        noun3 = input("choose a noun : ")
        # displays the story based on the users input
        print("---------------------------------------------")
        print(user_input)
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
    number_input = int(input("What number are you thinking of? : "))

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
    # even_or_odd()
    # mad_libs()
    # word_counter()
    biography_info()