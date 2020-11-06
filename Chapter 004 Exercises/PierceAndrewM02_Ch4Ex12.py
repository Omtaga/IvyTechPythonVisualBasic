# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 4 Exercise 12. Calculating the Factorial of a Number
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
    print("Finding " + "\N{Mathematical Italic Small N}" + "!")
    userInput = inputHandling("Let's find the factorial of a number, enter a positive integer: ")
    increment = 1
    result = 1
    while increment < userInput + 1:
        result *= increment
        increment += 1
    print(f'{userInput}! = {result:,d}')


main()
