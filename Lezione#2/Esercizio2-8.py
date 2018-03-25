'''
Created on 25 mar 2018

@author: Serena Sensini
'''
from twisted.test.test_process import Accumulator

def area(lato):
    return lato * lato 

def volume(lato, altezza):
    return area(lato) * altezza / 3

lato = 5
altezza = 3
print volume(lato, altezza)