'''
Created on 25 mar 2018

@author: Serena Sensini
'''

'''Ragionamento
1) Devo scorrere tutti gli elementi della lista: uso un ciclo for;
2) Devo controllare che l'elemento, diviso per 5, non dia resto; significa che è divisibile per quel numero: uso l'operatore modulo;
3) Se è divisibile, stampo l'elemento.
'''

def divisibiliPerCinque(lista):
	#per ogni elemento nella lista
    for element in lista:
		#se l'elemento, diviso 5, dà resto 0...
        if element % 5 == 0:
			#stampa l'elemento
            print element

lista1 = [10, 23, 45, 92, 70, 1020, 71]
divisibiliPerCinque(lista1)