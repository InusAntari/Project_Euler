# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:06:45 2022

@author: Tomek
"""

'''
The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the 
1000-digit number that have the greatest product. What is the value of this 
product?
'''

import math

def thirteen_digits():
    
    plik = open('C:\\Users\\Tomek\\OneDrive\\Szkolenie Python\\Project Euler\\Problem 8.txt', mode='r')
    kod_literki = []
    naj_mnozenie = 0
    
    kod = plik.read()
    kod = kod.replace('\n','')
    # print(kod)
    # print(len(kod))
    for litera in kod:
        kod_literki.append(int(litera))
    # print(kod_literki)
    
    for i in range(0,len(kod_literki)-12):
        mnozenie = math.prod(kod_literki[i:i+13])
        if mnozenie > naj_mnozenie:
            naj_mnozenie = mnozenie
            print('Znaleziono najwyzszy wynik: {} dla proby {}.'.format(naj_mnozenie,i))
    
    plik.close()
    return print('Najwyzszy wynik dla calej liczby wynosi {}.'.format(naj_mnozenie))

thirteen_digits()