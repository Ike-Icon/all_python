"""Many games and puzzles require iteration where a person (or a computer) repeats the same steps for
each piece in the game or each spot in a puzzle. For this assignment, you will create an interactive
word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way."""

# The program contains a hidden secret word stored in a variable.
secret_word = "book"

count = 1
print("\nWelcome to the word guessing game!")
# The program asks the user to guess a letter.

guess = input("\nWhat is your guess? ")

# The program compares the guess to the secret word.
while guess.lower() != secret_word.lower():
    count += 1
    print("Nope, try again.")
    guess = input("What is your guess? ")
    if guess == secret_word:
        print("\nCongratulations! You guessed it!")

if count == 1:
    print("\nCongratulations! You guessed it!")
    print(f"It took you {count} guess.")
else:
    print(f"It took you {count} guesses.")
