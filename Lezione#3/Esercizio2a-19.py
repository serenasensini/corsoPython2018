#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def secondMajor(lista):
	if len(lista) > 1:
		lista.sort()
		lista.reverse()
		return lista[1]
	else:
		return "Impossibile trovare il secondo elemento"
		
lista = []
print secondMajor(lista)
lista = [1]
print secondMajor(lista)
lista = [6,4]
print secondMajor(lista)
lista = [2,9,7,1,8,5,6]
print secondMajor(lista)