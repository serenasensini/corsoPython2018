#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Azienda:
    
    def __init__(self, nome, anno_fondazione, direttore, sede_principale, numero_filiali):
        self.nome = nome
        self.anno_fondazione = anno_fondazione
        self.direttore = direttore
        self.sede_principale = sede_principale
        self.numero_filiali = numero_filiali
        
    def __repr__(self):
        print "L'azienda " + self.nome + " fondata nel " + str(self.anno_fondazione) + " ha come direttore il sig. " + self.direttore + " e la sua sede principale si trova a " + self.sede_principale + ". Conta " + str(self.numero_filiali) + " filiali."
        
azienda1 = Azienda("F_society", 2009, "Mr. Robot", "Coney Island", 1)
azienda1.__repr__()