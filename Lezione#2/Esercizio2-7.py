'''
Created on 25 mar 2018

@author: Serena Sensini
'''

def divisibiliPerCinque(lista):
    for element in lista:
        if element % 5 == 0:
            print element

lista1 = [10, 23, 45, 92, 70, 1020, 71]
divisibiliPerCinque(lista1)