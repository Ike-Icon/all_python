
# number = 0

# Use a while loop to ask the user for a positive number (>= 0). 

number = -1

# Continue asking as long as the number is negative, then display the number.
while number < 0:
    number = int(input("Please type a positive number: "))
    print("Sorry, that is a negative number. Please try again.")

print(f"The number is: {number}")
