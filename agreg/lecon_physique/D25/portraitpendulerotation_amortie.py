# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:06:50 2019

@author: cleme
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import numpy as np

#Paramètres du système dynamique étudié
L=0.0981  #longeur du pendule
g=9.81   #gravité
w=12   #rotation imposée au pendule (wcrit = 10)
frottement=0.1  #frottement fluide
#plt.title('Rotation : 0 rad/s')

position_depart = 3.14159
vitesse_depart = 0



#Équations d'évolution du système
def f1(x,y):
    return (y)
def f2(x,y):
    return(-g/L*np.sin(x)+w*w*np.sin(x)*np.cos(x))
def f2a(x,y):
    return(-g/L*np.sin(x)+w*w*np.sin(x)*np.cos(x)-frottement*y)


   
#Résolution par Runge-Kutta
#Nombre de points et pas de temps
N=5000
Dt=0.01
#Variables
x1=[0]*N
x2=[0]*N
   
startx1=[position_depart]
startx2=[vitesse_depart]  
for x1[0] in startx1:
    for x2[0] in startx2:     
        for i in range(N-1):
            k11=f1(x1[i],x2[i])*Dt
            k21=f2a(x1[i],x2[i])*Dt
            k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k22=f2a(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k23=f2a(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k14=f1(x1[i]+k13,x2[i]+k23)*Dt
            k24=f2a(x1[i]+k13,x2[i]+k23)*Dt
            #
            x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
            x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
            
        plt.plot(x1,x2, color='black', linestyle='dashed')



#plt.axis([-3.14159, 3.14159,-50,50])
plt.xlabel('Theta')
plt.ylabel('Vitesse angulaire')   
   
plt.grid(True)
plt.show()