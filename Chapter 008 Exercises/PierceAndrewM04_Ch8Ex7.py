# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 8 Exercise 7. Character Analysis
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import time
import logging
import os

FILE_LOCATION = 'text.txt'


def fileInputHandling(question, array):
    while True:
        try:
            userInput = input(question)
            isinstance(float(userInput), str)
            userInput = int(userInput) - 1
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
            if float(userInput) < 0 or float(userInput) % 1 != 0 or float(userInput) >= len(array):
                print("Your input was invalid, check the number or please choose a file using the numerical keys.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")
            else:
                return int(userInput)


def chooseFile():
    directory = os.listdir()
    increment = 1
    for files in directory:
        print(f'{increment}. {files}')
        increment += 1
    fileChoice = fileInputHandling("Enter desired file: ", directory)
    if fileChoice < 0 or fileChoice >= len(directory) or fileChoice % 1 != 0:
        print('Invalid input, please try again.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        chooseFile()
    return directory[fileChoice]


def checkFile(programInput):
    try:
        usableFile = open(programInput, 'r')
    except IOError:  # IOError ValueError
        logging.exception('Caught an error')
        time.sleep(1)
        print('The file did not exist.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        newInput = chooseFile()
        return checkFile(newInput)
    else:
        usableFile.close()
        return programInput


def importFile(fileName):
    outputList = []
    openFile = open(fileName, 'r')
    for name in openFile:
        correctedName = name.rstrip('\n')
        outputList += correctedName
    openFile.close()
    lower = 0
    digit = 0
    space = 0
    upper = 0
    for character in outputList:
        if character.isupper():
            upper += 1
        elif character.isdigit():
            digit += 1
        elif character.isspace():
            space += 1
        elif character.isalpha():
            lower += 1
    return upper, lower, digit, space


def output(name, uppercase, lowercase, digits, whitespace):
    print(f'\nThe file "{name}" contains the following content:')
    print(f'Uppercase Letters: {uppercase}')
    print(f'Lowercase Letters: {lowercase}')
    print(f'Digits: {digits}')
    print(f'Whitespace: {whitespace}\n')


def main():
    thatExists = checkFile(FILE_LOCATION)
    result = importFile(thatExists)
    output(thatExists, result[0], result[1], result[2], result[3])


if __name__ == '__main__':
    main()
