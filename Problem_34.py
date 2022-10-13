# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:46:20 2022

@author: Tomek
"""

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial 
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

def problem34(liczba):
    #funkcja liczy sume poteg kazdej z cyfr
    
    from math import factorial
    
    liczba_str = str(liczba)
    suma = 0
    
    for i in liczba_str:
        
        suma += factorial(int(i))
        
    return suma

wynik = 0

for a in range(3,10000001):
    
    if a == problem34(a):
        
        wynik += a
        
print(wynik)