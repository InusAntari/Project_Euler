# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:40:19 2022

@author: Tomek
"""

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. 
There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
Find the product abc.
'''

warunek = False
tabela = [1,1,1]

while warunek == False:
    
    print('Sprawdzam warunek dla kompletu: {} | {} | {}'.format(tabela[0],tabela[1],tabela[2]))
    if (tabela[0]+tabela[1]+tabela[2]==1000) and ((tabela[0]**2 + tabela[1]**2)==tabela[2]**2):
        print('Znalazlem wartosci!')
        print('Wartosci wynosza a:{}, b:{}, c:{}.'.format(tabela[0],tabela[1],tabela[2]))
        print('Wyrazenie przyjmuje wtedy postac:{} + {} = {}.'.format(tabela[0]**2,tabela[1]**2,tabela[2]**2))
        print('Ich iloczyn wynosi {}.'.format(tabela[0]*tabela[1]*tabela[2]))
        warunek = True
        
    #jezeli a=500 przerwij program
    if tabela[0] == 500:
        print('Program osiagnal zalozony limit. ABORT! ABORT! ABORT!')
        break
    
    #jezeli b=500, zwieksz a o 1, b ustaw na 1
    elif tabela[1] == 500:
        tabela[0]+=1
        tabela[1]=1
        tabela[2]=1
    
    #jezeli c=500, zwieksza b o 1, c ustaw na 1
    elif tabela[2] == 500:
        tabela[1]+=1
        tabela[2]=1
    
    #sprawdz warunek, jezeli False, zawieksz c o 1
    else:
        tabela[2]+=1
   
    #sprawdz warunek, jezeli True, zmien warunek i wydrukuj wartosci
   