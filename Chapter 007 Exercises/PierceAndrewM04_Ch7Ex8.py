# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 7 Exercise 8. Name Search
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import time
import sys
import logging
import os


FILE_LOCATIONS = ['BoyNames.txt', 'GirlNames.txt']


def checkUserChoice(question, array):
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


def chooseFile(sex):
    directory = os.listdir()
    increment = 1
    for files in directory:
        print(f'{increment}. {files}')
        increment += 1
    fileChoice = checkUserChoice(f'Enter desired file for {sex} names: ', directory)
    if fileChoice < 0 or fileChoice >= len(directory) or fileChoice % 1 != 0:
        print('Invalid input, please try again.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        chooseFile()
    return directory[fileChoice]


def checkFile(ifValid, sex):
    try:
        usableFile = open(ifValid, 'r')
    except IOError:  # IOError ValueError
        logging.exception('Caught an error')
        time.sleep(1)
        print('The file did not exist.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        newInput = chooseFile(sex)
        return checkFile(newInput, sex)
    else:
        usableFile.close()
        return ifValid


def inputHandling(question):
    while True:
        typedInput = input(question)
        if typedInput.isalpha():
            typedInput = typedInput.lower().capitalize()
            return typedInput
        else:
            try:
                raise
            except Exception:
                logging.exception('Caught an error')
                # Pauses program so that exception prints to screen
                # and user sees next step to continue after error message.
                time.sleep(1)
                print("The name may not include anything other than letters.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")


def importFile(fileName):
    outputList = []
    openFile = open(fileName, 'r')
    for name in openFile:
        correctedName = name.rstrip('\n')
        outputList.append(correctedName)
    openFile.close()
    return outputList


def output(theName, sex, result):
    if result:
        print(f"{theName} was a popular {sex} name from 2000 through 2009!")
    else:
        print(f"{theName} was not a popular name from 2000 through 2009.")


def popularName(theName, boyNames, girlNames):
    if theName in boyNames and theName in girlNames:
        return "boy and girl", True
    elif theName in boyNames:
        return "boy", True
    elif theName in girlNames:
        return "girl", True
    else:
        return "", False


def main():
    boyFile = checkFile(FILE_LOCATIONS[0], 'boy')
    girlFile = checkFile(FILE_LOCATIONS[1], 'girl')
    boyNames = importFile(boyFile)
    girlNames = importFile(girlFile)
    theName = inputHandling("\nEnter a name to see if it was a popular baby name between 2000 to 2009: ")
    result = popularName(theName, boyNames, girlNames)
    output(theName, result[0], result[1])


if __name__ == '__main__':
    main()
