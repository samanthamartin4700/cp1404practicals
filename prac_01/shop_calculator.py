number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total = 0
for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total = total + price_of_item
if total > 100:
    discount = total - (total * 0.1)
    print(f"Total price for {number_of_items} items is ${discount}")
else:
    print("Total price for", number_of_items, "items is $", total)