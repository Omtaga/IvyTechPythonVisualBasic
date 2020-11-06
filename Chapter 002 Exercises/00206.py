# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 2 Exercise 6. Sales Tax
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.9.0

# logging for exceptions / sys for quit / time for sleep
import logging
import sys
import time

# Handles all user input, expects numeric entry and responses > 0


def inputHandling(question):
    while True:
        try:
            userInput = input(question)
            isinstance(float(userInput), str)
        except Exception:
            logging.exception('Caught an error')
            # Pauses program so that exception prints to screen
            # and user sees next step to continue after error message.
            time.sleep(1)
            print("Your number needs to be entered with numeric keys.")
            userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
            if userQuit == 'q':
                sys.exit("Quitting Program")
        else:
            # Makes sure input is greater than zero to avoid / by zero error or zero responses
            if float(userInput) <= 0:
                print("Your input must be greater than zero.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")
            else:
                return float(userInput)


def main():
    COUNTY_TAX = .025
    STATE_TAX = .05
    print()
    print("This program calculates the total price of\nthe sale to find the total state and\ncounty sales tax.")
    print()
    userInput = inputHandling("Enter the total price of the purchase: $")
    print()
    countyTax = userInput * COUNTY_TAX
    stateTax = userInput * STATE_TAX
    print(f'Subtotal: ${userInput:,.2f}')
    countyTaxOutput = f'County Tax ({COUNTY_TAX:.1%}): ${countyTax:,.2f}'
    print(countyTaxOutput)
    print(f'State Tax ({STATE_TAX:.1%}): ${stateTax:,.2f}')
    # Prints line dividing Total from rest of receipt to equal the longest line
    print('-' * len(str(countyTaxOutput)))
    print(f'Total: ${userInput + countyTax + stateTax:,.2f}')
    print("\n")
    input("Press enter to continue...")


main()
