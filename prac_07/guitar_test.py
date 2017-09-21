from prac_07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012)

    print(gibson)
    print("Gibson.get_age() - Expected 95. Got {}".format(str(gibson.get_age())))
    print("another_guitar get_age() - Expected 5. Got {}".format(str(another_guitar.get_age())))
    print("gibson.is_vintage() - Expected True. Got {}".format(str(gibson.is_vintage())))
    print("another_guitar.is_vintage() - Expected False. Got {}".format(str(another_guitar.is_vintage())))


main()