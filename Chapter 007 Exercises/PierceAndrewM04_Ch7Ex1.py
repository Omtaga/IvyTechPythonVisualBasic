# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 7 Exercise 1. Total Sales
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import logging
import time


def inputHandling(question):
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
    result = 0
    for dailyTotal in weeklyTotal:
        result += float(dailyTotal)
    return result


def output(week, day, salesTotal):
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
    salesTotalAndDay = userInput(week)
    salesTotal = computeSalesTotal(salesTotalAndDay[0])
    day = salesTotalAndDay[1]
    output(week, day, salesTotal)


if __name__ == '__main__':
    main()
