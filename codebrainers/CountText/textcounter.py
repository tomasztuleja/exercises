#!/usr/bin/env python3



proust = open("/home/dev/Desktop/PYex/codebrainers/CountText/proust.txt")
li = 0
tab = []

#for li in proust:
#    a+=1
#    d[a] = len(li.split()) #nr wiersza, dlugosc

text = proust.read() #czyta plik

word = text.split() #dzieli na wyrazy, TABLICA

wordlen = len(word)
print("Ilość wyrazów: ", wordlen)    # Ilość WYRAZÓW, TABLICA

for i in word:      # sumuje liczbę znaków (liter)
    for j in i:
        li+=1

print("Ilość liter: ", li)

avrword = li/wordlen    # średnia
avrwordround = round(avrword, 2)    # zaokrąglenie średniej

print("Średnia ilość znaków w wyrazie: ", avrwordround)

sentencedot = text.split(sep=".") # zdania z .
sentencelen = len(sentencedot)
sentenceshout = text.split(sep="!") #zdania z !
sentencelen2 = len(sentenceshout)
sentencewhy = text.split(sep="?")   #zdania z ?
sentencelen3 = len(sentencewhy)

allsentences = sentencelen+sentencelen2+sentencelen3 # chyba liczba zdań


print("Ilość zdań: ",allsentences)
avrsentence = li/sentencelen    # średnia ilość znaków w zdaniach

aslr = round(avrsentence, 2)    #zaokrągla średnią liczbę znaków w zdaniach

print("Średnia ilość znaków w zdaniu: ", aslr)
