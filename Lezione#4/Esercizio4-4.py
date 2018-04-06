#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 06 apr 2018

@author: Serena Sensini
'''

class Animale:
    
    def __init__(self, specie, habitat, vita_media):
        self.specie = specie
        self.habitat = habitat
        self.vita_media = vita_media
        
    def __repr__(self):
        print "L'animale appartiene alla specie " + self.specie + ", vive nel " + self.habitat + " ed ha una vita media di " + str(self.vita_media) + " anni."
    
    def suona(self, verso):
        return verso
    
class Cane(Animale):
    
    def __init__(self, specie, habitat, vita_media, razza, taglia, domestico=None):
        Animale.__init__(self, specie, habitat, vita_media)
        self.razza = razza
        self.taglia = taglia
        self.domestico = domestico
        
    def __repr__(self):
        Animale.__repr__(self)
        if(self.domestico != None and self.domestico == True):
            print "Il cane appartiene alla razza dei " + self.razza + ", è di taglia " + self.taglia + " ed è un cane domestico."
        elif(self.domestico != None and self.domestico == False):
            print "Il cane appartiene alla razza dei " + self.razza + ", è di taglia " + self.taglia + " e non è un cane domestico."
        else:
             print "Il cane appartiene alla razza dei " + self.razza + ", è di taglia " + self.taglia + "."
        
    def suona(self):
        return "Bau!"
            
class Elefante(Animale):
    
    def __init__(self, specie, habitat, vita_media,razza, rischio_estinzione):
        Animale.__init__(self, specie, habitat, vita_media)
        self.razza = razza
        self.rischio_estinzioe = rischio_estinzione
        
    def suona(self):
        return "FFFFFFFFFFFFF"
        
c = Cane("canide", "continentale", 12, "Bovaro del Bernese", "Gigante", True)
c.__repr__()
print c.suona()