# Use a while loop to ask the user for a positive number (>= 0).

number = int(input("Please type a positive number: "))

# Continue asking as long as the number is negative, then display the number.
while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))


print(f"The number is: {number}")


# Ask for candy

ask_candy = "no"

while ask_candy == "no":
    ask_candy = input("May I have a piece of candy? ")
    
print("Thank You")

