#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def lunghezzaStringa(stringa):
	counter = 0
	for element in stringa:
		counter += 1
	return counter
	
stringa = ""
print lunghezzaStringa(stringa)
stringa = "abba"
print lunghezzaStringa(stringa)