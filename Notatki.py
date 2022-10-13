# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:45:15 2022

@author: Tomek
"""

# a = 7*3*1*6*7*1*7*6*5*3*1*3*3

# print(a)

def front_back(wyraz):
  nowy = []
  for litera in wyraz:
      nowy.append(litera)
  pierwsza = nowy[0]
  ostatnia = nowy[-1]
  nowy[0] = ostatnia
  nowy[-1] = pierwsza
  wynik = ''
  for i in nowy:
    wynik +=i
  return wynik

print(front_back('a'))