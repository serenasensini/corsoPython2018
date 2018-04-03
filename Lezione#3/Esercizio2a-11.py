#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def divisibilePerCinque(numero):
	if numero % 5 == 0:
		return True
	else:
		return False
	#alternativa
	#return numero % 5 == 0
	
print divisibilePerCinque(15)
print divisibilePerCinque(7)