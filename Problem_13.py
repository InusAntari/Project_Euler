# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:29:16 2022

@author: Tomek
"""

'''
Work out the first ten digits of the sum of the following 
one-hundred 50-digit numbers.
'''

zrodlo = open('Problem 13 - kod.txt', 'r')
suma = 0

kod = zrodlo.read()
numerki = kod.split('\n')
for liczba in numerki:
    suma += int(liczba)
print(suma)
suma_str = str(suma)
print(suma_str[0:10])

zrodlo.close()