# Miles-per-Gallon

print()
print('Find the miles-per-gallon performance\nof your car.')
print()
milesDriven = int(input("How many miles did you travel? "))
gallonsUsed = int(input("How many gallons were consumed? "))
print()
print(f'Your vehicle achieved {milesDriven / gallonsUsed:,.2f} miles-per-gallon\non that trip.')
