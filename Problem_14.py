# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:44:42 2022

@author: Tomek
"""

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

tabela_z_wynikami = []
liczba_startowa = 1.0
najdluzszy_chain = 0.0
wynik = 0.0

while liczba_startowa < 1000000:
    
    tabela_z_wynikami.append(liczba_startowa)
    
    while tabela_z_wynikami[-1] != 1:
    
        if tabela_z_wynikami[-1]%2 ==0:
            tabela_z_wynikami.append(tabela_z_wynikami[-1]/2)
            # print('Dodaje {}'.format(tabela_z_wynikami[-1]))
            # print('Chain wyglada nastepujaco: {}'.format(tabela_z_wynikami))
        elif tabela_z_wynikami[-1]%2 == 1:
            tabela_z_wynikami.append(3*tabela_z_wynikami[-1]+1)
            # print('Dodaje {}'.format(tabela_z_wynikami[-1]))
            # print('Chain wyglada nastepujaco: {}'.format(tabela_z_wynikami))
    
    if len(tabela_z_wynikami)>najdluzszy_chain:
       najdluzszy_chain = len(tabela_z_wynikami)
       wynik = tabela_z_wynikami[0]
    # print('Caly chain dla wartosci {} wyglada tak: {}'.format(liczba_startowa,tabela_z_wynikami))
    tabela_z_wynikami.clear()
    liczba_startowa +=1

print('\n\nZakonczono liczenie!')
print('\nNajdluzszy chain o dlugosci {} zostal znaleziony dla wartosci poczatkowej {}'.format(najdluzszy_chain,wynik))