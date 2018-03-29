'''
Created on 25 mar 2018

@author: Serena Sensini
'''
#un numero è pari quando la sua divisione per 2 restituisce 0; anche 0 è considerato pari
def count_even_numbers(lista):
	#elemento contatore, che incremento ogni volta che la condizione nell'if è soddisfatta
    counter = 0
	#per ogni elemento della lista di numeri..
    for element in lista:
		# ...se la divisione dell'elemento per 2 dà resto 0..
        if element % 2 == 0:
			# ...incremento il contatore
            counter += 1
	#fuori dal ciclo, ritorno il risultato
    return counter

print count_even_numbers([2,3,4,7,5,1,10,0])