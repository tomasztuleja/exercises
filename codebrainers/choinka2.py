#!/usr/bin/env python

def high():
    global c
    c = int(input("How tall should be the christmas tree? "))

def tree():
    r = c-1
    l = 0

    for i in range(r):
        print(" ", end="")

    if r>0:
        print("*")

    for i in range(r):
        l +=1

        for i in range(r-l):
            print(" ", end="")

        print("*", end="")

        for i in range(0+l):
            print("*", end="")
        for i in range(0+l):
            print("*", end="")
    
        print(" ")



high()
    
while c in range(2):
        
    print("Did you see so small christmas tree? Try again\n")
    high()
            
else:
    tree()
    