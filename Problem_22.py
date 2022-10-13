# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:37:09 2022

@author: Tomek
"""

import string
lista_imion = []
wynik_koncowy = 0
wartosci_liter = dict(zip(string.ascii_uppercase, range(1,27)))
#uzyskanie listy samych imion

plik = open('names.txt','r')
tekst = plik.read()
plik.close()
tekst2 = tekst.split(',')

for imie in tekst2:
    lista_imion.append(imie[1:-1])

# posortowanie alfabetycznie imion
lista_imion.sort()

#dla kazdego z imion uzyskanie jego wartosci
for index,imie in enumerate(lista_imion):
    wynik_imienia = 0
    for litera in imie:
        wynik_imienia +=wartosci_liter[litera]
    #pomnozenie wartosci imienia razy pozycja na liscie
    #dodanie uzyskanego wyniku do wyniku koncowego
    wynik_koncowy += (wynik_imienia * (index+1))

print(wynik_koncowy)