from math import *

money = int(input("How much money do you have"))
print("A Nintendo Wii is 100 pesos. You have ", money)
afford = floor (money / 100)
print("You can buy ", afford)

short = 100 - (money - (100*afford))
print("You need ", short, " pesos more to buy another Nintendo Wii")