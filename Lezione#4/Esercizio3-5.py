#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Persona:
    
    def __init__(self, nome, cognome, anno_nascita, citta_nascita, genitori, citta_residenza):
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita
        self.citta_nascita = citta_nascita
        self.genitori = genitori
        self.citta_residenza = citta_residenza

    def __repr__(self):
        print "Il/la sig. " + self.nome + " " + self.cognome + " nato/a a " + self.citta_nascita + " nel " + str(self.anno_nascita) + " è figlio di " + str(self.genitori) + " e attualmente risiede a " + self.citta_residenza
        
    def setResidenza(self, nuovaResidenza):
        self.citta_residenza = nuovaResidenza
        
    
persona1 = Persona("Mario", "Rossi", 1987, "Roma", ["Lucia Bianchi", "Luca Rossi"], "Milano")
persona1.__repr__()

persona1.setResidenza("Torino")
persona1.__repr__()