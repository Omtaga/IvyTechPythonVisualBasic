# Ivy Tech - SDEV 140 - Introduction to Software Development
# Midterm Exam - Programming: Create sentence from words input one at a time into a list and output number of words.
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.8.6


def main():
    result = ""
    inputList = []
    continueInput = True
    while continueInput:
        word = input("Please type a word you would like to add to your sentence: ")
        if word == "i":
            word = "I"
        inputList.append(word)
        yesNo = input('Type "y" or "n" if you\'d like to continue: ')
        if yesNo == "Yes" or yesNo == "yes" or yesNo == "Y" or yesNo == "y":
            continueInput = True
        else:
            continueInput = False
    inputList[0] = inputList[0].capitalize()
    increment = 1
    for words in inputList:
        if increment == len(inputList):
            result += words
        else:
            result += words + " "
        increment += 1
    print(f'{result}.')
    plural = ""
    isAre = ""
    if len(inputList) == 1:
        isAre += "is"
    else:
        isAre += "are"
        plural += "s"
    print(f'There {isAre} {len(inputList)} word{plural} in the sentence.')


if __name__ == "__main__":
    main()
