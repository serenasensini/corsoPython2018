'''
Created on 25 mar 2018

@author: Serena Sensini
'''

def count_even_numbers(lista):
    counter = 0
    for element in lista:
        if element % 2 == 0:
            counter += 1
            
    return counter

print count_even_numbers([2,3,4,7,5,1,10,0])