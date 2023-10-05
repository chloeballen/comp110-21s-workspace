"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


import random

print("Welcome to the Underwhelming Fortune Teller")

start = input('Press enter to begin')


print("Your fortune cookie says...")

fortune = random.randint(1,4)

if fortune == 1:
    print("You will find cash you forgot you had.")
else:
    if fortune == 2:
        print("You will eat your favorite meal but it's a little cold.")
    else:
        if fortune == 3:
            print("You will get to work from home tomorrow afternoon.")
        else:
            if fortune == 4:
                print("You will see a cool bird but it poops on you car.")
        
print("Now, go spread positive vibes!")



