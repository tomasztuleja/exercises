#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# How many years to 100 years old. When?

name  = (input("Type your name: "))
age = int(input("Type your number: "))

toHundred = 100 - age
hundred = 2018+toHundred

print("{}, you left {} years to 100.\nThat will happen in  {} year".format(name, toHundred, hundred))
