from prac_07.guitar import Guitar


def main():
    index = 0
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year:"))
    cost = float(input("Cost"))
    guitars.append(Guitar(name, year, cost))
    print(guitars[index], "added")
    while name != "":
        name = input("Name: ")
        if name != "":
            index += 1
            year = int(input("Year:"))
            cost = float(input("Cost"))
            guitars.append(Guitar(name, year, cost))
            print(guitars[index], "added")

    print("These are my guitars:")
    guitar_number = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(guitar_number, guitar.name, guitar.year,
                                                                   guitar.cost, vintage_string))
        guitar_number += 1


main()
