# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:08:52 2022

@author: Tomek
"""

wartosci = []

for a in range(2,101):
    
    for b in range(2, 101):
        
        wartosci.append(a**b)
        
print(len(set(wartosci)))