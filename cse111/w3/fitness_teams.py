"""Health professionals who are helping a client achieve a healthy body weight,
 sometimes use two computed measures named body mass index and basal metabolic rate.

From the U.S. Centers for Disease Control and Prevention we read,

      10,000 weight
bmi = ---------------
      height**2
where weight is in kilograms and height is in centimeters.

Basal metabolic rate (BMR) is the minimum number of calories required daily 
to keep your body functioning at rest. BMR is different for women and men
and changes with age. The revised Harris-Benedict formulas for computing BMR are

(women)  bmr = 447.593 + 9.247 weight + 3.098 height - 4.330 age
(men)  bmr = 88.362 + 13.397 weight + 4.799 height - 5.677 age

where weight is in kilograms and height is in centimeters.
"""
from datetime import datetime


def main():
    # Ask the user for their gender
    gender = input("Please enter your gender (M or F): ")

    # Ask for the date of birth
    birthdate = input("Enter birthdate(YYYY-MM-DD): ")

    weight = float(input("Enter your weight in U.S. pounds: "))

    height = float(input("Enter your height in U.S. inches: "))

    # call the age function to compute the age
    age = compute_age(birthdate)

    # call the function to convert from pounds to kilograms
    weight_in_kg = kg_from_lb(weight)

    # call the function to convert from inches to centimeters
    height_in_cm = cm_from_in(height)

    # Call the function to compute the BMI 
    BMI = body_mass_index(weight_in_kg, height_in_cm)

    # Call the function to compute the BMR
    BMR = basal_metabolic_rate(gender, weight_in_kg, height_in_cm, age)

    # Stretch Challenges
    height_in_meters = m_from_cm(height_in_cm)

    # print the age for the user to see
    print(f"Age (years): {age}")

    print(f"Weight (kg): {weight_in_kg:.2f}")

    # print(f"Height (cm): {height_in_cm:.2f}")
    print(f"Height (m): {height_in_meters:.2f}")

    print(f"Body mass index: {BMI:.1f}")

    print(f"Basal metabolic rate (kcal/day): {round(BMR)}")



def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (
        birthdate.month == today.month and birthdate.day > today.day
    ):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    mass_in_kg = pounds * 0.45359237

    return mass_in_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    length_cm = inches * 2.54

    return length_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000 * weight / (height**2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == 'F':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

    else:
        gender == 'M'
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    
    return bmr


# Stretch Challenges
# Define a function to convert height from cm to m 
def m_from_cm(centimeters):
    height_m = centimeters * 0.01

    return height_m

# Call the main function so that
# this program will start executing.
main()
