# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 5 Exercise 17-18. Prime Numbers and Prime Number List
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
            # Makes sure input is greater than one.
            if float(userInput) <= 1:
                print("Your input must be greater than one, there are no prime numbers less than or equal to one.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")
            else:
                return float(userInput)


def is_prime(arg):
    halfPlusOne = (arg / 2) + 1
    increment = 2
    if arg == 2:
        return True
    else:
        while increment < halfPlusOne:
            if arg % increment == 0:
                return False
            elif increment == halfPlusOne:
                return True
            else:
                increment += 1


def first100primes():
    firstPrimes = []
    increment = 2



def main():
    pass


main()
