# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:24:55 2022

@author: Tomek
"""

'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

from datetime import datetime

# raport.write('{}'.format(datetime.now()))

# limit = int(gigant/2)
# naj_dzielnik = 0
szukana = 0

def largest_prime_factor(gigant):
    
    raport = open('Problem_2.txt', mode = 'w')
    raport.write('{}: Zaczynam szukanie...\n'.format(datetime.now()))
    print('{}: Zaczynam szukanie...\n'.format(datetime.now()))
   
    for maly_dzielnik in range(2,gigant+1):
        if gigant%maly_dzielnik==0:
            mozliwa_pierwsza = int(gigant/maly_dzielnik)
            raport.write('\n{}: Znaleziono dzielnik: {}. Sprawdzanie, czy jest to liczba pierwsza.'.format(datetime.now(),mozliwa_pierwsza))
            print('\n{}: Znaleziono dzielnik: {}. Sprawdzanie, czy jest to liczba pierwsza.'.format(datetime.now(),mozliwa_pierwsza))
            for liczba in range(2,mozliwa_pierwsza):
                                    
                    if mozliwa_pierwsza%liczba==0:
                            raport.write('\n{}: Dzielnik {} nie jest liczba pierwsza,poniewaz jest podzielna przez {}. Szukam dalej\n.'.format(datetime.now(),mozliwa_pierwsza,liczba))
                            print('\n{}: Dzielnik {} nie jest liczba pierwsza, poniewaz jest podzielna przez {}. Szukam dalej\n.'.format(datetime.now(),mozliwa_pierwsza,liczba))
                            break
                    
                    elif liczba+1 == mozliwa_pierwsza:
                       raport.write('\n{}: Dzielnik {} jest liczba pierwsza! Konczymy zabawe!'.format(datetime.now(),mozliwa_pierwsza))
                       print('\n{}: Dzielnik {} jest liczba pierwsza! Konczymy zabawe!'.format(datetime.now(),mozliwa_pierwsza))
                       print('\nRozwiazanie to: {}.'.format(mozliwa_pierwsza))
                       raport.close()
                       return mozliwa_pierwsza
                
    return
                
                
            #     if gigant%liczba==0 and mozliwa_pierwsza!=gigant:
            #         raport.write('\n{}: Dzielnik {} nie jest liczba pierwsza,poniewaz jest podzielna przez {}. Szukam dalej\n.'.format(datetime.now(),mozliwa_pierwsza,liczba))
            #         print('\n{}: Dzielnik {} nie jest liczba pierwsza, poniewaz jest podzielna przez {}. Szukam dalej\n.'.format(datetime.now(),mozliwa_pierwsza,liczba))
            #         break
            #     elif gigant%liczba==0 and mozliwa_pierwsza==gigant:
            #         raport.write('\n{}: Dzielnik {} jest liczba pierwsza! Konczymy zabawe!'.format(datetime.now(),mozliwa_pierwsza))
            #         print('\n{}: Dzielnik {} jest liczba pierwsza! Konczymy zabawe!'.format(datetime.now(),mozliwa_pierwsza))
            #         print('\nRozwiazanie to: {}.'.format(mozliwa_pierwsza))
            #         raport.close()
            #         return mozliwa_pierwsza
            #     break
            # else:
            #     raport.write('\n{}: Cos nie tak, niczego nie znalazlem.'.format(datetime.now()))
            #     print('\n{}: Cos nie tak, niczego nie znalazlem.'.format(datetime.now()))
            #     raport.close()
            #     return

largest_prime_factor(600851475143)