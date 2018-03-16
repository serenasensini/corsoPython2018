#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15 mar 2018

@author: Serena Sensini
'''

import sys
import random

ans = True

while ans:
    question = raw_input("Chiedi alla palla magica qualunque cosa. Per uscire, premi invio" +"\n")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "Meglio non dirlo ora."
    
    elif answers == 2:
        print "Ne sei sicuro?"
    
    elif answers == 3:
        print "Direi proprio di sì."
    
    elif answers == 4:
        print "La mia risposta è no."
    
    elif answers == 5:
        print "Chiedimelo più tardi."
    
    elif answers == 6:
        print "Ci puoi contare."
    
    elif answers == 7:
        print "Le mie fonti dicono di sì."
    
    elif answers == 8:
        print "Dovresti rifletterci di più."