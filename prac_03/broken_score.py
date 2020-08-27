"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(get_status(score))

def get_status(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

import random
score = random
print("Random score:", get_status(score.randint(0, 100)))

main()