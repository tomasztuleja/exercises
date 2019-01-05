#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# even and odd number

inp = int(input("Type an Integer: "))
flo = float(inp)
test = flo % 2.0

if test == 0.0:
    print("That is an even number, indeed!")
else:
    print("That is an odd number.")
