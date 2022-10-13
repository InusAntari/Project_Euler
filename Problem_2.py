# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:16:26 2022

@author: Tomek
"""

'''Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do 
not exceed four million, find the sum of the even-valued terms.'''

ciag_fibbo = [1,2]
ciag_fibbo_parzyste = []

while ciag_fibbo[-1]<4000000:
    nowa_liczba = ciag_fibbo[-2]+ciag_fibbo[-1]
    if nowa_liczba>4000000:
        break
    else:
        ciag_fibbo.append(nowa_liczba)

for liczba in ciag_fibbo:
    if liczba%2==0:
        ciag_fibbo_parzyste.append(liczba)
    else:
        pass

wynik = sum(ciag_fibbo_parzyste)
print(wynik)