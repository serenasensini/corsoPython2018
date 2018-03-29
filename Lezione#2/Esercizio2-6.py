'''
Created on 25 mar 2018

@author: Serena Sensini
'''

#range(start,stop,step)
'''
Ragionamento:
1) Per stampare una stringa al contrario, dovrò partire dall'ultimo carattere, fino al primo, prendendo ogni volta l'elemento precedente;
2) Si tratta di un'operazione ripetitiva, quindi uso un ciclo for;
3) Nel ciclo, uso range, dove come intervallo di partenza (start) ho l'ultimo elemento della stringa (basta prendere la lunghezza della stringa, e togliere 1 per via della notazione zero-index based); come intervallo di fine (stop) uso -1, perché devo prendere fino al carattere nella prima posizione e lo stop non viene considerato come intervallo inclusivo (il numero nello stop è il numero a cui si ferma); lo step sarà di meno uno, così che vada a ritroso.
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