# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:49:58 2022

@author: Tomek
"""
'''
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.
'''

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