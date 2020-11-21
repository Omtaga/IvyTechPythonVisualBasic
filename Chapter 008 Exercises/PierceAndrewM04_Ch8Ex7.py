# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 8 Exercise 7. Character Analysis
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import time
import logging
import os

FILE_LOCATION = 'text.txt'


def checkUserChoice(question, array):
    # If provided file choice fails this function forces user to choose a file from program directory or quit program.
    # Returns verified int or quits, users initiated program end.
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
    # If provided file is misspelled or missing, allows user to choose from active program directory or quit
    # returns string of user selected file name or user initiated program termination.
    directory = os.listdir()
    increment = 1
    for files in directory:
        print(f'{increment}. {files}')
        increment += 1
    fileChoice = checkUserChoice("Enter desired file: ", directory)
    if fileChoice < 0 or fileChoice >= len(directory) or fileChoice % 1 != 0:
        print('Invalid input, please try again.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        chooseFile()
    return directory[fileChoice]


def checkFile(ifValid):
    # Checks if default file provided is available, if file check fails runs chooseFile().
    # returns string of valid default file name or user selected input. User allowed to terminate program on check fail.
    try:
        usableFile = open(ifValid, 'r')
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
        return ifValid


def importFile(name):
    # Takes valid file and checks all characters for string types, checks upper first and then alpha to check for
    # lowercase characters.
    # Returns four integers.
    outputList = []
    openFile = open(name, 'r')
    for paragraph in openFile:
        simplified = paragraph.rstrip('\n')
        outputList += simplified
    openFile.close()
    upper = 0
    lower = 0
    digit = 0
    space = 0
    for character in outputList:
        if character.isupper():
            upper += 1
        elif character.isalpha():
            lower += 1
        elif character.isdigit():
            digit += 1
        elif character.isspace():
            space += 1
    return upper, lower, digit, space


def output(name, uppercase, lowercase, digits, whitespace):
    # Prints to screen results of select data gathered from file.
    print(f'\nThe file "{name}" contains the following content:')
    print(f'Uppercase Letters: {uppercase}')
    print(f'Lowercase Letters: {lowercase}')
    print(f'Digits: {digits}')
    print(f'Whitespace: {whitespace}\n')


def main():
    # Checks for valid file. Attempts to use default file name, global constant located at top of this program
    # named FILE_LOCATION (approx line 11).
    thatExists = checkFile(FILE_LOCATION)
    # Reads data from file and returns it.
    result = importFile(thatExists)
    # Takes data read from file and outputs.
    output(thatExists, result[0], result[1], result[2], result[3])


if __name__ == '__main__':
    main()
