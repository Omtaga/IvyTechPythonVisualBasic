# Tip, Tax, and Total

import os


def cls():
    # Clears the terminal screen for all systems except for IDE environments e.g. Pycharm
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    GRATUITY_CHARGE = .18
    SALES_TAX = .07
    print()
    print("This program will calculate the Tip, tax and total of a restaurant order.")
    print("This program will charge tax on the gratuity as it is a fixed amount and\nnot subject to change.")
    print()
    mealTotal = float(input("Please enter the total amount of the food in this order: $"))
    print()
    print(f"Subtotal: ${mealTotal}")
    gratuity = mealTotal * GRATUITY_CHARGE
    tipLine = f"Tip ({GRATUITY_CHARGE:.1%}): ${gratuity:,.2f}"
    print(tipLine)
    taxCollected = (mealTotal + gratuity) * SALES_TAX
    print(f"Tax ({SALES_TAX:.1%}): {taxCollected:,.2f}")
    print('-' * len(str(tipLine)))
    print(f"Total: ${mealTotal + gratuity + taxCollected:,.2f}")
    print("\n\n\n\n")
    input("Press enter to continue...")
    print("\n\n\n\n")


# Gets screen size of OSX users.
screenSize = os.get_terminal_size()
SCREEN_LENGTH = 80
SCREEN_HEIGHT = 30

# Sets screen size on OSX if not full screen.
os.system(f"resize -s {SCREEN_HEIGHT} {SCREEN_LENGTH}")

cls()

main()

# Returns screen size on OSX systems to previous user settings if not full screen.
os.system(f"resize -s {screenSize[1]} {screenSize[0]}")

cls()




