# Total Purchase
# Simple Regsiter Program

print("In the fields below, enter the prices of five items")
totalAmount = float(input("What is the price of the first item? "))
totalAmount += float(input("What is the price of the second item? "))
totalAmount += float(input("What is the price of the third item? "))
totalAmount += float(input("What is the price of the fourth item? "))
totalAmount += float(input("What is the price of the fifth item? "))
print()
salesTax = totalAmount * .07
print(f'The sales tax is ${salesTax:,.2f}')
print(f'The total is ${salesTax + totalAmount:,.2f}')