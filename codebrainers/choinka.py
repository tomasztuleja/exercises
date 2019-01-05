#!/usr/bin/env python
l = 0
r = int(input("How high should be the christmas tree? "))

for x in range(r):
    l += 1
    
    for i in range(r-l):
        print(" ", end="")
    for y in range(0+l):
        print("*", end="")
    for z in range(0+l):
        print("*", end="")
    print("\n")
  
        
    