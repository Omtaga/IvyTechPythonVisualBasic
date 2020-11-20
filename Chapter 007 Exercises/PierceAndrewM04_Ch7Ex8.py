# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 7 Exercise 8. Name Search
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import time
import sys
import logging


FILE_LOCATIONS = ['BoyNames.txt', 'GirlNames.txt']


def inputHandling(question):
    while True:
        try:
            typedInput = input(question)
            typedInput.isalpha()
        except ValueError:
            logging.exception('Caught an error')
            # Pauses program so that exception prints to screen
            # and user sees next step to continue after error message.
            time.sleep(1)
            print("The name may not include anything other than letters.")
            userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
            if userQuit == 'q':
                sys.exit("Quitting Program")
        else:
            typedInput = typedInput.lower().capitalize()
            return typedInput


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
    boyNames = importFile(FILE_LOCATIONS[0])
    girlNames = importFile(FILE_LOCATIONS[1])
    theName = inputHandling("\nEnter a name to see if it was a popular baby name between 2000 to 2009: ")
    result = popularName(theName, boyNames, girlNames)
    output(theName, result[0], result[1])


if __name__ == '__main__':
    main()
