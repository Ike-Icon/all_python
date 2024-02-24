"""Rosenberg self-esteem scale. Your program must ask the user to respond to each of the ten poss
with D, d, a, or A which mean strongly disagree, disagree, agree, and strongly agree. Your program
must compute the score for each answer and sum and display the person’s total score.
You should think about how you will separate this program into functions 
before you begin writing the program.
"""


# Define the main function to handle the program.
def main():
    display_intro()

    score = 0
    print()

    score += compute_pos_score(
        "1. I feel that I am a person of worth, at least on an equal plane with others."
    )

    score += compute_pos_score("2. I feel that I have a number of good qualities.")

    score += compute_neg_score(
        "3. All in all, I am inclined to feel that I am a failure."
    )

    score += compute_pos_score(
        "4. I am able to do things as well as most other people."
    )

    score += compute_neg_score("5. I feel I do not have much to be proud of.")

    score += compute_pos_score("6. I take a positive attitude toward myself.")

    score += compute_pos_score("7. On the whole, I am satisfied with myself.")

    score += compute_neg_score("8. I wish I could have more respect for myself.")

    score += compute_neg_score("9. I certainly feel useless at times.")

    score += compute_neg_score("10. At times I think I am no good at all.")

    print(f"the score is:{score}")
    print("A score below 15 may indicate problematic low self-esteem.")
    print()

    display_nr6_intro()
    nr_score = 0
    nr_score += get_nature_relatedness_scale(
        "1. My ideal vacation spot would be a remote, wilderness area."
    )
    nr_score += get_nature_relatedness_scale(
        "2. I always think about how my actions affect the environment."
    )
    nr_score += get_nature_relatedness_scale(
        "3. My connection to nature and the environment is a part of my spirituality."
    )
    nr_score += get_nature_relatedness_scale(
        "4. I take notice of wildlife wherever I am."
    )
    nr_score += get_nature_relatedness_scale(
        "5. My relationship to nature is an important part of who I am."
    )
    nr_score += get_nature_relatedness_scale(
        "6. I feel very connected to all living things and the earth."
    )

    actual_nr_score = nr_score / 6
    print(f"Your NR-6 score is: {actual_nr_score}")

# Define a function to display the introdutory information.
def display_intro():
    print(
        "\nThis program is an implementation of the Rosenberg"
        "\nSelf-Esteem Scale. This program will show you ten"
        "\nposs that you could possibly apply to yourself."
        "\nPlease rate how much you agree with each of the"
        "\nposs by responding with one of these four letters:"
    )
  
    print(
        "\nD means you strongly disagree with the pos."
        "\nd means you disagree with the pos."
        "\na means you agree with the pos."
        "\nA means you strongly agree with the pos."
    )


# Define a function to calculate the score of the person's self esteem.
def compute_pos_score(statement):
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == "A":
        score = 3 

    elif answer == "a":
        score = 2     

    elif answer == "d":
        score = 1 

    elif answer == "D":
        score = 0 

    return score


def compute_neg_score(statement):
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == "A":
        score = 0 

    elif answer == "a":
        score = 1 

    elif answer == "d":
        score = 2 

    elif answer == "D":
        score = 3 

    return score


# Stretch Challenges
def display_nr6_intro():
    print("Version of the Nature Relatedness Scale (NR-6)")

    print(
        "\nD means you strongly disagree with the statement."
        "\nd means you disagree with the statement."
        "\nN means you neither disagree or agree with the statement."
        "\na means you agree with the statement."
        "\nA means you strongly agree with the statement."
    )


# Short Form Version of the Nature Relatedness Scale (NR-6)
def get_nature_relatedness_scale(statement):
    print(statement)
    answer = input("Enter D, d, n, a, or A: ")
    score = 0
    if answer == "A":
        score = 5
    elif answer == "a":
        score = 4
    elif answer == "N":
        score = 3
    elif answer == "d":
        score = 2
    elif answer == "D":
        score = 1

    return score

if __name__ == "__main__":
    main()
