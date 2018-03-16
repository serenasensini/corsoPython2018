#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15 mar 2018

@author: Serena Sensini
'''

import sys
import random

ans = True
answer = random.randint(1,99)

while ans:
    
    number = input("Indovina che numero ho pensato? Per uscire, premi Invio" + "\n")
    
    if number == "":
        print "Gioco terminato!"
        sys.exit()
    
    elif answer == number:
        print "Hai vinto!"
        ans = False
        
    elif number < answer:
        print "Troppo basso. Ritenta"
        
    elif number > answer:
        print "Troppo alto. Ritenta"
        