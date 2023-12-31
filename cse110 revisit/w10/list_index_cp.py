'''Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."'''

shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish): ")

items = ""

while items != "quit":
    items = input("Item: ")
    if items != "quit":
        shopping_list.append(items)


print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

# access the item using the index and the square brackets. Print the index in front of the items
print("\nThe shopping list with indexes is:")
for index in range(len(shopping_list)):
    item = shopping_list[index]
    print(f"{index}. {item}")

# Ask the user for an index and a new shopping list item. Replace the item at that index with the new item.
add_item = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")

# remove_item = shopping_list.pop(add_itme)
# print(remove_item)
# shopping_list.append(new_item)
# print(shopping_list)
shopping_list[add_item] = new_item

# # Display thenew list with the new item in the list
print("\nThe new shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")
