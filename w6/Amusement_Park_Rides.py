"""Your program should prompt for the riders' ages and heights, 
and then display a message indicating whether they can ride or not."""
ride = True

first_age = int(input("What is the age of the first rider? "))
first_height = int(input("What is the height of the first rider? "))
sec_rider = input("Is there a second rider (yes/no)? ")

approval = "Welcome to the ride. Please be safe and have fun!"
denined = "Sorry, you may not ride."

# if there is a second rider, ask of their details
if sec_rider.lower() == "yes":
    second_age = int(input("What is the age of the second rider? "))
    second_height = int(input("What is the height of the second rider? "))

    # Finish implementing the basic rules.
    if first_height < 36 or second_height < 36:
        ride = False
    elif first_age >= 18 or second_age >= 18:
        ride = True


elif first_age >= 18:
    if first_height >= 62:
        ride = True

else:
    ride = False

# STRETCH CHALLENGE 1
if first_age < 18 and second_age < 18:
    if first_age >= 12 and second_age >= 12:
        if first_height >= 52 and second_height >= 52:
            ride = True

# STRETCH CHALLENGE 2

if ride:
    print(approval)
else:
    print(denined)

