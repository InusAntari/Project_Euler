# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:02:21 2022

@author: Tomek
"""
'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''


suma = 0

for i in range(1,1001):
    
    suma += (i**i)
    
suma_str = str(suma)

print(suma_str[-10:])