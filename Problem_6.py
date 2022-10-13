# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:42:23 2022

@author: Tomek
"""

'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + 3**2 +...+ 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+3+...+10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is
3025-385 = 2640
Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

suma = 0
suma_kwadratow = 0

for liczba in range(1,101):
    suma +=liczba
    suma_kwadratow += liczba**2
    
print(abs((suma**2)-suma_kwadratow))