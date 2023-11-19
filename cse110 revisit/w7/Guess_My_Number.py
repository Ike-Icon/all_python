"""In the Guess My Number game the computer picks a magic number,
and then the user tries to guess it. After each guess, the computer tells 
the user to guess "higher" or "lower" until they guess the magic number."""
import random

play_again = "yes"

# STRETCH CHALLENGE
while play_again == "yes":
    magic_num = random.randint(1, 10)
    # print(number)

    # Start by asking the user for the magic number.
    # magic_num = int(input("What is the magic number? "))

    guess_num = ""

    count_guess = 0

    while guess_num != magic_num:
        # Ask the user for a guess.
        guess_num = int(input("What is your guess? "))
        count_guess = count_guess + 1

        if guess_num < magic_num:
            print("Higher")
        elif guess_num > magic_num:
            print("Lower")
        else:
            print(f"You guessed it! the number is {magic_num}")

    # STRETCH CHALLENGE
    print(f"\nIt took you {count_guess} time to guess the number")
    play_again = input("\nDo you wanna play again? yes/no. ")

print("\nThank you for playing. Goodbye.")
