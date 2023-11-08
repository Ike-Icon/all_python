"""Write a program to convert from Fahrenheit to Celsius. 
Display the result to one decimal place of precision.
To convert degrees in Fahrenheit to Celsius you need 
to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9."""

# Ask for for the temperature in Fahrenheit
fahrenheit = int(input("What is the temperature in Fahrenheit? "))

# comput temperature in Fahrenheit to Celsius
temp_C = fahrenheit - 32 
celsius = temp_C * 5/9

print(f"The temperature in Celsius is {celsius:.1f} degrees.")