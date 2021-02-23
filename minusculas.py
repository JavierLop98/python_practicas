"""
Created on Tue Feb 23 15:53:51 2021

@author: Javier Lopez Bahon
Introducido un string devuelve unicamente las minúsculas
"""

# Python3 program to Split string into characters
def split(word):
	return [char for char in word] 
	
# Driver code
word = 'Javier Lopez Bahon'
lista = split(word)
for i in lista:
    if  i.islower():
        print (i)
