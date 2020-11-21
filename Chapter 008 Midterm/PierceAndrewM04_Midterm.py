# Ivy Tech - SDEV 140 - Introduction to Software Development
# Midterm Exam - Programming: Create sentence from words input one at a time into a list and output number of words.
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6

import sys
import time
import logging


def inputHandling(question):
    # Takes user input and verifies provided name does not contain invalid name characters. Returns string.
    # Only accepts numbers and alphanumerics.
    # Allows user to exit on input failure.
    while True:
        typedInput = input(question)
        # Raises exception if input does not contain only alphanumerics or numbers, allowing correct input.
        if typedInput.isalpha() or typedInput.isdigit():
            return typedInput
        else:
            try:
                raise
            except Exception:
                logging.exception('Caught an error')
                # Pauses program so that exception prints to screen
                # and user sees next step to continue after error message.
                time.sleep(1)
                print("The name may not include anything other than letters or numbers but not mixed.")
                userQuit = input("Hit enter to continue or type 'q' and enter to quit: ")
                if userQuit == 'q':
                    sys.exit("Quitting Program")


def userInput():
    # Runs loop to gather words from user, checks user input for numbers and alphanumerics, returns list.
    wordsInput = []
    continueInput = True
    while continueInput:
        word = inputHandling("Please type a word you would like to add to your sentence: ")
        if word == "i":
            word = "I"
        wordsInput.append(word)
        yesNo = input('Type "y" to continue or anything else to stop: ')
        if yesNo == "Yes" or yesNo == "yes" or yesNo == "Y" or yesNo == "y":
            continueInput = True
        else:
            continueInput = False
    return wordsInput


def combineWords(inputWords):
    # Takes list and capitalizes first word, joins with space until last word. Returns string.
    finishedSentence = ""
    inputWords[0] = inputWords[0].capitalize()
    for wordIndex in range(len(inputWords)):
        if wordIndex == len(inputWords) - 1:
            finishedSentence += inputWords[wordIndex]
        else:
            finishedSentence += inputWords[wordIndex] + " "
    return finishedSentence


def defineIsAre(inputWords):
    # Grammar: Determines if 'is' or 'are' is needed based on number of words in sentence created.
    # Output - String
    if len(inputWords) == 1:
        return "is"
    else:
        return "are"


def definePlural(inputWords):
    # Grammar: Determines if a word needs 's' to be plural based on number of words in list.
    # Output - String
    if len(inputWords) == 1:
        return ""
    else:
        return "s"


def main():
    # Takes user input, checks for 'i', asks to continue, returns list.
    inputWords = userInput()
    # Capitalize first word, joins words, returns string.
    sentence = combineWords(inputWords)
    # Grammar for adding the letter 's' to a word.
    plural = definePlural(inputWords)
    # Grammar to determine is & are.
    isAre = defineIsAre(inputWords)
    print(f'{sentence}.')
    print(f'There {isAre} {len(inputWords)} word{plural} in the sentence.')


if __name__ == "__main__":
    main()
