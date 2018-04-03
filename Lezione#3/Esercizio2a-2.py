def maxLista(lista):
	max = 0
	for element in lista:
		if element > max:
			max = element
	return max
	
#alternativa
def maxLista(lista):
	return max(lista)