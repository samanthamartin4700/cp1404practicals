from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxi_choices = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 100, 2)]
    total_cost = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            taxi_menu(taxi_choices)
            taxi_choice = int(input("Choose taxi: "))
            taxi = taxi_choices[taxi_choice]
        elif choice == "D":
            taxi.start_fare()
            driving_distance = float(input("Drive how far? "))
            taxi.drive(driving_distance)
            cost = taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi.name, cost))
            total_cost += cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        choice = input(">>>").upper()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    taxi_menu(taxi_choices)

def taxi_menu(taxi_choices):
    for number, taxi in enumerate(taxi_choices):
        print("{} - {}".format(number, taxi))

main()