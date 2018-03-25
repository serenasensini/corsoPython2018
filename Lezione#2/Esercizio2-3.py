'''
Created on 25 mar 2018

@author: Serena Sensini
'''
def equalTo(number_list, number):
    counter = 0
    for element in number_list:
        if number == element:
            counter += 1
    return counter

print equalTo([1,2,3,2,2,3,5,6],2)