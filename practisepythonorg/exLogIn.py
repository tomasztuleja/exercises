#!/usr/bin/env python

# My first try:) 

# Take from user @LOGIN and PASSWORD

# Conditions for @LOGIN and PASSWORD
logChar = ('@', '.')
passChar = ()
lowabc = map(chr, range(97, 123))
upabc = map(chr, range(65, 91))


# Defined input variable and type for login and PASSWORD
def logIN():
    global l
    l = str(input())

def passIN():
    global p
    p = str(input())



# Here will be checked the length and if @LOGIN contains @ and a . (dot).
def logCheck1():
    for letter in l[:]:
        if letter == logChar[0]:
            return True

def logCheck2():
    for letter in l[:]:
        if letter == logChar[1]:
            return True

def logCheck3():            
    if len(l[:]) not in range(5):
        return True

# Here will be checked the PASSWORD
# PASSWORD length
def passCheck3():
    if len(p[:]) not in range(0,6):
        return True
# Type the PASSWORD
def typepass():
    print("PASSWORD \n- Min. 6 characters \n Type your password: ")
    while passIN() not in passChar:
        while passCheck3() !=True:
            print("Remember about min. 6 characters! ")
            break
        else:
            pass
            break

# Type the @LOGIN
def typelog():         
    print("Type your email adress: ")
    while logIN() not in logChar:
        while (logCheck1() and logCheck2() and logCheck3()) != True:
            print("There is something wrong with your mail. Try again.")
            break
        else:
            #Type the PASSWORD
            typepass()
        
            break

# Run the program
typelog()

#Print to check if the program runs right
#print("\n\n")
#print(l.lower().strip())



#passIN()
#if passCheck1() == True:
#    print("1 OK")
    
#if passCheck2() == True:
#    print("2 OK")    
    
#if passCheck3() == True:
#    print("3 OK")    
    


