"""Programs can obtain information from users and then combine those values to 
compute meaningful results. In this assignment, you will write 
a program to calculate the price of a meal."""

# Ask the user for the price of a child's meal
child_meal = float(input("What is the price of child's meal? $"))

# Ask the user for the price of a adult's meal
adult_meal = float(input("\nWhat is the price of adult's meal? $"))

# Ask the user for the number of children
num_children = int(input("\nWhat is the number of children? "))

# Ask the user for the number of adults
num_adults = int(input("\nWhat is the number of adults? "))

# Ask the user for the sales tax rate
tax_rate = float(input("\nWhat is the sales tax rate? "))

# Compur the meal's subtotal (before adding sales tax)
child_total = child_meal * num_children
adult_total = adult_meal * num_adults

subtotal = child_total + adult_total

print(f"\nSubtotal: ${round(subtotal, 2)}")

# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100
sales_tax = subtotal * tax_rate/100

print(f"Sales Tax: ${round(sales_tax, 2)}")

# Compute and display the total price of the meal by adding the subtotal and the sales tax.
total_price = subtotal + sales_tax

print(f"Total Price: ${round(total_price, 2)}")

# Ask the user for the the payment amount
pay_amount = float(input("\nWhat is the payment amount? $"))

# Compute and display the change
change = pay_amount - total_price

print("Change: ${}".format(round(change, 2)))