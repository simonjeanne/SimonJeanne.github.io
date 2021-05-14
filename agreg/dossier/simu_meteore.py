# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import numpy as np





#|||||||||PARAMETRES|||||||||
#|||||||||PARAMETRES|||||||||
#|||||||||PARAMETRES|||||||||
#Paramètres principaux du système dynamique étudié
A=2/3600/0.01               #parametre A=cdF/rho/taille_caracteristique. cdF entre 1.2 et 2.5
Q=100*1000000              #Enthalpie massique de destruction, comprise entre 20 et 700 MJ/kg (majorité autour de 80-100 MJ/kg)
vitesse_depart = 13000     #vitesse initiale, entre 11 et 72 km/s
R=0.5*vitesse_depart*vitesse_depart/Q  #Ratio énergie cinetique initiale sur énergie nécessaire à la destruction du bolide

#paramètres secondaires
gamma=45*3.14159/180           #angle d'entrée dans l'atmosphère
mu=2/3                         #facteur de changement de forme
altitude_depart = 110000       #sommet de l'atmosphère

#paramètre de l'atmosphère
rho_0=1.29   #densité au niveau du sol
h0=7160      #hauteur d'échelle 
    # Rq : valeurs par défaut pour la Terre rho_0=1.29 et h0=7160

#Nombre de points et pas de temps
N=6000
Dt=0.01
#|||||||||PARAMETRES|||||||||
#|||||||||PARAMETRES|||||||||
#|||||||||PARAMETRES|||||||||






#|||||||||EQUATIONS|||||||||
#|||||||||EQUATIONS|||||||||
#|||||||||EQUATIONS|||||||||
def rho_atm(x):                     #densité de l'air en fonction de l'altitude
    return(rho_0*np.exp(-x/h0))     
def f1(x,y):                        #dh/dt
    return(-np.sin(gamma)*y)
def f2(x,y,A_,R_,v0):               #dv/dt
    return(-0.5*A*rho_atm(x)*y*y*np.exp(R*(1-(y/v0)*(y/v0))))
def masse(v,v0,R_,mu_):             #masse (normalisée) en fonction de la vitesse
    return(np.exp(-R_/(1-mu)*(1-(v/v0)*(v/v0))))
#|||||||||EQUATIONS|||||||||
#|||||||||EQUATIONS|||||||||
#|||||||||EQUATIONS|||||||||    




#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||
#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||
#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||
#Variables
x1=[0]*N
x2=[0]*N
x3=[0]*N
x1[0]=altitude_depart
x2[0]=vitesse_depart
x3[0]=1  
#integration 
for i in range(N-1):
    k11=f1(x1[i],x2[i])*Dt
    k21=f2(x1[i],x2[i],A,R,x2[0])*Dt
    k12=f1(x1[i]+k11/2,x2[i]+k21/2)*Dt
    k22=f2(x1[i]+k11/2,x2[i]+k21/2,A,R,x2[0])*Dt
    k13=f1(x1[i]+k12/2,x2[i]+k22/2)*Dt
    k23=f2(x1[i]+k12/2,x2[i]+k22/2,A,R,x2[0])*Dt
    k14=f1(x1[i]+k13,x2[i]+k23)*Dt
    k24=f2(x1[i]+k13,x2[i]+k23,A,R,x2[0])*Dt

    x1[i+1]=x1[i]+(k11+2*k12+2*k13+k14)/6
    x2[i+1]=x2[i]+(k21+2*k22+2*k23+k24)/6
    x3[i+1]=masse(x2[i+1],x2[0],R,mu)
#renormalisation
for i in range(N-1):
    x2[i+1]=x2[i+1]/x2[0]
    x1[i+1]=x1[i+1]/1000
x2[0]=1
x1[0]=altitude_depart/1000
plt.plot(x1,x2, label='Vitesse')
plt.plot(x1,x3, linestyle='dashed', label='Masse')                
#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||
#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||
#|||||||||INTEGRATEUR RUNGE-KUTTA|||||||||




#|||||||||AFFICHAGE|||||||||
#|||||||||AFFICHAGE|||||||||
#|||||||||AFFICHAGE|||||||||
plt.axis([0, 100,0,1.1])
plt.xlabel('Altitude [km]')
plt.ylabel('Vitesse et Masse normalisées')   
plt.legend()
plt.grid(True)
plt.show()
#|||||||||AFFICHAGE|||||||||
#|||||||||AFFICHAGE|||||||||
#|||||||||AFFICHAGE|||||||||