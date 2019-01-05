#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

inp = int(input("Type an Integer: "))

test = inp % 2
testfour = inp % 4

if test == 0:
    print("It's an even number!")
    if testfour == 0:
        print("It's also a multiple of 4!") 
else:
    print("It's an odd number!")
