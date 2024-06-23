"""
In chemistry, a mole is a very large, fixed quantity, specifically 602,214,076,000,000,000,000,000
 (usually written as 6.02214076 × 1023). The molar mass of a substance is the mass in grams of one mole of
 the substance (grams / mole). A molar mass calculator is a program that computes the molar mass of a substance and
 the number of moles of a sample of that substance. To use a molar mass calculator, a chemist enters two inputs:

* The formula for a molecule, such as H2O (water) or C6H12O6 (glucose)
* The mass in grams of a sample of the substance, such as 3.71
"""


def main():
    # These are the indexes of the
    # elements in the periodic table.
    SYMBOL_INDEX = 0
    NAME_INDEX = 1
    ATOMIC_MASS_INDEX = 2

    # Call the make_periodic_table function and store the returned list in a variable.
    periodic_table = make_periodic_table()

    for table_list in periodic_table:
        atomic_name = table_list[NAME_INDEX]
        atomic_mass = table_list[ATOMIC_MASS_INDEX]

        # Print the name and atomic mass for each chemical element on a separate line. Do not print the chemical element symbols.
        print(f"{atomic_name} {atomic_mass}")


def make_periodic_table():
    periodic_table_list = [
        # [symbol, name, atomic_mass]
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ["Ar", "Argon", 39.948],
        ["As", "Arsenic", 74.921],
        ["At", "Astatine", 210],
        ["Au", "Gold", 196.966569],
        ["B", "Boron", 10.811],
        ["Ba", "Barium", 137.32],
        ["Be", "Beryllium", 9.0],
        ["Bi", "Bismuth", 208.98],
        ["Br", "Bromine", 79.904],
        ["C", "Carbon", 12.010],
        ["Ca", "Calcium", 40.078],
        ["Cd", "Cadmium", 112.41],
        ["Ce", "Cerium", 140.11],
        ["Cl", "Chlorine", 35.453],
        ["Co", "Cobalt", 58.933],
        ["Cr", "Chromium", 51.996],
        ["Cs", "Cesium", 132.90],
        ["Cu", "Copper", 63.546],
        ["Dy", "Dysprosium", 16],
        ["Er", "Erbium", 167.25],
        ["Eu", "Europium", 151.96],
        ["F", "Fluorine", 18.998],
        ["Fe", "Iron", 55.845],
        ["Fr", "Francium", 223],
        ["Ga", "Gallium", 69.723],
        ["Gd", "Gadolinium", 15],
        ["Ge", "Germanium", 72],
        ["H", "Hydrogen", 1.0079],
        ["He", "Helium", 4.0026],
        ["Hf", "Hafnium", 178.49],
        ["Hg", "Mercury", 200.59],
        ["Ho", "Holmium", 164.93],
        ["I", "Iodine", 126.90],
        ["In", "Indium", 114.81],
        ["Ir", "Iridium", 192.21],
        ["K", "Potassium", 39],
        ["Kr", "Krypton", 83.798],
        ["La", "Lanthanum", 13],
        ["Li", "Lithium", 6.941],
        ["Lu", "Lutetium", 174.96],
        ["Mg", "Magnesium", 24],
        ["Mn", "Manganese", 54],
        ["Mo", "Molybdenum", 95],
        ["N", "Nitrogen", 14.006],
        ["Na", "Sodium", 22.989],
        ["Nb", "Niobium", 92.906],
        ["Nd", "Neodymium", 14],
        ["Ne", "Neon", 20.1797],
        ["Ni", "Nickel", 58.693],
        ["Np", "Neptunium", 23],
        ["O", "Oxygen", 15.999],
        ["Os", "Osmium", 190.23],
        ["P", "Phosphorus", 30],
        ["Pa", "Protactinium", 23],
        ["Pb", "Lead", 207.2],
        ["Pd", "Palladium", 10],
        ["Pm", "Promethium", 14],
        ["Po", "Polonium", 209],
        ["Pr", "Praseodymium", 14],
        ["Pt", "Platinum", 195.08],
        ["Pu", "Plutonium", 24],
        ["Ra", "Radium", 226],
        ["Rb", "Rubidium", 85.467],
        ["Re", "Rhenium", 186.20],
        ["Rh", "Rhodium", 102.90],
        ["Rn", "Radon", 222],
        ["Ru", "Ruthenium", 10],
        ["S", "Sulfur", 32.065],
        ["Sb", "Antimony", 121.76],
        ["Sc", "Scandium", 44.955],
        ["Se", "Selenium", 78.96],
        ["Si", "Silicon", 28.085],
        ["Sm", "Samarium", 150.36],
        ["Sn", "Tin", 118.71],
        ["Sr", "Strontium", 87],
        ["Ta", "Tantalum", 180.94],
        ["Tb", "Terbium", 158.92],
        ["Tc", "Technetium", 98],
        ["Te", "Tellurium", 12],
        ["Th", "Thorium", 232.03],
        ["Ti", "Titanium", 47.867],
        ["Tl", "Thallium", 204.38],
        ["Tm", "Thulium", 168.93],
        ["U", "Uranium", 238.02],
        ["V", "Vanadium", 50.941],
        ["W", "Tungsten", 183.84],
        ["Xe", "Xenon", 131.29],
        ["Y", "Yttrium", 88.905],
        ["Yb", "Ytterbium", 17],
        ["Zn", "Zinc", 65.38],
        ["Zr", "Zirconium", 91]
    ]

    return periodic_table_list



if __name__ == "__main__":
    main()