"""Many vehicle owners record the fuel efficiency of their vehicles as a way to 
track the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, 
there is probably something wrong with the engine or drive train of the vehicle. 
In the United States, fuel efficiency for gasoline powered vehicles is calculated 
as miles per gallon. In most other countries, fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

       end − start
 mpg = ------------
       gallons

where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.
The formula for converting miles per gallon to liters per 100 kilometers is the following:

         235.215
lp100k = ---------
         mpg
"""


# Define the main function.
def main():
    # Ask for the starting odometer value in miles
    start_odometer = float(input("Enter the starting odometer value in miles: "))

    # Ask for the ending odometer value in miles
    end_odometer = float(input("Enter the ending odometer value in miles: "))

    # Ask for the amount of fuel in gallons
    fuel_amount = float(input("Enter the amount of fuel in gallons: "))

    # Call the get_miles_per_gallon function
    mpg = get_miles_per_gallon(
        start_odometer, end_odometer, fuel_amount
    )
    print(f"{mpg:.2f} miles per gallon")

    # Call the get_lp100k_from_mpg to converting from miles per gallon to liters per 100 kilometers
    litersPer100K = get_lp100k_from_mpg(mpg)

    print(f"{litersPer100K:.2f} liters per 100 kilometers")


# Define the functon for computing the miles per gallon
def get_miles_per_gallon(start, end, gallons):
    miles_per_gallon = (end - start) / gallons

    return miles_per_gallon


# Define the funtion for converting from miles per gallon to liters per 100 kilometers
def get_lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg

    return lp100k

# Call the main function to start the program 
main()