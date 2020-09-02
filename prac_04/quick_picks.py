# I did use the solutions to help me with parts of this question
MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBER_PER_LINE = 6
import random

quick_picks = int(input("How many quick picks? "))
while quick_picks <= 0:
    print("Number of quick picks must be > 0")
    quick_picks = int(input("How many quick picks? "))

for i in range(0, quick_picks):
    quick_pick = []
    for j in range(NUMBER_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))