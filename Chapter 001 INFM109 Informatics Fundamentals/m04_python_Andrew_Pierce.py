# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 3 Exercise 16. February Days
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.9.0

# Time for sleep so user gets next response if error message in console.
# Sys for exit should user opt to exit program.
# Logging for handling errors.
# Datetime used for grammar.
import time
import sys
import logging
import datetime


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
            if float(userInput) % 1 != 0:
                print("Your input must be a whole number.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")

            else:
                return int(userInput)


def main():
    userYear = inputHandling('\nEnter a year to determine if it is a leap year:  ')

    # Initialize variables early for some results.
    bc = ''
    nullYear = None
    noLeap = None
    numberOf = 0

    # This section handles the special cases that arose during the implementation of leap year.
    if userYear == 0:
        # Creates output for user input of zero.
        nullYear = "There was no year 0!"
    elif userYear < -45:
        # Creates output for user input less than -45.
        noLeap = f'In {userYear * -1} BC it was not a leap year.  Leap year was not introduced until 45 BC'
    elif userYear == 8 or userYear == 12:
        numberOf = 29
    elif userYear <= -9 and userYear % 3 == 0:
        numberOf = 29
        bc = ' BC'
        userYear *= -1
    elif userYear < 0:
        numberOf = 28
        bc = ' BC'
        userYear *= -1
    elif userYear < 8:
        numberOf = 28

    # This section handles the most recent years and those going forward until adjustments are needed.
    if userYear >= 16:
        if userYear % 400 == 0:
            numberOf = 29
        elif userYear % 4 == 0 and userYear % 100 == 0:
            numberOf = 28
        elif userYear % 4 == 0:
            numberOf = 29
        else:
            numberOf = 28

    # Handles Have, Has, and had in last output.
    now = datetime.datetime.now()
    if userYear > now.year:
        haveHadHas = 'will have'
    elif userYear < now.year:
        haveHadHas = 'had'
    else:
        haveHadHas = 'has'

    # Handles the word 'be' in the final output.
    if userYear > now.year:
        be = ' be '
    elif userYear < now.year:
        be = ' '
    else:
        be = ' '

    # Handles will, was, and is in the final output.
    if userYear > now.year:
        wasIsWill = 'will'
    elif userYear < now.year:
        wasIsWill = 'was'
    else:
        wasIsWill = 'is'

    # Output begins here.
    if nullYear is not None:
        # Pulls response from user input of zero.
        output = nullYear
        print(output)
    elif noLeap is not None:
        # Pull response from user input of less than -45 (45BC)
        output = noLeap
        print(output)
    else:
        output = f'In {userYear}{bc}, February {haveHadHas} {numberOf} days.'
        print(output)
        if numberOf == 28:
            print(f'{userYear} {wasIsWill} not{be}a leap year.')
        else:
            print(f'{userYear} {wasIsWill}{be}a leap year.')
    input('\nPress enter to exit...')


if __name__ == "__main__":
    main()
