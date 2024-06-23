""" write a Python program named random_numbers.py that creates a list of numbers, 
appends more numbers onto the list, and prints the list. The program must have two 
functions named main and append_random_numbers as follows:
"""
import random

def main():
    # Creates a list named numbers like this:
    numbers = [16.2, 75.1, 52.3]
    # Prints the numbers list
    print(f"numbers {numbers}")


    # Calls the append_random_numbers function with only one argument to add one number to numbers
    appended_random_numbers(numbers, 3)
    print(f"numbers {numbers}")
    # Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    appended_random_numbers





def appended_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


if __name__ == '__main__':
    main()
