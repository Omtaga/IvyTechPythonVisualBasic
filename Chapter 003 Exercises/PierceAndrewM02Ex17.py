# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 3 Exercise 17. Wi-Fi Diagnostic Tree
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.9.0

import sys

# Handles expected input as described explicitly by the text book.


def simpleQuestion():
    answer = input('Did that fix the problem? ')
    if answer == 'Yes' or answer == 'yes':
        return True
    elif answer == 'No' or answer == 'no':
        return False
    else:
        print("Please phrase your response as 'yes' or 'no'.")
        userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
        if userQuit == 'q':
            sys.exit("Quitting Program")
        else:
            simpleQuestion()


def main():
    print()
    print('Reboot the computer and try to connect.')
    response = simpleQuestion()
    if response is False:
        print('Reboot the router and try to connect.')
        response = simpleQuestion()
        if response is False:
            print('Make sure the cables between the router and modem are plugged in firmly.')
            response = simpleQuestion()
            if response is False:
                print('Move the router to a new location.')
                response = simpleQuestion()
                if response is False:
                    print('Get a new router.')


main()


