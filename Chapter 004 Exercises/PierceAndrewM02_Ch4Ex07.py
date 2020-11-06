# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 4 Exercise 7. Pennies for Pay
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
    print()
    print('You will begin being paid at one penny a day.')
    print('The amount will double everyday after the first day.')
    daysEmployed = inputHandling('How many days do you plan on being employed under these terms:  ')
    dailyIncrement = 1
    amountEarned = .01
    startingSalary = .01
    while dailyIncrement < daysEmployed + 1:
        print(f'Employment Day: {dailyIncrement}  Amount Earned: ${amountEarned:,.2f}  Current Salary: ${startingSalary:,.2f}')
        dailyIncrement += 1
        startingSalary *= 2
        amountEarned += startingSalary


main()
