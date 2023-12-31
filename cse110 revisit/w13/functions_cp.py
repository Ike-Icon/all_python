"""In your program below the functions, ask the user to type a message. 
Then, pass that message to each of the three functions, so it it displays it each way"""

# Write three functions:
# display_regular—Receives a string and prints it out, exactly as received.
def display_regular(message):
    print(message)


# display_uppercase—Receives a string, converts it to upper case, and then prints it out.
def display_uppercase(message):
    upperMessage = message.upper()
    print(upperMessage)


# display_lowercase—Receives a string, converts it to lower case, and then prints it out.
def display_lowercase(message):
    lowerMessage = message.lower()
    print(lowerMessage)


userMessage = input("What is your message? ")

# Call the functions now
display_regular(userMessage)
display_uppercase(userMessage)
display_lowercase(userMessage)