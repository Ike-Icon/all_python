"""Write functions to compute and return the areas of squares, rectangles, and circles.
These functions should not display the values directly, but rather should return them, 
so they could be used in other parts of the program.
"""
# import numpy as np

shapes = [
    "1. Square",
    "2. rectangle",
    "3. Circle",
    "4. Quit",
]


# Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.
def compute_area_square(square_len):
    area = square_len**2
    return area


# Write a function compute_area_rectangle that accepts a single value as a parameter, and then computes the area and returns it.
def compute_area_rectangle(rec_len, rec_width):
    area_rec = rec_len * rec_width
    return area_rec


# Write a function compute_area_circle that accepts a single value as a parameter, and then computes the area and returns it.
def compute_area_circle(pi_value, circle_radius):
    area_circle = pi_value * circle_radius**2
    return area_circle


userShapes = ""

while userShapes != 4:
    print("\nPlease select one of the following shapes: ")

    for shape in shapes:
        print(shape)

    userShapes = int(input("\nWhat kind of shape do you have? "))

    if userShapes == 1:
        # write code to prompt the user for the side of a square
        squareLen = float(
            input("What is the length of a side of the square in centimeters? ")
        )
        # save it into a variable
        square_area = compute_area_square(squareLen)
        # print out the square area
        print(f"The area of the square is: {square_area}")

    elif userShapes == 2:
        # comput the area of the rectangle
        rec_len = float(input("\nWhat is the length of rectangle in centimeters? "))
        rec_width = float(input("What is the width of the rectangle in centimeters?"))
        recArea = compute_area_rectangle(rec_len, rec_width)
        print(f"The area of the rectangle is: {recArea}")

    elif userShapes == 3:
        circle_radius = float(
            input("\nWhat is the radius of the circle in centimeters? ")
        )
        # pi_value = np.pi
        pi_value = 0.3
        areaCircle = compute_area_circle(pi_value, circle_radius)
        print(f"The area of the circle is: {areaCircle}")

    else:
        print("thank you, Goodbye")
