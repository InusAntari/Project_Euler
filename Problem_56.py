# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 18:24:15 2022

@author: Tomek
"""

'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
'''

wynik_final = 0

def sumaProblem56 (a,b):
    
    suma = 0
    liczba = a**b
    liczba_str = str(liczba)
    
    for cyfra in liczba_str:
        
        suma += int(cyfra)
    
    return suma

for a in range(1,101):
    for b in range(1,101):
        
        wynik = sumaProblem56(a, b)
        
        if wynik > wynik_final:
            
            wynik_final = wynik

print(wynik)