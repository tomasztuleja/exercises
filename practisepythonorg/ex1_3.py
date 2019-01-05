#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Print all nymbers from 0 to input without loop

name = input("Type your name: ")
number = int(input("Type your number: "))

numberone = number + 1
r = list(range(0,numberone))


print("{}, you'll see numbers from o to {}:".format(name, number))
print(r[:numberone])