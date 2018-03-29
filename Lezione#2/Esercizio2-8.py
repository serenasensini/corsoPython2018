'''
Created on 25 mar 2018

@author: Serena Sensini
'''


'''Ragionamento
1) Devo definire una funzione per calcolare l'area di base (quadrata): definisco una funzione con def, che chiamo area; gli passo un parametro chiamato "lato" e ritorno, tramite return, il prodotto del lato per sé stesso;
2) Per calcolare il volume, dovrò calcolare l'area di base e moltiplicarla per altezza, dividendo per 3; definisco con def una funziona volume dove passo come parametri sia il lato che l'altezza; il lato verrà usato per calcolare l'area, mentre l'altezza verrà usata nella formula prima specificata.
'''

from twisted.test.test_process import Accumulator

def area(lato):
    return lato * lato 

def volume(lato, altezza):
    return area(lato) * altezza / 3

lato = 5
altezza = 3
print volume(lato, altezza)