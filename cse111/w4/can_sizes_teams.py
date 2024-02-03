"""In many countries, food is stored in steel cans (also known as tin cans)
 that are shaped like cylinders. There are many different sizes of steel cans.
   The storage efficiency of a can tells us how much a can stores versus how 
   much steel is required to make the can. Some sizes of cans require a lot 
   of steel to store a small amount of food. Other sizes of cans require less
     steel and store more food. A can size with a large storage efficiency 
     is considered more friendly to the environment than a can size with a 
     small storage efficiency.

The storage efficiency of a steel can is computed
 by dividing the volume of a can by its surface area.

                      volume
storage_efficiency =----------------
                      surface_area


In other words, the storage efficiency of a can is the space inside 
the can divided by the amount of steel required to make the can. 
The formulas for the volume and surface area of a cylinder are:

volume = π radius**2 * height

surface_area = 2π*radius*(radius + height)

-π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
-radius is the radius of the cylinder
-height is the height of the cylinder
"""

import math

def main():

     # Create a list for the cans names
     can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
     can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
     can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
     can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]
     
     best_store = None
     best_cost = None
     max_store_eff = -1
     max_cost_eff = -1

     # For each can in the parallel lists, unpack the values
     # into the variables name, radius, height, and cost.
     for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]

        # Call the compute_storage_efficiency and
        # compute_cost_efficiency functions.
        store_eff = compute_storage_efficiency(radius, height)
        cost_eff  = compute_cost_efficiency(radius, height, cost)

        # Print the can size name, storage
        # efficiency, and cost efficiency.
        print(f"{name} {store_eff:.2f} {cost_eff:.0f}")

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

     # Print the best storage and cost efficiencies.
     print()
     print("Best can size in storage efficiency:", best_store)
     print("Best can size in cost efficiency:", best_cost)


def compute_storage_efficiency(radius, height):
     """
     This function should call the compute_volume and
     compute_surface_area functions and then compute
     and return the storage efficiency of a steel can size.
     """
     
     volume = compute_volume(radius, height)

     # call the surface area function to compute the storage efficiency
     surface_area = compute_surface_area(radius, height)

     # compute the storage efficiency
     storage_efficiency = volume / surface_area

     return storage_efficiency


def compute_volume(radius, height):
     # calculate the volume of the cylinder
     volume = math.pi * radius**2 * height

     return volume
     

def compute_surface_area(radius, height):
     # compute the surface area of the cylinder
     surface_area = 2 * math.pi * radius * (radius + height)

     return surface_area


def compute_cost_efficiency(radius, height, cost_per_can):
     """
     compute_cost_efficiency that computes and returns
     the volume of a steel can divided by its cost.
     """
     volume = compute_volume(radius, height)
     cost = volume / cost_per_can

     return cost


main()