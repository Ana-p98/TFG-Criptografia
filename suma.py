# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:03:15 2021

@author: ana_p
"""

###Suma de dos punts de la corba el·líptica y^2=x^3+1

#Sigui P=(x_1,y_1) i Q=(x_2,y_2), llavors la seva suma la podem definir com:
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
    if P==[None,None]:
            [x1,y1]=[0,0]
    if Q==[None,None]:
            [x2,y2]=[0,0]
    if x1==x2:
        l=(3*x1**2)*inv((2*y1),p)
        v=(-x1**3+2)*inv((2*y1), p)
    if x1!=x2:
        l=(y2-y1)*inv((x2-x1), p)
        v=(y1*x2-y2*x1)*inv((x2-x1), p)
        
    return [l%p,v]

#punts per a la corba y^2=x^3+1

puntX=[]
puntY=[]
punt=[]
def punts(p):
    for i in range(p):
        a=(i**3+1)%p
        for j in range(p):
            b=(j**2)%p
            if a == b:
                puntX.append(i)
                puntY.append(j)  
    
    for i in range(len(puntX)):
        punt.append([puntX[i],puntY[i]])
    punt.append([None,None])

    return punt

# print(punts(11))
# p=11
# for i in range(p+1):
#     punto=punts(p)
#     for j in range(p+1):
#         print(punto[i],'+',punto[j],'=',suma(punto[i],punto[j],p))
#         #Amb això comprovam si tots els punts resultants de la suma pertanyen a la nostra corba el·líptica.
#         # if suma(punto[i], punto[j], p)!=[None,None]:
#         #     sumas=suma(punto[i],punto[j],p)
#         #     print(((sumas[0])**3+1)%p==(sumas[1]**2)%p)
        

#Funció que retorna [m]P, és a dir la suma de P m vegades.
def mSuma(P,p,m):
    s=P
    for i in range(m-1):
        s=suma(s,P,p)
    return s

#Funció que retorna l'invers d'un nombre mòdul p.
def inv(a,p):
    for i in range(p+1):
        if (a*i)%p==1:
            return i
        if a==0:
            return 0
    
