# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:17:16 2022

@author: Tomek
"""

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

silnia_100 = 1
suma = 0

for i in range(1,101):
    silnia_100 *=i

print(silnia_100)

silnia_str = str(silnia_100)

for i in silnia_str:
    suma +=int(i)
    
print(suma)