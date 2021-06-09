# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 1, 100)

Aa=1
ka=2


def ordrezero(A,k,t):
    return(A-k*t)
    
def ordreun(A,k,t):
    return(A*np.exp(-k*t))
    
def ordredeux(A,k,t):
    return(A/(1+A*k*t))


plt.plot(x, ordrezero(Aa,ka,x), label='Ordre 0, k=2')
plt.plot(x, ordreun(Aa,ka,x), label='Ordre 1, k=2')
plt.plot(x, ordredeux(Aa,ka,x), label='Ordre 2, k=2')


plt.xlabel('t')
plt.ylabel('[A](t)')
plt.axis([0, 1,0,1])

plt.title('[A](t) pour des lois differentes')

plt.legend()

#plt.savefig('difficiledejuger')
plt.show()

