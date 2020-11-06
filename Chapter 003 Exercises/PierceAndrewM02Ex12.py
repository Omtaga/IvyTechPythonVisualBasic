# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 3 Exercise 12. Software Sales
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.9.0

import time
import sys
import logging


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
            elif float(userInput) % 1 != 0:
                print("Your input must be a whole number.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")
            else:
                return int(userInput)


def main():
    PACKAGE_PRICE = 99
    print()
    print('Welcome to Quality Software Sales, where we bring the discount to you!')
    print()
    print('Our corporate members enjoy discounts based on the volume purchased.')
    print("Check our pricing tiers below to find the one that fits your company's needs.")
    print()
    print(f'Current selection cost: ${PACKAGE_PRICE}')
    print('Quantity    Discount')
    print('--------------------')
    print('10-19       10%')
    print('20-49       20%')
    print('50-99       30%')
    print('100+        40%')
    print()
    userInput = inputHandling("Let's get your discount!  Enter the number of software packages you need:  ")
    # Package amounts and discounts lined up.  For Example, less than 10 - zero discount, between 10 and 19 - 10 percent
    packageCutoff = [10, 20, 50, 100]
    discountBreak = [00, 10, 20,  30, 40]
    discount = None
    for num, amount in enumerate(packageCutoff):
        if userInput < amount:
            discount = discountBreak[num]
            break
        elif userInput >= 100:
            discount = discountBreak[4]
            break
    print()
    print(f'Units purchased: {userInput}')
    subtotal = userInput * PACKAGE_PRICE
    print(f'Subtotal: ${subtotal}')
    print(f'Member Discount: {discount}%')
    amountSaved = subtotal * (discount / 100)
    print(f'Member Savings: ${amountSaved}')
    print('-------------')
    print(f'Total: ${subtotal - amountSaved}')


main()
