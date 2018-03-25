'''
Created on 25 mar 2018

@author: Serena Sensini
'''
parola = 'parolaAlContrario'

def reverse(stringa):
    for element in range(len(stringa)-1,0,-1):
        print stringa[element]
        
reverse(parola)

'''
Alternativa
'''

def reverse2(stringa):
    index = len(stringa)-1
    while index > 0:
        print stringa[index]
        index -= 1

reverse2(parola)

'''
Alternativa
'''
def reverse3(stringa):
    print stringa[::-1]

reverse3(parola)