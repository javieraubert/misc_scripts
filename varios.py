# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:57:05 2017

@author: Javier Aubert
"""
def busqueda_lineal(A,X):
    j=0
    n=len(A)
    while (j<n)and(X!=A[j]):
        j+=1
    if j<n:
        return j
    else:
        return 0

def SIFTUP (H,i):
    import math
    import numpy as np
    pos = (busqueda_lineal(H,i))
    iop = pos + 1
    irl = iop-1
    ivader = iop//2
    ivaderrl = ivader - 1
    fin = 0
    while fin == 0:
        if H[ivaderrl] > H[irl]:
            fin = 1
            return 1
        else :
            temp = H[ivaderrl]
            H[ivaderrl]=H[irl]
            H[irl]=temp
            fin = 1
            return 0 
    return fin

def INSERT (H,N):
    H=H.append(N)
    Tot= len(H)
    fin = 0
    k=1
    j=H[Tot-1]
    pos = Tot-1
    iop = pos + 1
    irl = iop-1
    ivader = iop//2
    ivaderrl = ivader - 1
    while fin==0:
        SIFTUP(H,j)
        
        
        
        
        
        
        