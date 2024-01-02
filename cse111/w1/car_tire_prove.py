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


# Base Funtion to compute the volume of a tire
def get_volume(width, ratio, diameter):
    volume = math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / (10000000000)

    return volume


# Ask the user for the width of the tire in mm
width = int(input("Enter the width of the tire in mm (ex 205): "))

# Ask the user for the aspect ratio of the tire
aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Ask the user for the diameter of the tire in inches
diameter = int(input("Enter the diameter of the tire in inches (ex 15): "))

tireVolume = get_volume(width=width, ratio=aspectRatio, diameter=diameter)

# Print the approximate volume of the tire in liters
print(f"\nThe approximate volume is {tireVolume:.2f} liters")
