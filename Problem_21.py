# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:22:34 2022

@author: Tomek
"""

def amicable_numbers(limit):
    
    sprawdzana_wartosc = 1
    lista_liczb = []
    wynik = 0
    while sprawdzana_wartosc < limit:
        lista_dzielnikow1 = []
        suma_dzielnikow1 = 0
        lista_dzielnikow2 =[]
        suma_dzielnikow2 = 0
        #sprawdzenie dzielnikow liczby
        for i in range(1,sprawdzana_wartosc):
            if sprawdzana_wartosc%i == 0:
                lista_dzielnikow1.append(i)
            else:
                pass
        
        #obliczenie sumy dzielnikow
        suma_dzielnikow1 = sum(lista_dzielnikow1)
        
        #sprawdzenie dzielnikow sumy
        for x in range(1,suma_dzielnikow1):
            if suma_dzielnikow1%x == 0:
                lista_dzielnikow2.append(x)
            else:
                pass
        
        #sprawdzenie sumy dzielnikow sumy
        suma_dzielnikow2 = sum(lista_dzielnikow2)
        
        #stwierdzenie, czy sa to amicable numbers
        if (suma_dzielnikow2 == sprawdzana_wartosc) and (suma_dzielnikow1 != suma_dzielnikow2):
            lista_liczb.append(suma_dzielnikow1)
            lista_liczb.append(suma_dzielnikow2)
        else:
            pass
        sprawdzana_wartosc+=1
    
    #zrobienie setu ze zbioru liczb, by pozbyc sie powtorek
    lista_liczb = set(lista_liczb)
    #zsumowanie wartosci, by otrzymac wynik
    wynik = sum(lista_liczb)
        
    return wynik

wynik = amicable_numbers(10000)