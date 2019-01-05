#!/usr/bin/env python

# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

num = int(input("Type first Integer: "))
check = int(input("Type second Integer: "))
numbycheck = num / check
numcheck = num % check

    
if numcheck == 0:
    print("First Integer was devided evenly by the second. The result that is {}.".format(int(numbycheck)))
else:
    print("First Integer was devided NOT evenly by the second. The result that is {}.".format((numbycheck)))
