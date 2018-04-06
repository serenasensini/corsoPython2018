#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Opera:
    
    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento):
        self.titolo = titolo
        self.autore = autore
        self.anno_commissione = anno_commissione
        self.luogo_esposizione = luogo_esposizione
        self.anno_ritrovamento = anno_ritrovamento
        
    def __repr__(self):
        print "L'opera intitolata " + self.titolo + " il cui autore è " + self.autore + " è stata commissionata nel " + str(self.anno_commissione) + " e si trova a " + self.luogo_esposizione
        
    
class Quadro(Opera):
    
    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento, tecnica_pittura, cornice=None, restauratore=None):
        Opera.__init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento)
        self.tecnica_pittura = tecnica_pittura
        self.cornice = cornice
        self.restauratore = restauratore
    
class Scultura(Opera):
    
    def __init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento, materiale, base):
        Opera.__init__(self, titolo, autore, anno_commissione, luogo_esposizione, anno_ritrovamento)
        self.materiale = materiale
        self.base = base
        
q = Quadro("Les Demoiselles d'Avignon", "Pablo Picasso", 1907, "MoMa New York", 1916, "Olio su tela")
q.__repr__()