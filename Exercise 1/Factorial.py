from math import *

userIn = int(input("Enter a number"))
difference = 1
for x in range (1, (userIn+1)):
    difference = difference * x

print("The factorial of ", userIn, "is " , difference)