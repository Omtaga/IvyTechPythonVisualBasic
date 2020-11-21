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
    # Checks user input from list generated from chooseFile() returns verified input or quits program on
    # user request
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
    # After failure to use expected file, this function forces choice from list or program termination.
    # Returns user selected file into program or quits on user command.
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
        chooseFile(sex)
    return directory[fileChoice]


def checkFile(ifValid, sex):
    # Checks to make sure expected file is available. Returns string of file name.
    try:
        usableFile = open(ifValid, 'r')
    except IOError:  # IOError ValueError
        logging.exception('Caught an error')
        time.sleep(1)
        print('The file did not exist.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        # Handles missing or misspelled file and passes expected sex of file to aid user in selecting
        # correct file.
        newInput = chooseFile(sex)
        return checkFile(newInput, sex)
    else:
        usableFile.close()
        return ifValid


def inputHandling(question):
    # Takes user input and verifies provided name does not contain invalid name characters. Returns string.
    while True:
        typedInput = input(question)
        # Raises exception if input does not contain only alphanumerics, allowing correct input.
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
    # Takes input from validated file (exists but not content) and returns list of strings in file.
    outputList = []
    openFile = open(fileName, 'r')
    for name in openFile:
        correctedName = name.rstrip('\n')
        outputList.append(correctedName)
    openFile.close()
    return outputList


def output(theName, sex, result):
    # Prints output of user provided name, sex and result of list searches.
    if result:
        print(f"{theName} was a popular {sex} name from 2000 through 2009!")
    else:
        print(f"{theName} was not a popular name from 2000 through 2009.")


def popularName(theName, boyNames, girlNames):
    # Creates grammar for output and passes string and a boolean result of search in list of boy
    # and girl files.
    if theName in boyNames and theName in girlNames:
        return "boy and girl", True
    elif theName in boyNames:
        return "boy", True
    elif theName in girlNames:
        return "girl", True
    else:
        return "", False


def main():
    # Default file names provided in constant FILE_LOCATIONS located at the top of this
    # program (approx line 12).
    # The next two lines verifies the location and availability of the files, gives option to
    # choose from list if file names incorrect or file not available.
    boyFile = checkFile(FILE_LOCATIONS[0], 'boy')
    girlFile = checkFile(FILE_LOCATIONS[1], 'girl')
    boyNames = importFile(boyFile)
    girlNames = importFile(girlFile)
    theName = inputHandling("\nEnter a name to see if it was a popular baby name between 2000 to 2009: ")
    result = popularName(theName, boyNames, girlNames)
    output(theName, result[0], result[1])


if __name__ == '__main__':
    main()
