#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def productLista(lista):
	#controllo se la lista è maggiore di zero: se sì, il counter lo imposto a 1; altrimenti, il prodotto di una lista vuota è 0
	if len(lista) > 0:
		counter = 1
		for element in lista:
			counter *= element
	else: 
		counter = 0
	return counter

#lista vuota
lista = []	
print productLista(lista)
#lista
lista = [1,2,3,4]
print productLista(lista)
#lista di zeri
lista = [0,0,0,0]
print productLista(lista)

