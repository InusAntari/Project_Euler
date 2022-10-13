# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:00:13 2022

@author: Tomek
"""

def problem_25(limit):
    lista = [1,1,2]
    while True:
        if len(str(lista[-1])) == limit:
            print('Pasujaca wartosc to: {}.'.format(lista[-1]))
            print('Pasujaca wartosc ma {} miejsce w ciagu.'.format(len(lista)))
            break
        else:
            lista.append(lista[-2]+lista[-1])
            
problem_25(1000)