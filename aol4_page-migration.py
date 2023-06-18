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


def int_to_bin(x):
    x = bin(x)[2:]
    l = len(x)
    x = str(0) * (6 - l) + x
    return x

def bin2_to_quat(x):
    if x=='00':
        q='0'
    elif x=='01':
        q='1'
    elif x=='10':
        q='2'
    elif x=='11':
        q='3'
    return q

def int_to_quat(x): # works only for 0 to 63
    q=''
    x=int_to_bin(x)
    q+=bin2_to_quat(x[:2])
    q+=bin2_to_quat(x[2:4])
    q+=bin2_to_quat(x[4:6])
    return q

def distance(x,y,structure):
    if structure=='hypercube':
        if len(x)!=6 or len(y)!=6:
            return 'wrong size of binary number (not 6)'
        d=0
        for k in range(0,6):
            if x[k]!=y[k]:
                d+=1
        return d
    if structure=='torus':
        if len(x)!=3 or len(y)!=3:
            return 'wrong size of quaternary number (not 3)'
        d=0
        for k in range(0,3):
            tmp=abs(int(x[k])-int(y[k]))
            if tmp==3:
                tmp=1
            d+=tmp
        return d
    else:
        return 'unknown structure'

def flip(page_place,asks,D,structure):
    cost=0
    p=1/(2*D)
    for i in range(0,len(asks)):
        cost+=distance(page_place,asks[i],structure)
        if random.random() < p:
            cost += D*distance(page_place,asks[i],structure)
            page_place = asks[i]
    return cost

def find_optimum(phase,structure):
    if structure=='hypercube':
        position_best=int_to_bin(0)
    elif structure=='torus':
        position_best=int_to_quat(0)
    cost_best=127023892
    for pos in range(0,64):
        if structure=='hypercube':
            position=int_to_bin(pos)
        elif structure=='torus':
            position=int_to_quat(pos)
        cost=0
        for j in range(0,len(phase)):
            cost+=distance(position,phase[j],structure)
        if cost < cost_best:
            cost_best = cost
            position_best = position
    return position_best

def move_to_min(page_place,asks,D,structure):
    cost=0
    phase=[]
    for i in range(0,len(asks)):
        cost+=distance(page_place,asks[i],structure)
        phase.append(asks[i])
        if len(phase)==D:
            new_position=find_optimum(phase,structure)
            phase=[]
            cost+=D*distance(page_place,new_position,structure)
            page_place=new_position
    return cost



structure='h' # 'hypercube' or 'torus'
distribution='j'

if structure=='t':
    structure='torus'
elif structure=='h':
    structure='hypercube'
D=32
nodes=[]
asks=[]
if structure=='hypercube':
    for i in range(0,64):
        nodes.append(int_to_bin(i))
    page_place=int_to_bin(random_number('j',64)-1)
    for i in range(0,1024):
        asks.append(int_to_bin(random_number(distribution,64)-1))
elif structure=='torus':
    for i in range(0,64):
        nodes.append(int_to_quat(i))
    page_place=int_to_quat(random_number('j',64)-1)
    for i in range(0,1024):
        asks.append(int_to_quat(random_number(distribution,64)-1))


print(flip(page_place, asks, D, structure))
print(move_to_min(page_place, asks, D, structure))

