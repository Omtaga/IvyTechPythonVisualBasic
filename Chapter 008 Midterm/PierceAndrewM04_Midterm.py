# Ivy Tech - SDEV 140 - Introduction to Software Development
# Midterm Exam - Programming: Create sentence from words input one at a time into a list and output number of words.
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6


def userInput():
    wordsInput = []
    continueInput = True
    while continueInput:
        word = input("Please type a word you would like to add to your sentence: ")
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
    finishedSentence = ""
    inputWords[0] = inputWords[0].capitalize()
    for wordIndex in range(len(inputWords)):
        if wordIndex == len(inputWords) - 1:
            finishedSentence += inputWords[wordIndex]
        else:
            finishedSentence += inputWords[wordIndex] + " "
    return finishedSentence


def defineIsAre(inputWords):
    if len(inputWords) == 1:
        return "is"
    else:
        return "are"


def definePlural(inputWords):
    if len(inputWords) == 1:
        return ""
    else:
        return "s"


def main():
    inputWords = userInput()
    sentence = combineWords(inputWords)
    plural = definePlural(inputWords)
    isAre = defineIsAre(inputWords)
    print(f'{sentence}.')
    print(f'There {isAre} {len(inputWords)} word{plural} in the sentence.')


if __name__ == "__main__":
    main()
