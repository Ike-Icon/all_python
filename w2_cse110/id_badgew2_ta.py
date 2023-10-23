# An ID badge
# ask for the user's first name
firstName = input("First Name: ")

# ask for the user's last name
lastName = input("Last Name: ")

# ask for the user's job title
jobTitle = input("Job Title: ")

# ask for the user's email address
email = input("Email Address: ")

# ask for the user's phone number
phone = input("Phone Number:")

# ask for the user's id number
id_number = input("ID Number:")

# ask for the user's hair color
hair_color = input("Hair Color:")

# ask for the user's eye color
eye_color = input("Eye Color:")

# ask for the user's month of starting
start_month = input("Start Month: ")

# ask for the user's completed advanced training
advanced_training = input("Advanced Training, Yes or No:")


# The ID Card
print("The ID Card is:")
print("-------------------------------------------")
print(f"{firstName.capitalize()}, {lastName.capitalize()}")
print(jobTitle.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair Color: {hair_color:5} Eye Color: {eye_color}")
print(f"Month: {start_month:10} Training: {advanced_training}")
print("--------------------------------------------")