"""
Created on Tue Feb 23 15:39:15 2021

@author: Javier
"""
import random

def moneda():
    moneda = random.random()
    if moneda < 0.7:
        print("cara")
    else:
        print("cruz")
    return

moneda()
