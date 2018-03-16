'''
Created on 15 mar 2018

@author: Serena Sensini
'''
freddo = True
caldo = not freddo
pioggia = False
nuvoloso = True
brutto_tempo = pioggia or nuvoloso
vento = True
neve = True
tormenta = vento and neve

print caldo
print brutto_tempo
print tormenta