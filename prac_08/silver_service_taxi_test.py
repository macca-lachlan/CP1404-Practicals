from prac_08.silver_service_taxi import SilverServicetaxi


def main():
    hummer = SilverServicetaxi("Hummer", 200, 2)
    print(hummer)
    hummer.drive(18)
    print("${:.2f}".format(hummer.get_fare()))

main()
