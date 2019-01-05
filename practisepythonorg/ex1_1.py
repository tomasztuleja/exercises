#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# cooperation between str & int, without loop

name = input("Type your name: ")
number = int(input("Type your number: "))

numberstr = str(number) + '\n'

print("{}, Your number will be print out so many times, as it's worth:".format(name))
print(numberstr * number)
