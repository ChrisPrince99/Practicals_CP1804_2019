CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        age = self.get_age()
        if age >= VINTAGE_AGE:
            return True
        else:
            return False
