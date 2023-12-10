"""Working with lists
Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0."""

num_list = []

numbers = None

print("Enter a list of numbers, type 0 when finished.")
while numbers != 0:
    numbers = int(input("Enter number: "))

    if numbers != 0:
        num_list.append(numbers)


sum = 0
for num in num_list:
    # Compute the sum, or total, of the numbers in the list.
    sum += num

    # Compute the average of the numbers in the list.
    averageNum = sum / len(num_list)

    # Find the maximum, or largest, number in the list.
    maxNum = max(num_list)

    # Find the minimum number in the list
    minNum = min(num_list)


print(f"\nThe sum is: {sum}")

print(f"\nthe average is: {averageNum:.2f}")

print(f"\nthe maximum is: {maxNum}")

print(f"\nthe minimum is: {minNum}")


# II STRETCH CHALLENGE
# find the smallest positive number (the positive number that is closest to zero).
pos_num = 99999999999

for num in num_list:
    if num < pos_num and num > 0:
        pos_num = num
print(f"\nsmallest positive numberis: {pos_num}")

# Sort the numbers in the list and display the new, sorted list.
sorted_numbers = sorted(num_list)
print("The sorted list is: ")
for sorted_num in sorted_numbers:
    print(sorted_num)


# Sort the numbers reversely in the list and display the new, reversed sorted list.
reversed_sorted_list = sorted(num_list, reverse=True)
print("\nThe reversed sorted list is: ")
for rev_sorted in reversed_sorted_list:
    print(rev_sorted)
# print(num_list)
