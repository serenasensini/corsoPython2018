#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def pariODispari(numero):
	if numero % 2 == 0:
		return "Pari"
	else:
		return "Dispari"
	
print pariODispari(0)
print pariODispari(6)
print pariODispari(17)