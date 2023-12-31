# loop through the number and find the positive number.
number = int(input("Please type a positive number: "))

# Continue asking as long as the number is negative, then display the number.
while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))
    
    
print(f"\nThe number is: {number}")