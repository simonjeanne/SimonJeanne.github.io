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
w=13    #rotation imposée au pendule (wcrit = 10)

plt.title('Rotation : 13 rad/s')




#Équations d'évolution du système
def f1(x,y):
    return (y)
def f2(x,y):
    return(-g/L*np.sin(x)+w*w*np.sin(x)*np.cos(x))
    
#Résolution par Runge-Kutta
#Nombre de points et pas de temps
N=1000
Dt=0.005
#Variables
x1=[0]*N
x2=[0]*N

#Liste des points de départs
#startx1=[0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.14159]
#startx2=[0]
x2_crit = np.sqrt(4*g/L)
startx1=[-0.95*3.14159,-0.9*3.14159,-0.8*3.14159,-0.7*3.14159,-0.6*3.14159,-0.5*3.14159,-0.4*3.14159,-0.3*3.14159,-0.2*3.14159,-0.1*3.14159,-0.01*3.14159,0.01*3.14159,0.1*3.14159,0.2*3.14159,0.3*3.14159,0.4*3.14159,0.5*3.14159,0.6*3.14159,0.7*3.14159,0.8*3.14159,0.9*3.14159,0.95*3.14159]
startx2=[0]
for x1[0] in startx1:
    for x2[0] in startx2:     
        for i in range(N-1):
            k11=f1(x1[i],x2[i])*Dt
            k21=f2(x1[i],x2[i])*Dt
            k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k22=f2(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k23=f2(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k14=f1(x1[i]+k13,x2[i]+k23)*Dt
            k24=f2(x1[i]+k13,x2[i]+k23)*Dt
            #
            x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
            x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
            
        plt.plot(x1,x2, '-r')

        
startx1=[-3.14159]
startx2=[0.2*x2_crit,0.4*x2_crit,0.6*x2_crit,0.8*x2_crit,1*x2_crit]
for x1[0] in startx1:
    for x2[0] in startx2:     
        for i in range(N-1):
            k11=f1(x1[i],x2[i])*Dt
            k21=f2(x1[i],x2[i])*Dt
            k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k22=f2(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k23=f2(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k14=f1(x1[i]+k13,x2[i]+k23)*Dt
            k24=f2(x1[i]+k13,x2[i]+k23)*Dt
            #
            x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
            x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
            
        plt.plot(x1,x2, '-g')
startx1=[3.14159]
startx2=[-0.2*x2_crit,-0.4*x2_crit,-0.6*x2_crit,-0.8*x2_crit,-1*x2_crit]
for x1[0] in startx1:
    for x2[0] in startx2:     
        for i in range(N-1):
            k11=f1(x1[i],x2[i])*Dt
            k21=f2(x1[i],x2[i])*Dt
            k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k22=f2(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k23=f2(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k14=f1(x1[i]+k13,x2[i]+k23)*Dt
            k24=f2(x1[i]+k13,x2[i]+k23)*Dt
            #
            x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
            x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
            
        plt.plot(x1,x2, '-g')
        

startx1=[-1*3.14159,1*3.14159]
startx2=[0]
for x1[0] in startx1:
    for x2[0] in startx2:     
        for i in range(N-1):
            k11=f1(x1[i],x2[i])*Dt
            k21=f2(x1[i],x2[i])*Dt
            k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k22=f2(x1[i]+k11/2,x2[i]+k21/2)*Dt
            k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k23=f2(x1[i]+k12/2,x2[i]+k22/2)*Dt
            k14=f1(x1[i]+k13,x2[i]+k23)*Dt
            k24=f2(x1[i]+k13,x2[i]+k23)*Dt
            #
            x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
            x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
            
        plt.plot(x1,x2, '--b')
        




plt.axis([-3.14159, 3.14159,-50,50])
plt.xlabel('Theta')
plt.ylabel('Vitesse angulaire')   
   
plt.grid(True)
plt.show()