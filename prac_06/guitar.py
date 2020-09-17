PRESENT_YEAR = 2020
VINTAGE_AGE = 50

class Guitar:
    """Store guitar details"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string for Guitar object"""
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return PRESENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE