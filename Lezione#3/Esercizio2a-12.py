#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def divisibilePerSetteNonPerCinque(numero):
	if numero % 7 == 0 and numero % 5 != 0:
		return True
	else:
		return False
	#alternativa
	#return numero % 7 == 0 and numero % 5 != 0
	
print divisibilePerSetteNonPerCinque(35)
print divisibilePerSetteNonPerCinque(7)
print divisibilePerSetteNonPerCinque(15)