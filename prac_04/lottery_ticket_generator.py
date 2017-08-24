import random


def main():

    number_of_quick_picks = int(input("how many quick picks do you wish to generate? :"))
    for i in range(1, number_of_quick_picks + 1):
        numbers = []
        numbers.append(random.randint(1, 45))
        while len(numbers) < 6:
            number = random.randint(1, 45)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        print(numbers)


main()
