"""
Created on Mon Feb 22 12:29:35 2021

@author: Javier López Bahón

Programa que pide una letra al usuario y devuelve otra letra del abacedario 
desplazada n veces de la dada.
"""

def pedir_letra():
    letra = input('¿Qué letra te gusta?')
    while len(letra)>1:
        letra = input('Introduzca una única letra:')        
    letra = letra.upper()
    return letra

def pedir_n():
    n = input('¿Cuantas posiciones vas a desplazar?')
    return n

def n_desplazado (n, valor_letra):
    n = int(n)
    while n > 26:
        n = n - 26
    if (n + valor_letra) > 25:
        n_nuevo = n+valor_letra-26
    else:
        n_nuevo = valor_letra + n
    return n_nuevo

def mostrar_nueva_letra(n):
    
    return print('Tu nueva letra es:',chr(n))

def main():
    letra = pedir_letra()
    n = pedir_n()
    valor_letra=ord(letra)-65
    n = n_desplazado(n,valor_letra) #juntar con la linea de arriba
    mostrar_nueva_letra(n+65)
  
    
main()
    
