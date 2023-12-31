import random


def generate_hint(secret_word, correct_guesses):
    hint = ""
    for letter in secret_word:
        if letter in correct_guesses:
            hint += letter.upper()
        else:
            hint += "_"
    return hint


def main():
    secret_word = "python"  # Replace with your secret word
    secret_word_length = len(secret_word)

    print("Welcome to the Guess the Word Game!")

    guesses = 0
    correct_guesses = []

    while True:
        user_guess = input("Enter your guess: ").lower()

        # Check if the length of the guess is correct
        if len(user_guess) != secret_word_length:
            print("Invalid guess. Please enter a guess with the correct length.")
            continue

        guesses += 1

        # Check if the guess is correct
        if user_guess == secret_word:
            print(
                f"Congratulations! You guessed the word '{secret_word}' in {guesses} guesses."
            )
            break

        # Generate and display the hint
        hint = generate_hint(secret_word, correct_guesses)
        print(f"Hint: {hint}")

        # Check for correct letters at correct positions and update correct_guesses
        for i in range(secret_word_length):
            if user_guess[i] == secret_word[i]:
                correct_guesses.append(user_guess[i])

    print("Game Over!")


if __name__ == "__main__":
    main()
