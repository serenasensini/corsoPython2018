def sommaLista(lista):
	counter = 0
	for element in lista:
		counter += element
	return counter

#lista vuota
lista = []	
print sommaLista(lista)
#lista
lista = [1,2,3,4]
print sommaLista(lista)
#lista di zeri
lista = [0,0,0,0]
print sommaLista(lista)

