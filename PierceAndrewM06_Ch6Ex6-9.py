# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 5 Exercise 17-18. Prime Numbers and Prime Number List
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


def chooseFile():
    directory = os.listdir()
    increment = 1
    for files in directory:
        print(f'{increment}. {files}')
        increment += 1
    fileChoice = int(input("Enter desired file: ")) - 1
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
        print('Please phrase your response as "1" or "2".')
        userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        else:
            fileQuestion()


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
