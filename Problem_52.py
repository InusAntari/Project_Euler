# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:03:08 2022

@author: Tomek
"""

'''
It can be seen that the number, 125874, and its double, 251748, contain 
exactly the same digits, but in a different order. Find the smallest positive 
integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def problem_52():
    
    liczba_sprawdzana = 1
    while True:
        
        print('Sprawdzam liczbe: {}'.format(liczba_sprawdzana))
        razy2 = liczba_sprawdzana*2
        razy3 = liczba_sprawdzana*3
        razy4 = liczba_sprawdzana*4
        razy5 = liczba_sprawdzana*5
        razy6 = liczba_sprawdzana*6
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        
        for liczba in str(liczba_sprawdzana):
            lista1.append(float(liczba))
        
        for liczba in str(razy2):
            lista2.append(float(liczba))
        
        for liczba in str(razy3):
            lista3.append(float(liczba))
            
        for liczba in str(razy4):
            lista4.append(float(liczba))
            
        for liczba in str(razy5):
            lista5.append(float(liczba))
        
        for liczba in str(razy6):
            lista6.append(float(liczba))
        
        lista1.sort()
        lista2.sort()
        lista3.sort()
        lista4.sort()
        lista5.sort()
        lista6.sort()
        
        if lista1 == lista2:
            if lista1 == lista3:
                if lista1 == lista4:
                    if lista1 == lista5:
                        if lista1 == lista6:
                            print('Znalazlem liczbe: {}'.format(liczba_sprawdzana))
                            return
        
        liczba_sprawdzana += 1
        
problem_52()