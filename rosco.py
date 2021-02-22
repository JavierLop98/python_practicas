"""
Created on Mon Feb 22 12:29:35 2021

@author: Javier López Bahón

Programa que pide una letra al usuario y devuelve otra letra del abacedario 
desplazada n veces de la dada.
"""

import numpy as np
import string

def crear_diccionario_letras1():
    letras = list(string.ascii_uppercase)
    numeros = np.arange(len(letras))
    rosco_letras = dict(zip(letras, numeros))
    return rosco_letras

def crear_diccionario_letras2():
    letras = list(string.ascii_uppercase)
    numeros = np.arange(len(letras))
    rosco_numeros = dict(zip(numeros, letras))
    return rosco_numeros

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

def mostrar_nueva_letra(n,rosco_numeros):
    
    return print('Tu nueva letra es:',rosco_numeros[n])

def main():
    rosco_letras = {}
    letra = pedir_letra()
    n = pedir_n()
    rosco_letras = crear_diccionario_letras1()
    valor_letra = int(rosco_letras[letra])
    n = n_desplazado(n, valor_letra)
    rosco_numeros={}
    rosco_numeros=crear_diccionario_letras2()
    mostrar_nueva_letra(n, rosco_numeros)
    
main()
    
