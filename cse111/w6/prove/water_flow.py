"""Write a Python program that could help an engineer design 
a water distribution system. During this prove milestone, 
you will write three program functions and three test functions 
as described in the Steps section below."""

# unction that calculates and returns the height of a column
# of water from a tower height and a tank wall height.
def water_column_height(tower_height, tank_height):
    """In your function, use the following formula for calculating the water column height.
                         3w
                h = t + ----
                         4
    where
        h is height of the water column
        t is the height of the tower
        w is the height of the walls of the tank that is on top of the tower"""
    water_column_height = tower_height + (3 * tank_height / 4)

    return water_column_height


# write a function  that calculates and returns the pressure
# caused by Earth’s gravity pulling on the water stored in an elevated tank.
def pressure_gain_from_water_height(height):
    """In your function, use the following formula for calculating pressure caused by Earth's gravity.
                    ρgh
               P = ------
                    1000
    where
        P is the pressure in kilopascals
        ρ is the density of water (998.2 kilogram / meter3)
        g is the acceleration from Earths gravity (9.80665 meter / second2)
        h is the height of the water column in meters"""

    pressure = (998.2 * 9.80665 * height) / 1000
    
    return pressure


# write a function named pressure_loss_from_pipe that calculates and returns
# the water pressure lost because of the friction between the water and the walls of a pipe that it flows through
def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """In your function, use the following formula for calculating pressure loss from friction within a pipe.

                    -fLρv**2
               P = --------
                    2000d
    where
        P is the lost pressure in kilopascals
        f is the pipe's friction factor
        L is the length of the pipe in meters
        ρ is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the pipe in meters / second
        d is the diameter of the pipe in meters"""

    pressure_loss = - friction_factor * pipe_length * 998.2 * fluid_velocity**2 / (2000 * pipe_diameter)

    return pressure_loss


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """In your function, use the following formula for calculating pressure loss from pipe fittings.

                -0.04 ρ v**2n
            P =  -------------
                    2000
    where
        P is the lost pressure in kilopascals
        ρ is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the pipe in meters / second
        n is the quantity of fittings
    """
    pressure_loss = -0.04 * 998.2 * fluid_velocity**2 * quantity_fittings / (2000)

    return pressure_loss


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """In your function, use the following formula for calculating the Reynolds number.
         ρdv
     R =--------
          μ
    where
        R is the Reynolds number
        ρ is the density of water (998.2 kilogram / meter3)
        d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe's inner diameter.
        v is the velocity of the water flowing through the pipe in meters / second
        μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
        """
    reynolds_num = 998.2 * hydraulic_diameter * fluid_velocity / (0.0010016)

    return reynolds_num
