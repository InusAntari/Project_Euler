# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:14:00 2022

@author: Tomek
"""

'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

a=str(2**1000)
suma = 0

for cyfra in a:
    suma += int(cyfra)
    
print(suma)