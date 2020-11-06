
a = int(input("Please enter a whole number for value 'a':  "))
b = None
if a < 10:
    b = 0
    print(f'Since variable "a" is less than 10, variable "b" equals {b}')
else:
    b = 99
    print(f'Since variable "a" is greater than or equal to 10, varible "b" equals {b}')
