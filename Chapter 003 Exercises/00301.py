x = int(input("Please enter a whole number for variable x: "))

y = 0
z = 0

if x > 100:
    y = 20
    z = 40
    print(f"Since your input is greater than 100 your input, x is...")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
else:
    print(f"Since your input is less than or equal to 100 your input, x is...")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
