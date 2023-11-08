"""Write a program that determines the letter grade for a course according to the following scale:
A >= 90
B >= 80
C >= 70
D >= 60
F < 60 """

# Ask the user for their grade percentage
grade = float(input("What is your grade percentage? "))

# print out the appropriate letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"


# For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.
sign = ""

if grade % 10 >= 7:
    sign = "+"
elif grade % 10 < 3:
    sign = "-"
else:
    sign = " "

if grade >= 93:
    sign = ""

if grade < 60:
    sign = ""

print(f"Your letter grade is: {letter}{sign}")


# if student had at least 70, they passed the class. Add a separate if statement to determine if the user passed the course, 
# and if so display a message to congratulate them
if grade >= 70:
    print("\nCongratulation, you passed the class")
else:
    print("Fail, better luck next time")