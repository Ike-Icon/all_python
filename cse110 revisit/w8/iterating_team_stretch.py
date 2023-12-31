# STRETCH CHALLENGE
"""
Start a new program that will work similar to one from the core requirements,
but use a different string, this time using the following quote from President Nelson:
"""
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

play_again = "yes"

while play_again.lower() == "yes":
   
    #  asks for a number n. Make the program capitalize every n-th letter in the string.
    x = int(input("Please enter a number: "))

    for n, letter in enumerate(quote):
        # print(f"letter {letter_2} at position {n}")

        if n % x == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    print("")
    
    play_again = input("Would you like to enter another number? ")
    if play_again.lower() == "no":
        print("Goodbye")
        break
