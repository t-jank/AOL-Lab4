# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:51:53 2023

@author: t-jan
"""
import random


def Harmonic_Number(n):
   # return 0.5772156649 + math.log(n) + 1/(2*n)
    Hn=0
    for i in range(1,n+1):
        Hn+=1/i
    return Hn

def Harmonic_Number_2(n):
    Hn2=0
    for i in range(1,n+1):
        Hn2+=1/i**2
    return Hn2

def random_number(rozklad,n): # <1,n>
    prawdopodobienstwa=[]
    przedzialy=[]
    if rozklad=='jednostajny' or rozklad=='j':
        for i in range(0,n):
            prawdopodobienstwa.append(1/n)
    elif rozklad=='harmoniczny' or rozklad=='h':
        Hn=Harmonic_Number(n)
        for i in range(1,n+1):
            prawdopodobienstwa.append(1/(i*Hn))
    elif rozklad=='dwuharmoniczny' or rozklad=='d' or rozklad=='dh':
        Hn2=Harmonic_Number_2(n)
        for i in range(1,n+1):
            prawdopodobienstwa.append(1/(i**2*Hn2))
    elif rozklad=='geometryczny' or rozklad=='g':
        for i in range(1,n):
            prawdopodobienstwa.append(1/2**i)
        prawdopodobienstwa.append(1/2**(n-1))
    else: return 'nieznany rozklad'
    przedzialy.append(0)
    for i in range(1,len(prawdopodobienstwa)+1):
        przedzialy.append(przedzialy[i-1]+prawdopodobienstwa[i-1])
    przedzialy.append(1)
    X=random.random()
    for i in range(0,len(przedzialy)):
        if X>=przedzialy[i] and X<przedzialy[i+1]:
            return i+1


######## HIPERKOSTKA 6 ########

def distance_hypercube(x,y):
    if len(x)!=6 or len(y)!=6:
        return 'wrong size of binary number (not 6)'
    d=0
    for i in range(0,6):
        if x[i]!=y[i]:
            d+=1
    return d

def find_optimum(phase):
    position_best=int_to_bin(0)
    cost_best=127023892
    for pos in range(0,64):
        position=int_to_bin(pos)
        cost=0
        for i in range(0,len(phase)):
            cost+=distance_hypercube(position,phase[i])
        if cost < cost_best:
            cost_best = cost
            position_best = position
    return position_best

def move_to_min_hypercube(page_place,asks,D):
    return 15

def flip_hypercube(page_place,asks,D):
    cost=0
    p=1/(2*D)
    for i in range(0,len(asks)):
        cost+=distance_hypercube(page_place,asks[i])
        if random.random() < p:
            cost += D*distance_hypercube(page_place,asks[i])
            page_place = asks[i]
    return cost

def int_to_bin(x):
    x = bin(x)[2:]
    l = len(x)
    x = str(0) * (6 - l) + x
    return x

nodes=[]
for i in range(0,64):
    nodes.append(int_to_bin(i))
D=32
page_place=int_to_bin(random_number('j',64)-1)
distribution='j'
asks=[]
for i in range(0,1024):
    asks.append(int_to_bin(random_number(distribution,64)-1))

print(flip_hypercube(page_place,asks,D))

