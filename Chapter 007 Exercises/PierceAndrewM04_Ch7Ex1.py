# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 7 Exercise 1. Total Sales
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import logging
import time


def inputHandling(question):
    # Takes user input question and checks to make sure input is a number. Output is a float.
    while True:
        try:
            typedAmount = input(question)
            isinstance(float(typedAmount), str)
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
            return float(typedAmount)


def userInput(week):
    # Take input from user, expects a number, returns array of numbers and number of day of week of
    # last input.
    day = 0
    inputAmount = []
    continueInput = True
    while continueInput and day < 7:
        word = inputHandling(f"Please enter the sales for {week[day]}: ")
        inputAmount.append(word)
        if day < 6:
            yesNo = input('Type "y" to continue or anything else to stop: ')
            if yesNo == "Yes" or yesNo == "yes" or yesNo == "Y" or yesNo == "y":
                continueInput = True
            else:
                continueInput = False
        day += 1
    return inputAmount, day - 1


def computeSalesTotal(weeklyTotal):
    # Takes array argument and totals a result, returns a float.
    result = 0
    for dailyTotal in weeklyTotal:
        result += float(dailyTotal)
    return result


def output(week, day, salesTotal):
    # Takes days of week, and outputs last date input along with formatting for correct grammar for output.
    if salesTotal == 0:
        print('There were no sales for this week.')
    elif day == 0:
        print(f'Sales for Sunday were ${salesTotal:,.2f}.')
    elif day == 1:
        print(f'Sales for Sunday and Monday were ${salesTotal:,.2f}.')
    else:
        print(f'Sales for Sunday thru {week[day]} was ${salesTotal:,.2f}.')


def main():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    print('\nEnter sales for each day to see the sales for the past week.')
    # Asks for user input of sales amounts for each day of week sales are available.
    salesTotalAndDay = userInput(week)
    # Takes list of sales from userInut() and creates/returns sum.
    salesTotal = computeSalesTotal(salesTotalAndDay[0])
    # Takes number from salesTotalAndDay and converts to variable day help with clarity of arg in output.
    day = salesTotalAndDay[1]
    output(week, day, salesTotal)


if __name__ == '__main__':
    main()
