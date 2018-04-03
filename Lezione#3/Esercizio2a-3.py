def maxStringa(lista):
	max = 0
	for element in lista:
		if len(element) > max:
			max = len(element)
	return max
	
lista = ['ab','aba','abbba', 'a', 'acca']
print maxStringa(lista)