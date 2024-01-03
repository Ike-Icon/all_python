"""
write a Python program named discount.py that gets a customer’s subtotal as input
and gets the current day of the week from your computer’s operating system. Your program 
must not ask the user to enter the day of the week. Instead, it must get the day of the
week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday,
your program must subtract 10% from the subtotal. Your program must then compute the
total amount due by adding sales tax of 6% to the subtotal. Your program must print the 
discount amount if applicable, the sales tax amount, and the total amount due.
"""
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()
time_now = current_date_and_time.time()

# print(day_of_week, time_now)


# function to computes and prints the discount amount if applicable.
def get_discount_amount(day_of_week, subtotal):
    if subtotal >= 50:
        if day_of_week == 1 or day_of_week == 2:
            discount_amount = subtotal - subtotal * 0.1
    else:
        discount_amount = subtotal

    return discount_amount


# Function to compute the sales tax for the subtotal amount
def compute_sales_tax(subtotal):
    sales_tax = subtotal * 0.06

    return sales_tax


# Fnction for computing the total amount due by adding sales tax of 6% to the subtotal
def get_total_amount(subtotal, sales_tax):
    total = subtotal + sales_tax
    return total


# Funtion to compute and print the difference between $50 and the subtotal for the user to get the discount
def compute_difference(subtotal):
    if day_of_week == 1 or day_of_week == 2:
        if subtotal < 50:
            difference = 50 - subtotal
    return difference


# Ask the user for the subtotal amount
# subtotal = float(input("Please enter the subtotal: "))

# replace the code that asks the user for the subtotal with a loop
# that repeatedly asks the user for a price and a quantity and computes the subtotal.
print("Enter the price and quantity for each item.")
subtotal = 0
price = 1
while price != 0:
    price = float(input("Enter the price of the item: "))
    if price != 0:
        quantity = int(input("Enter the quantity of the item: "))

        subtotal += price * quantity
    print()

# Call the function which computes the discount if the day of the week is Teuesday or Wednesday
discount = get_discount_amount(day_of_week, subtotal)

# call the funtion that computes the sales tax
salesTax = compute_sales_tax(discount)
print()

# print the sales tax amountfor the user
print(f"Sales tax amount: {salesTax:.2f}")


diff_to_discount = compute_difference(subtotal)

total = get_total_amount(discount, salesTax)

# if the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount.
if subtotal >= 50:
    if day_of_week == 1 or day_of_week == 2:
        print(f"The amount after the discount is: {discount:.2f}")
else:
    if day_of_week == 1 or day_of_week == 2:
        print(f"Purchase {diff_to_discount:.2f} more to get discount")

# Display the total for the user to see.
print(f"The total amount is: {total:.2f}")
