#!/usr/bin/env python

#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
d = []


# a elements less/equal than 5
for element in a:
    if element <= 5:
        print(element)
    else:
        pass
# a elements less/equal than 5 in a new list
for element in a:
    if element <=5:
        b.append(element)
    else:
        pass

print(b)

# a elements less/equal than input

def inp():
    global c 
    c = int(input("Type an Integer: "))

def func():      
    for element in a:               
        if c in a and element <= c:
            d.append(element)
                                         
        #elif c not in a:
        #    print("Too much, you're out of the list. Try again\n")
        #    break   
    if len(d) != 0:
        print(d)
    else:
        pass
# OBSERVATIONS:
# Take an Integer untli it's equal to random element in list a.
# The condition 'while inp() not in a' is allways true: python can't compare function to list.
# c is a global variable, after it was 'taken' from 'inp()' python could compare c to a[] element
while inp() not in a:  
    while c not in a:
        print("You're out of the list. Try again:\n")
        break    
    else:
        if c in a:
            func()
        break     

print("\n\n\n")
# Funkcja lambda
print("Funkcja LAMBDA")
print(list(filter(lambda x:x<5, a)))
   