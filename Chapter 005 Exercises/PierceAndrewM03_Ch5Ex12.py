# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 5 Exercise 12. Maximum of Two Values
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

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


def isEqual(valueOne, valueTwo):
    if valueOne != valueTwo:
        return False
    else:
        return True


def maximumOfTwoValues(valueOne, valueTwo):
    # This function always returns a number, if both numbers are equal it will return the first number.
    if valueOne > valueTwo:
        return valueOne
    elif valueTwo > valueOne:
        return valueTwo
    else:
        return valueOne


def main():
    print()
    print('This program will check which number entered has the largest value.')
    valueOne = inputHandling("Enter the first whole number.")
    valueTwo = inputHandling("Enter the second whole number.")
    equalNumber = isEqual(valueOne, valueTwo)
    if equalNumber is False:
        largestNumber = maximumOfTwoValues(valueOne, valueTwo)
        print()
        print(f'The largest number inputted was {largestNumber}')
    else:
        print()
        print(f'Both values are equal. The maximum is the same: {valueOne}')
    print()
    input('Press enter to exit...')


main()
