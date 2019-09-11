from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)

    print(guitar.name, "get_age() - Expected 97. Got", guitar.get_age())
    print(guitar.name, "is_vintage() - Expected True. Got", guitar.is_vintage())


main()
