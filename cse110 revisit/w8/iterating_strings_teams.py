"""Write a program that asks the user for their favorite letter.
 Then, loop through a programmed word one letter at a time. If the letter in the programmed 
 word is the user's favorite, print it out as a capital letter (or "hide" it), if not, print 
 it out as a lower case letter."""

word = "Commitment"
user_letter = input("What is your favorite letter? ")

#  2)
# for letter in word:
#     if user_letter.lower() == letter:
#         print(letter.upper(), end="") #use end="" to print on the same line.
#     else:
#         print(letter.lower(), end="")


# 3)
for letter in word:
    if user_letter.lower() == letter:
        print("_", end="")  # use end="" to print on the same line.
    else:
        print(letter.lower(), end="")


