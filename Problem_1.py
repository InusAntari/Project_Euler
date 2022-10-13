# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:08:00 2022

@author: Tomek
"""

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

suma_liczb = 0

for liczba in range(1,1000):

    if liczba%3==0 or liczba%5==0:
        suma_liczb += liczba
