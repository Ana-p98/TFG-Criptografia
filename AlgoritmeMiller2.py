# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:17:02 2021

@author: ana_p
"""

import numpy as np 
from sympy import mod_inverse

#Algoritme de Miller. 
#Treballam amb la corba el·líptica y^2=x^3+1.

def Miller(P,S,p,N):
    T=P
    f=1
    [e,t]=num(N)
    for i in range(t-1,-1,-1):
        f=f**2*h(T,T,S,p)
        T=suma(T,T,p)
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
    return [e,len(e)]
    
#Funció que retorna la funció h_{P,Q}, avaluada a ub punt S, en funció de si lambda és infinit (False) o no ho és (True).
def h(P,Q,S,p):
    [x,y]=S
    [xP,yP]=P
    [xQ,yQ]=Q
    [lam,l]=lamda(P,Q,p)
    if lam == True:
        #utilitzam la funció mod_inverse per calcular la inversa en aritmètica modular
        hPQ=(y-yP-l*(x-xP))*mod_inverse(x+xP+xQ-l**2,p)
    else:
        hPQ=(x-xP)
    return hPQ


#Funció que retorna lambda, que és el pendent de la recta que uneix P i Q, en funció de si P=Q, P!=Q o si és vertical. 
def lamda(P,Q,p):
    [xP,yP]=P
    [xQ,yQ]=Q
    #Si P=Q, llavors:
    if np.array_equal(P,Q)==True:
        #pendiente de la recta tengente
        l=(3*xP**2)*mod_inverse((2*yP),p)
        lam=True 
    else:
        #Si alguna de les dues components són iguals, llavors:
        if xP==xQ or yP==yQ:
            lam=False
            l=0 #No se usa, no sé como no ponerlo
        #sino:
        else:
            lam=True
            PQx=xQ-xP
            
            PQy=yQ-yP
            l=PQy*mod_inverse(PQx,p)        
    return [lam,l]

#Funció que suma dos punts d'una corba el·líptica.
def suma(P,Q,p):
    [x1,y1]=P
    [x2,y2]=Q
    
    #Propietat: O+O=O
    if P==[None,None] and Q==[None,None]:
        x3=None
        y3=None
        return [x3,y3]
    
    #Propietat: Q+O=Q
    if P==[None,None]:
        x3=x2
        y3=y2
        return [x3,y3]
    
    #Propietat: P+O=P
    if Q==[None,None]:
        x3=x1
        y3=y1
        return [x3,y3]    
    
    #Si x1==x2 i y1+y2=0, llavors P+Q=O
    if x1==x2 and (y1+y2)%p==0:
        x3=None
        y3=None
        return [x3,y3]
    
    [l,v]=pendiente(P,Q,p)
    x3=l**2-x1-x2
    y3=-l*x3-v
    return [int(x3 % p), int(y3 % p)]
        

def pendiente(P,Q,p):
    [x1,y1]=P
    [x2,y2]=Q
    if x1==x2:
        l=(3*x1**2)*mod_inverse((2*y1),p)
        v=(-x1**3+2)*mod_inverse((2*y1), p)
            
        
    if x1!=x2:
        l=(y2-y1)*mod_inverse((x2-x1), p)
        v=(y1*x2-y2*x1)*mod_inverse((x2-x1), p)
        
    return [l,v]
        
def Weil(P,Q,S,p,N):
    Sm=[S[0],-S[1]%p]
    fpQS=Miller(P,suma(Q,S,p),p,N)
    fpS=Miller(P,S,p,N)
    fqPS=Miller(Q,suma(P,Sm,p),p,N)
    fqS=Miller(Q,Sm,p,N)

    ePQ=(fpQS*mod_inverse(fpS, p))*mod_inverse(fqPS*mod_inverse(fqS, p),p)
    return ePQ%p

P=[2,3]
P1=[2,3]
Q=[0,10]      
S=[5,4]
print(((Weil(P,Q,S,11,6))*Weil(P1,Q,S,11,6))%11)
print(Weil(P1,Q,S,11,6))
print(Weil(suma(P,P1,11),Q,S,11,6))
