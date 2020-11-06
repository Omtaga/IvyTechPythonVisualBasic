# Ivy Tech - SDEV 140 - Introduction to Software Development
# Chapter 4 Exercise 14. Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *
# Andrew M. Pierce  Associate of Applied Science - Software Development
# Python 3.9.0

print()
row = 7
column = 7
for r in range(row):
    for c in range(column):
        print('*', end='')
    column -= 1
    print()
