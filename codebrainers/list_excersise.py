#!/usr/bin/env python

imiona_string = "Iga julia Aleksandra Zofia oliwia Kinga Krzysztof antoni Jan Piotr kacper Jakub"
foreign_names_string = "Alex George Jeanette Michael"

# 0 - utwórz listy z podanych ciągów znaków
print("# 0 - utwórz listy z podanych ciągów znaków\n")
imiona_string = imiona_string.split()
foregin_names_string = foreign_names_string.split()

print("imiona_string type: ",type(imiona_string))
print("foregin_names_string type: ", type(foregin_names_string))
print("\n")

# 1 - wyswietl z name_list imiona kobiet
print("# 1 - wyswietl z name_list imiona kobiet\n")
for i in imiona_string:
    if i.endswith("a"):
        print(i," ", end="")
print("\n")

# 2 - usuń z listy imiona Piotr i Zofia
print("# 2 - usuń z listy imiona Piotr i Zofia\n")
imiona_string.remove("Piotr")
imiona_string.remove("Zofia")
print(imiona_string)
print("\n")

# 3 - utworz liste imion zaczynajacych sie na J
print("# 3 - utworz liste imion zaczynajacych sie na J\n")
jNames = []
for i in imiona_string:
    if i.startswith("J"):
        jNames.append(i)
    elif i.startswith("j"):
        jNames.append(i)
    else:
        pass
print(jNames)
print("\n")

# 4 - posortuj alfabetycznie polaczona liste imion
print("# 4 - posortuj alfabetycznie polaczona liste imion\n")
listConnect = []
for i in imiona_string:
    listConnect.append(i)
for i in foregin_names_string:
    listConnect.append(i)

def keyFunc(i):
    return i.upper()

listConnect.sort(key = keyFunc)
print(listConnect,"\n")


listConnect2 = listConnect
listConnect2.sort(key = lambda i: i.upper()) # support from stackoverflow, sort() sorts separately up and lowercase
print(listConnect2)

print("\n")

# 5 - posortuj poloczona liste wg dlugosci imion
print("# 5 - posortuj poloczona liste wg dlugosci imion\n")
listConnect3 = listConnect

def keyFunc3(i):
    return len(i)

listConnect3.sort(key = keyFunc3)
print(listConnect3)

print("\n")

# 6 - odwroc kolejnosc posortowanej listy 
print("# 6 - odwroc kolejnosc posortowanej listy \n")

listConnect4 = listConnect3
listConnect4.reverse()
print("reverse()")
print(listConnect4)

print("\n")

listConnect5 = listConnect3
listConnect5.sort(key = keyFunc3, reverse = True)
print("sort(key = keyFunc3, reverse = True)")
print(listConnect5)