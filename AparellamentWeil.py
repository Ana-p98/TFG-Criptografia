# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:17:02 2021

@author: ana_p
"""

from suma import suma, pendiente, mSuma, punts, inv

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
    lam=lamda(P,Q,p)
    if P==[None,None]:
            [xP,yP]=[0,0]
    if Q==[None,None]:
            [xQ,yQ]=[0,0]
    [l,v]=pendiente(P, Q, p)
    if lam == True:
        if (x+xP+xQ-l**2)%p==0:
            hPQ=0
        else:
            hPQ=(y-yP-l*(x-xP))*inv(x+xP+xQ-l**2,p)
    else:
        hPQ=(x-xP)
    return hPQ



#Funció que retorna lambda, que és el pendent de la recta que uneix P i Q, en funció de si P=Q, P!=Q o si és vertical. 
def lamda(P,Q,p):
    [xP,yP]=P
    [xQ,yQ]=Q
    #Si P=Q, llavors:
    if xP==xQ and yP==yQ: 
        #pendiente de la recta tengente
        lam=True
    else:
        #Si alguna de les dues components són iguals, llavors:
        if xP==xQ or yP==yQ:
            lam=False
        #sino:
        else:
            lam=True    
    return lam


#Funció que retorna l'aparellament de Weil
def Weil(P,Q,S,p,N):
    Sm=[S[0],-S[1]%p]
    fpQS=Miller(P,suma(Q,S,p),p,N)
    fpS=Miller(P,S,p,N)
    fqPS=Miller(Q,suma(P,Sm,p),p,N)
    fqS=Miller(Q,Sm,p,N)
    if fpS%p==0 or fqS%p==0 or (fqPS*inv(fqS, p))%p==0:
        ePQ=0
    else:
        ePQ=(fpQS*inv(fpS, p))*inv(fqPS*inv(fqS, p),p)
    return ePQ%p


print(Weil([0,1],[2,8],[5,7],11,3))
print((Weil([0,1],[2,8],[5,7],11,3)*Weil([0,1],[2,8],[5,7],11,3))%11)
print(Weil(suma([0,1],[0,1],11), [2,8], [5,7], 11, 3))

