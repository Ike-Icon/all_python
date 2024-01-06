"""Write a program named tire_volume.py that computes the approximate volume of air 
inside a tire. Add code near the end of that program that does the following:

1. Gets the current date from the computer’s operating system.
2. Opens a text file named volumes.txt for appending.
3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire
"""

"""
The size of a car tire in the United States is represented with three
numbers like this: 205/60R15. The first number is the width of the tire in millimeters.
The second number is the aspect ratio. The third number is the diameter in inches of
the wheel that the tire fits. The volume of space inside a tire can be approximated 
with this formula:

 
    π*w**2*a(w*a + 2,540*d)
v = --------------------
    10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the
 circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
import math
from datetime import datetime


def main():
    # Ask the user for the width of the tire in mm
    width = int(input("Enter the width of the tire in mm (ex 205): "))

    # Ask the user for the aspect ratio of the tire
    aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))

    # Ask the user for the diameter of the tire in inches
    diameter = int(input("Enter the diameter of the tire in inches (ex 15): "))

    tireVolume = get_volume(width=width, ratio=aspectRatio, diameter=diameter)

    # Add a set of if … elif … else statements in your program that use the tire width,
    # tire aspect ratio, and wheel diameter that the user enters to find a price and then print the price.
    if width >= 195 and diameter >= 55 and aspectRatio >= 13:
        price = 100.00

    elif width >= 180 and diameter >= 50 and aspectRatio >= 12:
        price = 90.00

    elif width >= 170 and diameter >= 45 and aspectRatio >= 11:
        price = 80.00

    else:
        price = 70.00

    # Print the approximate volume of the tire in liters
    print(f"\nThe approximate volume is {tireVolume:.2f} liters")
    print(f"The Price is ${price}")

    # ask the user if she wants to buy tires with the dimensions that she entered.

    # If the user answers “yes”, your program should ask for her phone number
    # and store her phone number in the volumes.txt file.
    buy_tire = input("Do you want to buy dimensions you entered? (yes/no): ")

    if buy_tire == "yes":
        tele_num = int(input("Enter your telephone number: "))
        print("Thank you for the purchase!")
    else:
        tele_num = ""
        print("Thank you for passing by, Goodbye!")

    # Call the now() method to get the current date and time
    current_date_and_time = datetime.now()

    # Use an f-string to print only the date part of the current date and time.
    print(f"\nDate: {current_date_and_time:%Y-%m-%d}")

    with open("volumes.txt", "at") as volumes_file:
        # Print a city's name and information to the file.
        # print(current_date_and_time, width, aspectRatio, diameter, tireVolume, file=volumes_file)
        print(
            f"Date: {current_date_and_time:%Y-%m-%d}, Width: {width}, Ratio: {aspectRatio}, Diameter: {diameter}, Tire Volume: {tireVolume:.2f}, Phone: {tele_num}",
            file=volumes_file,
        )


# Base Funtion to compute the volume of a tire
def get_volume(width, ratio, diameter):
    volume = (
        math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / (10000000000)
    )

    return volume


# Start this program by
# calling the main function.
main()
