# Practice the mechanics of if statements.


num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".
if num1 > num2:
    print("\nThe first number is greater")
else:
    print("The second number is greater")

# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal"
if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".
if num2 < num1:
    print("The second number is greater")
else:
    print("The second number is not greater")


my_animal = "dog"
animal = input("\nWhat is your favorite animal? ")

if animal.lower() == my_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")