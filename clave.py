# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 00:14:39 2021

@author: ana_p
"""

import random
from math import log
from suma import suma, mSuma, punts
from AparellamentWeil import Weil

#Treballam amb la corba y^2=x^3+1
#Amb n=6, q=2, r=3, l=2


pt=[]
#Funció que retorna si un punt P compleix que [N]P=O i [k]P!=O per k<N.
def puntValid(P,p,N):
    if mSuma(P,p,N)==[None,None]:
        for j in range(1,N):
            if mSuma(P,p,j)!=[None,None]:
                pt.append(P)
    if len(pt)==(N-1):
        return pt
    else:
        return None
    
    
ptv=[]
#funció que retorna quins punts de p ens serveixen per un cert N.
def puntsValids(p,N):
    P=punts(p)
    for i in range(p):
        if puntValid(P[i], p, N)!=None:
            ptv.append(P[i])
    return ptv


#Funció que retorna els punts P i Q arbitraris.
def puntsBGN(p,N,r):
    P=random.choice(puntsValids(p, N))
    Q1=random.choice(punts(p))
    Q=mSuma(Q1,p,r)
    S=random.choice(punts(p))
    return [P,Q,S]


#Funció que retorna les claus, tant la pública (pk) com la privada (q). 
def Gen(q,r,p,N):
    [P,Q,S]=puntsBGN(p, N,r)
    pk=Weil(P,Q,S,p,N)
    return [pk,q]


#Funció que retorna l'encriptació.
def Enc(m,N,p,q,r):
    [P,Q]=Gen(q,r,p,N)
    I=list(range(1,N+1))
    t=random.choice(I)
    C=suma(mSuma(P,p,m), mSuma(Q,p,t), p)
    return C

mp=[]
#Funció que retorna la desencriptació.
def Dec(N,q,r,p,m):
    C=Enc(m, N, p, q, r)
    [P,Q]=puntsBGN(p,N,r)
    Pm=mSuma(P,q,N)
    Cm=mSuma(C,q,N)
    mp.append(log(Cm[0],Pm[0]))
    mp.append(log(Cm[1],Pm[1]))
    return mp

