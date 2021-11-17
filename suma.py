# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:03:15 2021

@author: ana_p
"""

###Suma de dos punts d'una corba el·líptica
from sympy import mod_inverse

#Sigui P=(x_P,y_P) i Q=(x_Q,y_Q), llavors la seva suma la podem definir com:
    
def suma(P,Q,p):
    [xP,yP]=P
    [xQ,yQ]=Q
    l=(yQ-yP)*mod_inverse(xQ-xP,p)
    Sx=l**2-xP-xQ
    Sy=l*(xP-Sx)
    Sy=Sy-yP
    S=[Sx%p,Sy%p]
    return S
    
print(suma([5,22], [16,27], 29))
