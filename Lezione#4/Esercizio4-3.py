#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Personaggio:
    
    def __init__(self, nome, potere, citazione):
        self.nome = nome 
        self.potere = potere
        self.citazione = citazione
        
    def __repr__(self):
        print "Ciao! Sono " + self.nome + ", il mio potere è " + self.potere
        print "Il mio mantra è: " + self.citazione

class Mago(Personaggio):
    
    def __init__(self, nome, potere, citazione, oggetti_magici):
        Personaggio.__init__(self, nome, potere, citazione)
        self.oggetti_magici = oggetti_magici
    
    def __repr__(self):
        Personaggio.__repr__(self)
        if len(self.oggetti_magici) > 0:
            print "Possiedo questi oggetti magici: ",
            for element in self.oggetti_magici:
                if self.oggetti_magici[len(self.oggetti_magici)-1] != element:
                    print element +  "," ,
                else:
                    print element
        
    
class Strega(Personaggio):
    
    def __init__(self, nome, potere, citazione, maledizione):
        Personaggio.__init__(self, nome, potere, citazione)
        self.maledizione = maledizione
        
    def __repr__(self):
        Personaggio.__repr__(self)
        print "Ti maledico! " + self.maledizione
        
m = Mago("Mago Merlino", "realizzare i tuoi sogni", "Oketi Poketi!", ["Bastone", "Anacleto"])
m.__repr__()