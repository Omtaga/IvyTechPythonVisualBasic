
a = int(input("Please enter a whole number for variable 'a':  "))
b = None
c = None
if a < 10:
    b = 0
    c = 1
    print(f'Since a is less than 10, b = {b} and c = {c}')
else:
    if b is None and c is None:
        b = "'Nothing'"
        c = "'Nothing'"
    print(f'Since a is greater than or equal to 10, b = {b} and c = {c}.')

