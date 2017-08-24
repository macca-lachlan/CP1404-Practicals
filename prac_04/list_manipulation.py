
def main():
    numbers = get_numbers_from_user()
    display_list_manipulation(numbers)


def get_numbers_from_user():
    numbers = []
    for i in range(0, 5):
        value = input("please enter a number :")
        numbers.append(value)
    return numbers


def display_list_manipulation(numbers):
    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(numbers[len(numbers)-1]))
    print("the smallest number is {}".format(min(numbers)))
    print("the largest number is {}".format(max(numbers)))


main()
