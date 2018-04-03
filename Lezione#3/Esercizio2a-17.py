#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def palindroma(stringa):
	return stringa[::-1] == stringa
	#alternativa
	'''
	str = ""
	for i in stringa:
		str = i + str
	return str
	'''
	#alternativa
	'''
	string = "".join(reversed(string))
    return string
	'''

	
print palindroma("eriunnanononannuire")
print palindroma("anna")
print palindroma("roma")