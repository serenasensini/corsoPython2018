#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

nome = raw_input("Qual è il tuo nome? ")
cognome = raw_input("Qual è il tuo cognome? ")
data_nascita = raw_input("Qual è la tua data di nascita? Scriverla nel formato dd/MM/yyyy ")

file = open("dati.txt", "w+")
file.write(nome + "\n")
file.write(cognome + "\n")
file.write(data_nascita + "\n")
file.close()

with open("dati.txt", "r+") as f: 
    for line in f:
        print line