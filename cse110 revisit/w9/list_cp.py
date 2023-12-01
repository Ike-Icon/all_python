"""Ask the user for the names of their friends and append them to a list.
Then, display each of the friends in the list. You should stop asking for
friends when the user types "end"."""


friends = []

add_more = "yes"

count_friends = 0
friend_name = input("Enter your friend name: ")

while friend_name != "end":
    count_friends += 1
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)

print("\nYour friends are: ")
for friend in friends:
    print(friend)


print(f"\nYou have {count_friends} friends")
