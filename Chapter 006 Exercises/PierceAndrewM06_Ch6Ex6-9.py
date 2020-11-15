# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 6 Exercise 6 & 9. Average of Numbers and Exception Handling
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import logging
import time
import os


def inputHandling(openFile):
    while True:
        try:
            total = 0
            increment = 0
            for line in openFile:
                lineAmount = float(line.rstrip('\n'))
                total += lineAmount
                increment += 1
        except ValueError:
            logging.exception('Caught an error')
            time.sleep(1)
        else:
            return total / increment


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
            # Makes sure input is greater than one.
            if float(userInput) <= 1 or float(userInput) % 1 != 0 or float(userInput) > len(array) - 1:
                print("Your input was invalid, please choose a file using the numerical keys.")
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
    if fileChoice < 1 or fileChoice > len(directory) or fileChoice % 1 != 0:
        print('Invalid input, please try again.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        chooseFile()
    fileName = directory[fileChoice]
    return directory[fileChoice]


def enterFile():
    try:
        typedFile = input("Enter the name of the file you'd like to use: ")
        usableFile = open(typedFile, 'r')
    except IOError:  # IOError ValueError
        logging.exception('Caught an error')
        time.sleep(1)
        print('The file did not exist.')
        userQuit = input("Hit enter to choose from a list or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        chooseFile()
    else:
        usableFile.close()
        return typedFile


def fileQuestion():
    print('This program will find the average of numbers within a file.')
    print('Would you like to:')
    print('1.) Choose from a list?')
    print('2.) Enter a file name?')
    answer = input('Please enter a "1" or a "2": ')
    if answer == '1':
        return True
    elif answer == '2':
        return False
    else:
        print('Your response was invalid, please choose a file from a list.')
        userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        else:
            return True


def main():
    # Average Numbers in a file: Ask to choose file from list or enter a file name.
    if fileQuestion():
        activeFile = chooseFile()
    else:
        activeFile = enterFile()
    openFile = open(activeFile, 'r')
    result = inputHandling(openFile)
    print(f'The average of the lines in {activeFile} is {result}')
    openFile.close()


if __name__ == '__main__':
    main()
