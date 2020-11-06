# Chapter 2 Exercise 10. Ingredient Adjuster
# Andrew M. Pierce
# Python 3.9.0


# Converts a whole number less than 1000 to English.
def toAlpha(number):
    stringCookies = str(number)
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if len(stringCookies) > 3:
        return int(number)
    elif len(stringCookies) < 2:
        return ones[int(stringCookies[0]) - 1]
    elif len(stringCookies) == 2:
        if int(stringCookies) % 10 == 0:
            return tens[int(stringCookies[0]) - 1]
        else:
            if stringCookies[0] == '1':
                return teens[int(stringCookies[1]) - 1]
            else:
                return tens[int(stringCookies[0]) - 1] + '-' + ones[int(stringCookies[1]) - 1]
    else:
        if int(stringCookies) % 100 == 0:
            return ones[int(stringCookies[0]) - 1] + ' hundred'
        elif int(stringCookies[2]) == 0:
            return ones[int(stringCookies[0]) - 1] + ' hundred ' + tens[int(stringCookies[1]) - 1]
        elif int(stringCookies[1]) == 0:
            return ones[int(stringCookies[0]) - 1] + ' hundred ' + ones[int(stringCookies[1]) - 1]
        elif int(stringCookies[1]) == 1:
            return ones[int(stringCookies[0]) - 1] + ' hundred ' + teens[int(stringCookies[2]) - 1]
        else:
            return ones[int(stringCookies[0])-1]+' hundred '+tens[int(stringCookies[1])-1]+'-'+ones[int(stringCookies[2])-1]


def main():

    cupsOfSugar = 1.5 / 48
    cupsOfButter = 1 / 48
    cupsOfFlour = 2.75 / 48

    print('\n\n')
    print("This program gives you the ingredients required for mom's famous cookie recipe.")
    numberOfCookies = int(input(f"How many cookies will you be baking:  "))
    print()

    # Adds the ability to add an 's' if the word 'cookie' should be plural.
    multiple = '' if numberOfCookies == 1 else 's'

    # Creates a variable to determine if result was a string or integer.  Avoids recalculating function in if statement.
    phraseResult = toAlpha(numberOfCookies)

    # If result of toAlpha() was str, prints output, else adds commas in the correct place.
    # Also could use type(phraseResult) == str instead of isinstance
    if isinstance(phraseResult, str):
        print(f'To create {phraseResult} cookie{multiple}, use the following ingredients:')
    else:
        print(f'To create {phraseResult:,d} cookie{multiple}, use the following ingredients:')

    print()
    print(f'Use:')
    print(f'{numberOfCookies * cupsOfSugar:,.2f} Cups of Sugar')
    print(f'{numberOfCookies * cupsOfButter:,.2f} Cups of Butter')
    print(f'{numberOfCookies * cupsOfFlour:,.2f} Cups of Flour')
    print('\n')
    input('Press enter to exit...')
    print('\n')


main()
