#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Auto:
    
    def __init__(self, targa, anno_immatricolazione, marca, modello):
        self.targa = targa
        self.anno_immatricolazione = anno_immatricolazione
        self.marca = marca
        self.modello = modello
        
    def __repr__(self):
        print "L'auto targata " + self.targa + " immatricolata nel " + str(self.anno_immatricolazione) + " è una " + self.marca + " " + self.modello
        
auto1 = Auto("DN543LN", 2009, "Toyota", "Yaris")
auto1.__repr__()