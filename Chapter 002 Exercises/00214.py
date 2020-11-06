# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 2 Exercise 14. Compound Interest
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

# Some user input terminates program due to numbers that are too large.
# The function below tries to stop that.


def compoundInterestFormula(principal, interestRate, compoundedInterest, yearsLeft):
    try:
        amount = principal * (1 + interestRate / compoundedInterest) ** (compoundedInterest * yearsLeft)
    except Exception:
        logging.exception('Caught an error')
        # Pauses program so exception prints and user can clearly see the next step.
        time.sleep(1)
        print('The numbers used were too big for this program.')
        userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        main()
        # Exits program since above command recursively calls program.
        sys.exit("Quitting Program")
    else:
        return amount


def main():
    print('\n\n')
    print("Welcome to Misers Money Credit Union Compound Interest Calculator!")
    print()
    # User input below, all handled by try except to prevent common program crashes.
    principal = inputHandling("Enter how much was originally deposited into the account:  $")
    interestRate = inputHandling("In whole numbers, please enter the interest rate paid by the account:   ")
    # Converts percent to decimal
    interestRate /= 100
    compoundedInterest = inputHandling("Enter the number of times a year the interest is compounded:  ")
    yearsLeft = inputHandling("Enter the number of years the account has left to earn interest:  ")
    # Function below handles user input that results in program crashes due to too big of a number.
    amount = compoundInterestFormula(principal, interestRate, compoundedInterest, yearsLeft)
    # Returns interestRate to a "decimal"
    printedInterest = interestRate * 100
    #
    # Output
    #
    # Handles singular and plural English responses depending on compoundedInterest value.
    plural = ' per Year' if compoundedInterest == 1 else 's Yearly'
    print()
    print("Please see below for the status of this account.")
    print("------------------------------------------------")
    # This array stores phrases that are formatted using f strings.
    terms = ['Principal:', 'Interest Rate:', 'Compound Interest:', 'Years Left:', 'Amount to Earn:']
    # For value of 'terms' used below, see the array above.
    print(f"{terms[0]:>20}   ${principal:<20,.2f}")
    # if statement discriminates based on length of item for better formatting.
    if len(str(printedInterest)) == 4:
        print(f"{terms[1]:>20}   {printedInterest:<3,.2f}%")
    else:
        print(f"{terms[1]:>20}   {printedInterest:<4,.2f}%")
    # if statement changes response for English grammar based on value.
    if len(str(int(compoundedInterest))) == 1:
        print(f"{terms[2]:>20}   {int(compoundedInterest):<1,d} Time{plural}")
    else:
        print(f"{terms[2]:>20}   {int(compoundedInterest):<2,d} Times Yearly")
    print(f"{terms[3]:>20}   {int(yearsLeft):<10,d}")
    print(f"{terms[4]:>20}   ${amount:<20,.2f}")
    print('\n')
    input("Press enter to exit...")
    print('\n')

# Program start with below function call


main()
