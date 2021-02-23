"""
Created on Tue Feb 23 16:14:51 2021

@author: Introduce un texto y devuelve el texto con . donde habia letras minúsculas.
"""

txt = "Banana"

txt = list(txt)

for i in range(len(txt)):
    if  txt[i].islower():
        if(txt[i]=='A' or txt[i]=='a' or txt[i]=='E' or txt[i] =='e' or txt[i]=='I'
         or txt[i]=='i' or txt[i]=='O' or txt[i]=='o' or txt[i]=='U' or txt[i]=='u'):
            txt[i] = '.'

txt=' '.join(txt)
print(txt)
