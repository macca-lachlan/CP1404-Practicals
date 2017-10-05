from prac_08.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("car", 100, 50)
    car.drive(60)
    print(car)


main()