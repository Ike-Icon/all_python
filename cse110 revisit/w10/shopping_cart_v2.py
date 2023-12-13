"""For this project you will create a program that stores a list of products
 in a shopping cart along with their prices. The user should have the ability 
 to add items to the list, remove them, and see the total price of the cart."""

print("\nWelcome to the Shopping Cart Program!")
menu = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]

shopping_cart = []
prices = []

user_menu = 0

# Have menu system that repeats until the user chooses quit.
while user_menu != 5:
    print("\nPlease select one of the following: ")
    for opt in menu:
        print(opt)
    user_menu = int(input("Please enter an action: "))

    if user_menu == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? $"))
        shopping_cart.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif user_menu == 2:
        print("\nThe contents of the shopping cart are: ")
        # for i in enumerate(range(len(shopping_cart, start=1))):
        #     item = shopping_cart[i]
        #     price = prices[i]
        #     print(f"{i}. {item} - ${price}")
        for i, item in enumerate(shopping_cart, start=1):
            for i in range(len(prices)):
                price = prices[i]
            print(f"{i}. {item} - ${price}")

    elif user_menu == 3:
        user_menu = menu[2]
    elif user_menu == 4:
        user_menu = menu[3]
    else:
        user_menu == 5
        user_menu = menu[4]
        print("Thank you. Goodbye.")
        break

# print(shopping_cart)
