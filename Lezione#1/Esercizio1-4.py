'''
Created on 15 mar 2018

@author: Serena Sensini
'''
def whatIf(parametro):
    if(parametro == "piove"):
        print "Rimanda appuntamento"
    elif(parametro == "sole"):
        print "Puoi partecipare all'evento"
    else:
        print "Non ho capito"
        
whatIf("piove") #primo caso
whatIf("sole")  #secondo caso
whatIf("Testo di prova")    #terzo caso