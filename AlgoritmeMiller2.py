# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:17:02 2021

@author: ana_p
"""

import numpy as np
from sympy import mod_inverse


#Algoritme de Miller. 
def Miller(P,Q,S,t,p,N):
    T=np.array(P,dtype=np.float64)
    f=1
    e=num(N)
    for i in range(t-1,-1,-1):
        f=f**2*h(T,T,S,p)
        T=mult2(T,p)
        if e[i]==1:
            f=f*h(T,P,S,p)
            T=suma(T,P,p)
    return f%p
    
#Funció que retorna un nombre N en forma binària
def num(N):
    e=[]
    while N!=0:
        e.insert(0,N%2)
        N=N//2
    return e
    
#Funció que retorna la funció h_{P,Q} en funció de si lambda és infinit (False) o no ho és (True).
def h(P,Q,S,p):
    [x,y]=S
    [a1,a2,xP,yP,xQ,yQ]=constantes(P,Q)
    [lam,l]=lamda(P,Q,p)
    if lam == True:
        #utilitzam la funció mod_inverse per calcular la inversa en aritmètica modular
        hPQ=(y-yP-l*(x-xP))*mod_inverse(x+xP+xQ-l**2-a1*l+a2,p)
    else:
        hPQ=(x-xP)
    return hPQ


#Funció on ficam totes les constants que utilitzam
def constantes(P,Q):
    #Guardam totes les constants necessàries.
    a1=0
    a2=0
    xP=P[0]
    yP=P[1]
    xQ=Q[0]
    yQ=Q[1]
    
    #Si P=Q, llavors:
    if np.array_equal(P,Q)==True:
        return [a1,a2,xP,yP,xP,yP]
    #Si P!=Q, llavors:
    else:
        return [a1,a2,xP,yP,xQ,yQ]


#Funció que retorna lambda, que és el pendent de la recta que uneix P i Q, en funció de si P=Q, P!=Q o si és vertical. 
def lamda(P,Q,p):
    [a1,a2,xP,yP,xQ,yQ]=constantes(P,Q)
    #Si P=Q, llavors:
    if np.array_equal(P,Q)==True:
        #pendiente de la recta tengente
        l=(3*xP**2+30)/(2*yP)
        lam=True 
    else:
        #Si alguna de les dues components són iguals, llavors:
        if xP==xQ or yP==yQ:
            lam=False
            l=0 #No se usa, no sé como no ponerlo
        #sino:
        else:
            lam=True
            PQx=int(xQ-xP)
            PQy=int(yQ-yP)
            l=PQy/(PQx)        
    return [lam,l]

#Funció que suma dos punts d'una corba el·líptica.
def suma(P,Q,p):
    [xP,yP]=P
    [xQ,yQ]=Q
    l=(yQ-yP)*mod_inverse(xQ-xP,p)
    Sx=l**2-xP-xQ
    Sy=l*(xP-Sx)
    Sy=Sy-yP
    S=[Sx%p,Sy%p]
    return S

#Funció que multiplica un punt d'una corba el·líptica per l'escalar 2.
def mult2(P,p):
    [xP,yP]=P
    a=30
    l=(3*xP**2+a)*mod_inverse(2*yP,p)
    Sx=l**2-2*xP
    Sy=l*(xP-Sx)
    Sy=Sy-yP
    S=[Sx%p,Sy%p]
    return S

print(Miller([36,60],[121,387],[0,36], 3,631,5))
