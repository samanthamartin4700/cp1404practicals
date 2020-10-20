"""
CP1404 Practical
Unreliable Car
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super.__init__(name, fuel)
        self.reliability = reliability

    def test_drive(self, distance):
        random_value = randint(1, 100)
        if self.reliability <= random_value:
            distance = 0
        drive = super().test_drive(distance)
        return drive