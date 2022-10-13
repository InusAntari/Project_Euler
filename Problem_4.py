# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:06:11 2022

@author: Tomek
"""

'''
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def largest_palindrom():
    lista_palindromow = []
    
    for palindrom in reversed(range(10000,998002)):
        palindrom_odwrocony_string = str(palindrom)[::-1]
        
        if palindrom_odwrocony_string == str(palindrom):
            lista_palindromow.append(palindrom)

    for element in lista_palindromow:
    
        for liczba in reversed(range(100,1000)):
           if element%liczba==0 and len(str(int(element/liczba)))==3 and (element/liczba)%1==0:
             druga_liczba = element/liczba
             return print('Ten palindrom to {}, a liczby to {} i {}'.format(element,liczba,druga_liczba))
         
largest_palindrom()