# Prompt the user for their age
age = int(input("How old are you? "))

# add one to the age, and tell them how old they will be on their next birthday
next_age = age + 1

print(f"On your next birthday, you will be {next_age}")

# Prompt the user for the number of egg cartons they have
cartons_of_eggs = int(input("\nHow many egg cartons do you have? "))

# Assume each carton holds 12 eggs, multiply their number by 12
total_eggs = cartons_of_eggs * 12

print(f"You have {total_eggs} eggs")

# Prompt the user for a number of cookies and a number of people.
num_of_cookies = float(input("\nHow many cookies do you have? "))
num_of_people = float(input("How many people are there? "))

# divide the number of cookies by the number of people
ppl_per_cookie = num_of_cookies/num_of_people

print(f"\nEach person may have {ppl_per_cookie} cookies")