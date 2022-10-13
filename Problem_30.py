# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:49:58 2022

@author: Tomek
"""

def problem30(liczba, potega):
    #funkcja rozbija liczbe na cyfry skladowe, podnosi je do potegi i sumuje
    
    liczba_str = str(liczba)
    suma = 0
    
    for a in liczba_str:
        
        cyfra_int = int(a)
        suma += cyfra_int**potega
    
    return suma

wynik = 0
        
for i in range(2,10000000):
    
    if i == problem30(i,5):
        
        wynik += i
        
print(wynik)