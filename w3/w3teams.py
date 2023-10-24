import numpy as np
"""Write a program to compute the areas of three different shapes.
Prompt for the necessary information,
then compute and display the area"""

"""Square—The area is the length of a side squared.
Rectangle—The area is the length multiplied by the width.
Circle—The area is Pi (you can use 3.14) multiplied by the radius squared."""

square_len = float(input("What is the length of a side of the square in centimeters? "))

# comput the area of the square 
square_area = square_len ** 2

print(f"The area of the square is: {square_area}")

# comput the area of the rectangle
rec_len = float(input("\nWhat is the length of rectangle in centimeters? "))
rec_width = float(input("What is the width of the rectangle in centimeters?"))

area_rec = rec_len * rec_width

print(f"The area of the rectangle is: {area_rec}")

# comput the radius of the circle
circle_radius = float(input("\nWhat is the radius of the circle in centimeters? "))
pi_value = np.pi

area_circle = pi_value * circle_radius ** 2

print(f"The area of the circle is: {area_circle}")

# comput the area of the square and the circle with single length value
single_value = float(input("What is the value of the length of all the shapes? "))

# comput the area of the square 
square = single_value ** 2

# comput the radius of the circle
circle = pi_value * single_value ** 2

print(f"\nThe area of the square is: {square}")
print(f"The area of the circle is: {circle}")
