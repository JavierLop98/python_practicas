# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:13:22 2021

@author: USUARIO
"""

import sys
from mrjob.job import MRJob

def suma_doble(pares):
    """
    De una lista de valores tipo ((int,int...),(int,int...)) hace un sumatorio
    de las listas.

    Parameters
    ----------
    pares : ((int,int...),(int,int...))
        lista con dos listas dentro.

    Returns
    -------
    a : int
        Sumatorio de la primera lista.
    b : int
        Sumatorio de la segunda lista.

    """
    a, b = 0, 0
    for x, y in pares:
        a, b = a + x, b + y
    return a, b

class MRSumaParos(MRJob):
    """
    Función map_reduce: del archivo datos_limpios.txt, la función mapper limpia
    los datos y retorna key(comunidad, anno), values(paro, 1). Con esto la 
    función reducer suma los paros y el números de datos de paro que se han
    tomado.
    """
    def mapper(self, _, linea):
        comunidad, edad, anno, paro = linea.split(";")
        try:
            paro = float(paro.replace(',','.'))
        except:
            paro = 0.0
        yield (comunidad, anno), (paro, 1)
        
    def reducer(self, key, values):
        yield key, suma_doble(values)

def main():
    archivo_datos = sys.argv[1]
    datos = MRSumaParos(args=[archivo_datos])   
    """
    Una vez realizado el map_reduce, partimos del sumatorio de paros y nº de 
    datos de paro por cada provincia y año, con que para tener la media,
    simplemente dividimos value[0] / value[1], esto lo pasamos a string y lo 
    imprimimos en el nuevo archivo.
    """
    with datos.make_runner() as runner:
        runner.run()
        f= open("paro_por_anno_mapreduce.txt","w+")
        for key, value in datos.parse_output(runner.cat_output()):
            media = value[0] / value[1]
            media_str = str(round(media, 2))
            escribir = (key[0] + " - " + key[1] + ";" + media_str + "\n")
            f.write(escribir)
        f.close()
            
main()