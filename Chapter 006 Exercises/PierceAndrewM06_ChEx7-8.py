# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 6 Exercise 6 & 9. Average of Numbers and Exception Handling
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import logging
import time
import random


def inputHandling(question):
    while True:
        try:
            userInput = input(question)
            isinstance(float(userInput), str)
        except ValueError:
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
            if float(userInput) <= 0 or float(userInput) % 1 != 0:
                print("Your input must be greater than zero and a whole number.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")
            else:
                return float(userInput)


def writeRandom(openFile, userNumber):
    increment = 0
    while increment < userNumber:
        randomNumber = str(random.randint(1, 500))
        openFile.write(randomNumber + '\n')
        increment += 1


def randomReader(openFile):
    while True:
        try:
            numbersInFile = []
            for line in openFile:
                lineAmount = line.rstrip('\n')
                numbersInFile.append(lineAmount)
        except ValueError:
            logging.exception('Caught an error')
            time.sleep(1)
        else:
            return numbersInFile


def listToText(arg):
    increment = 0
    length = len(arg)
    lineLength = 130
    result = ""
    while increment < length:
        if increment == 0:
            result += arg[increment]
            increment += 1
        else:
            if len(result) > lineLength:
                result += f",\n{arg[increment]}"
                lineLength += 130
            else:
                result += f', {arg[increment]}'
            increment += 1
    return result


def main():
    print('This program will write random numbers from 1 - 500.')
    userNumber = inputHandling('Enter how many random numbers would you like to generate: ')
    openFile = open('andrewRandom.txt', 'w')
    writeRandom(openFile, userNumber)
    openFile.close()
    openFile = open('andrewRandom.txt', 'r')
    result = randomReader(openFile)
    print('The numbers created were:')
    print(f'{listToText(result)}')
    for i in range(0, len(result)):
        result[i] = int(result[i])
    Sum = sum(result)
    print(f'The total of those numbers is: {Sum}')
    print(f'The number of random numbers read from the file was {len(result)}.')
    openFile.close()


if __name__ == '__main__':
    main()
