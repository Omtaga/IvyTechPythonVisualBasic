# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 5 Exercise 17-18. Prime Numbers and Prime Number List
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

# logging for exceptions / sys for quit / time for sleep
import logging
import sys
import time
import math


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
    # halfPlusOne removes the need to divide the candidate by numbers greater than half it's value.
    halfPlusOne = math.ceil(arg / 2)
    increment = 2
    if arg == 2:
        return True
    else:
        while increment <= halfPlusOne:
            if arg % increment == 0:
                return False
            elif increment == halfPlusOne:
                return True
            else:
                increment += 1


def first100primes():
    firstPrimes = []
    increment = 2
    while increment < 100:
        thisNumber = is_prime(increment)
        if thisNumber:
            firstPrimes.append(increment)
        increment += 1
    return firstPrimes


def toAlpha(number):
    toString = str(number)
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if len(toString) > 3:
        return int(number)
    elif len(toString) < 2:
        return ones[int(toString[0]) - 1]
    elif len(toString) == 2:
        if int(toString) % 10 == 0:
            return tens[int(toString[0]) - 1]
        else:
            if toString[0] == '1':
                return teens[int(toString[1]) - 1]
            else:
                return tens[int(toString[0]) - 1] + '-' + ones[int(toString[1]) - 1]
    else:
        if int(toString) % 100 == 0:
            return ones[int(toString[0]) - 1] + ' hundred'
        elif int(toString[2]) == 0:
            return ones[int(toString[0]) - 1] + ' hundred ' + tens[int(toString[1]) - 1]
        elif int(toString[1]) == 0:
            return ones[int(toString[0]) - 1] + ' hundred ' + ones[int(toString[1]) - 1]
        elif int(toString[1]) == 1:
            return ones[int(toString[0]) - 1] + ' hundred ' + teens[int(toString[2]) - 1]
        else:
            return ones[int(toString[0])-1]+' hundred '+tens[int(toString[1])-1]+'-'+ones[int(toString[2])-1]


def listToText(arg):
    increment = 0
    length = len(arg)
    lineLength = 150
    result = ""
    while increment < length:
        if increment == 0:
            result += toAlpha(arg[increment])
            increment += 1
        else:
            if len(result) > lineLength:
                result += f",\n{toAlpha(arg[increment])}"
                lineLength += 150
            else:
                result += f', {toAlpha(arg[increment])}'
            increment += 1
    return result


def main():
    print()
    userInput = int(inputHandling("Please enter a number to assess if it is prime:  "))
    print()
    userInputResult = is_prime(userInput)
    print(f'The number {toAlpha(userInput)} is {"" if userInputResult else "not "}prime.')
    print()
    print('The first one-hundred primes are:')
    oneHundredPrimesList = first100primes()
    print(f'{listToText(oneHundredPrimesList)}')
    print()
    input('Press enter to continue...')


main()
