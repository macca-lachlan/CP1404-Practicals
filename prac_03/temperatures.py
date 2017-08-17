"""
CP1404 - Practical 01
Pseudocode for temperature conversion
"""


def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit = celsius_to_fahrenheit(fahrenheit)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = float(input("Celsius: "))
            celsius = fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
