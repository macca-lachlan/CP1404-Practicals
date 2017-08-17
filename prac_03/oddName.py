"""
Lachlan McDonald
"""


def main():
    username = get_name()
    letter_frequency = get_number()
    print_name(username, 2)


def print_name(username, frequency):
    for i in range(0, len(username), frequency):
        print(username[i])


def get_name():
    username = input("What is your name? :")
    while len(username) == 0:
        print("You need to enter your name")
        username = input("What is your name? :")
    return username


def get_number():
    checker = True
    while checker:
        try:
            number = int(input("please enter a number"))
            if number > 0:
                checker = False
        except ValueError:
            print("invalid input")
    return number

main()
