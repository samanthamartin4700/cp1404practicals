from prac_08.taxi import Taxi

def main():
    test_taxi = Taxi("Prius 1", 100)
    test_taxi.drive(40)
    print(test_taxi)

    test_taxi.start_fare()
    test_taxi.drive(100)
    print(test_taxi)
    print(test_taxi.get_fare())

main()