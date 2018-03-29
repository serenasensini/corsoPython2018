'''
Created on 25 mar 2018

@author: Serena Sensini
'''
def count_occurences(word):
	#elemento contatore, che incremento ogni volta che la condizione nell'if è soddisfatta
    counter = 0
	#per ogni elemento (in questo caso un carattere) della stringa...
    for element in word:
		# ...se l'elemento è uguale a "a" in maiuscolo o minuscolo...
        if 'a' == element or 'A' == element:
			#incremento il contatore
            counter += 1
	#fuori dal ciclo, ritorno il valore
    return counter

a = 'banana'
b = 'Aiuola'
c = 'Abracadrabra'
d = 'Elfo'

print count_occurences(a)
print count_occurences(b)
print count_occurences(c)
print count_occurences(d)