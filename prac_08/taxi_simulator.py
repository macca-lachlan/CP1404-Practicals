from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServicetaxi

MENU = " q)uit \n c)hoose taxi \n d)rive"


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServicetaxi("Limo", 100, 2), SilverServicetaxi("Hummer", 200, 4)]
    user_menu_choice = menu()
    bill = 0
    user_taxi_choice = 0
    while user_menu_choice.upper() != "Q":
        if user_menu_choice.upper() == "C":
            for taxi_number, taxi in enumerate(taxis):
                print("{} - {}".format(taxi_number, taxi))
            user_taxi_choice = int(input("Choose taxi: "))
            print("Bill to date ${:.2f}".format(bill))
        elif user_menu_choice.upper() == "D":
            taxis = ride_taxi(taxis, user_taxi_choice)
            print("Your {} trip cost you ${:.2f}".format(taxis[user_taxi_choice].name,
                                                         taxis[user_taxi_choice].get_fare()))
            bill += taxis[user_taxi_choice].get_fare()
            print("Bill to date ${:.2f}".format(bill))
        user_menu_choice = menu()
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    for taxi_number, taxi in enumerate(taxis):
        print("{} - {}".format(taxi_number, taxi))


def menu():
    print(MENU)
    user_choice = input(">>> ")
    return user_choice


def ride_taxi(taxis, taxi_number):
    distance = int(input("Drive how far? "))
    taxis[taxi_number].drive(distance)
    return taxis

main()
