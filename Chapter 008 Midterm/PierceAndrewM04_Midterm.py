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
        if word:
            continueInput = True
        else:
            continueInput = False
            del inputList[-1]
    inputList[0] = inputList[0].capitalize()
    for index in range(len(inputList)):
        if index == len(inputList) - 1:
            result += inputList[index]
        else:
            result += inputList[index] + " "
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
