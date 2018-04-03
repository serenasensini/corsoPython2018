#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def mostraOperazioni(a,b):
	if(a < b):
		tempA = b
		tempB = a
	else:
		tempA = a
		tempB = b
	somma = "La somma è: " + str(tempA+tempB) + "\n"
	differenza = "La differenza è " + str(tempA-tempB) + "\n"
	prodotto = "Il prodotto è " + str(tempA*tempB) + "\n"
	divisione = "La division è " + str(tempA/tempB) + "\n"
	
	return somma + differenza + prodotto + divisione
	
print mostraOperazioni(4,3)
print mostraOperazioni(4,7)