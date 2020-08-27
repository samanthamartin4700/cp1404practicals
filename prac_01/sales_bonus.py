"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        ten_percent_bonus = sales * 0.1
        # total_ten_percent_bonus = ten_percent_bonus + sales
        print("Your total bonus is $", ten_percent_bonus)
    else:
        fifteen_percent_bonus = sales * 0.15
        # total_fifteen_percent_bonus = fifteen_percent_bonus + sales
        print("Your total bonus is $", fifteen_percent_bonus)
    sales = float(input("Enter sales: $"))
print("done")