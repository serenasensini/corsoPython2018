'''
Created on 25 mar 2018

@author: Serena Sensini
'''
def count_occurences(word):
    counter = 0
    for element in word:
        if 'a' == element or 'A' == element:
            counter += 1
    return counter

a = 'banana'
b = 'Aiuola'
c = 'Abracadrabra'
d = 'Elfo'

print count_occurences(a)
print count_occurences(b)
print count_occurences(c)
print count_occurences(d)