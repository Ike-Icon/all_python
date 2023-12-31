"""For this project you will create a program that stores a list of products
 in a shopping cart along with their prices. The user should have the ability 
 to add items to the list, remove them, and see the total price of the cart."""

print("\nWelcome to the Shopping Cart Program!")
menu = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]

# Create a list that will store the names of the items in the shopping cart.
shopping_cart = []
prices = []

user_menu = 0

# Have menu system that repeats until the user chooses quit.
while user_menu != 5:
    print("\nPlease select one of the following: ")
    for opt in menu:
        print(opt)
    user_menu = int(input("Please enter an action: "))

    # Add a new item
    if user_menu == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? $"))
        shopping_cart.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")

    # Display the contents of the shopping cart
    elif user_menu == 2:
        print("\nThe contents of the shopping cart are: ")
        # The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
        for i in range(1, len(shopping_cart) + 1):
            if 1 <= i <= len(shopping_cart) and 1 <= i <= len(prices):
                item = shopping_cart[i - 1]
                price = prices[i - 1]
                print(f"{i}. {item} - ${price}")

    # Remove an item
    elif user_menu == 3:
        removeItem = int(input("\nWhich item would you like to remove? "))
        shopping_cart.pop(removeItem - 1)
        prices.pop(removeItem - 1)
        print("Item Removed")

        # make sure then user removes an item in the length of the shopping cart
        # for removeItem in range(1, len(shopping_cart) + 1):
        #     if removeItem > len(shopping_cart):
        #         print("The item is not in the shopping cart")

    # Compute the total
    elif user_menu == 4:
        totalAmount = 0
        for price in prices:
            totalAmount += price
        print(f"The total amount is: {totalAmount:.2f}")

    # Quit
    else:
        user_menu == 5
        print("Thank you. Goodbye.")
        break
