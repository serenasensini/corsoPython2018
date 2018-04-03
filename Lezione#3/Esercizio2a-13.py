#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def compresoTra(numero):
	if numero >= 0 and numero <= 99:
		return True
	else:
		return False
	#alternativa
	return numero >= 0 and numero <= 99
	
print compresoTra(3)
print compresoTra(-2)
print compresoTra(95)
print compresoTra()