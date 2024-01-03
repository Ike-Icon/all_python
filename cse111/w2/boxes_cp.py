"""
A manufacturing company needs a program that will help its employees pack 
manufactured items into boxes for shipping. Write a Python program named boxes.py 
that asks the user for two integers:

1. the number of manufactured items
2. the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to
hold the items. This must be a whole number. Note that the last box may
be packed with fewer items than the other boxes.
"""
import math


# function to comput how many boxes to hold the items
def get_items(manu_items, items_box):
    items_per_box = manu_items / items_box

    return items_per_box


# Ask for the the number of manufactured items
manufactured_items = int(input("Enter the number of items: "))

# Ask for the the number of items that the user will pack per box
pack_per_box = int(input("Enter the number of items per box: "))

items = math.ceil(get_items(manufactured_items, pack_per_box))

print(
    f"\nFor {manufactured_items} items, packing {pack_per_box} items in each box, you will need {items} boxes."
)
