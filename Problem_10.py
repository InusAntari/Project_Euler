# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:38:27 2022

@author: Tomek
"""

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from datetime import datetime

def count_primes(liczba):
    # plik = open('Problem 10_{}.txt'.format(liczba),mode='w+')
    print('{}: Zaczynam szukanie...\n'.format(datetime.now()))
    # plik.write('{}: Zaczynam szukanie...\n'.format(datetime.now()))
    
    #sprawdzenie czy wpisano 0 lub 1
    if liczba <2:
        return 0
    
    # 2 albo wiecej
    pierwsze = [2]
    counter = 3
    suma = 0
    
    while counter <= liczba:
        for y in range(3,counter,2): #co drugie, bo pojamy w ten sposob liczby parzyste
            if counter%y==0:
                counter += 2
                break
        
        else:
            # print(counter)
            pierwsze.append(counter)
            print('Dodaje {}\n'.format(counter))
            # plik.write('Dodaje {}\n'.format(counter))
            print('Do tej pory znaleziono {} liczb pierwszych.\n'.format(len(pierwsze)))
            # plik.write('Do tej pory znaleziono {} liczb pierwszych.\n\n'.format(len(pierwsze)))                                             
            counter += 2
    
    print('{}: Dla wartosci ponizej {} znaleziono w sumie {} liczb pierwszych.\n'.format(datetime.now(),liczba,len(pierwsze)))
    # plik.write('{}: Dla wartosci ponizej {} znaleziono w sumie {} liczb pierwszych.\n'.format(datetime.now(),liczba,len(pierwsze)))
    print('{}: Licze ich sume...'.format(datetime.now()))
    # plik.write('{}: Licze ich sume...\n'.format(datetime.now()))
    for element in pierwsze:
        suma += element
    
    print('{}: Liczenie zakonczono!'.format(datetime.now()))
    # plik.write('{}: Liczenie zakonczono!'.format(datetime.now()))
    print('{}: Suma znalezionych liczb wynosi {}.'.format(datetime.now(), suma))
    # plik.write('{}: Suma znalezionych liczb wynosi {}.'.format(datetime.now(),suma))
    
    # plik.close()
    return suma

wynik = count_primes(2000000)