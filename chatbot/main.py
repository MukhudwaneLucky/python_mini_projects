# This is a sample Python script.


# Press the green button in the gutter to run the script.
from greeting import Greeting

if __name__ == '__main__':
    dialog = Greeting()
    # listen returns (response, confidence) tuples just print the response
    print(dialog.listen("Hello!", user="lucky14")[0])
    print(dialog.listen("my name is Lucky", user="lucky14")[0])
    print(dialog.listen("Roll call!", user="lucky14")[0])
    print(dialog.listen("have to go, goodbye!", user="lucky14")[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
