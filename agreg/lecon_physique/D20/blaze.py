# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#Nom du programme : DiffractionNFentes

#Auteurs : Arnaud Raoux, Emmanuel Baudin, FranÃ§ois LÃ©vrier et la prÃ©pa agreg de Montrouge
#Adresse : Departement de physique de l'Ecole Normale Superieure
#		24 rue Lhomond
#		75005 Paris
#Contact : arnaud.raoux@ens.fr
#
#AnnÃ©e de crÃ©ation : 2016 
#Version : 1.10

#Liste des modifications
#v 1.00 : 2016-03-01 PremiÃ¨re version complÃ¨te
#v 1.10 : 2016-05-02 Mise Ã  jour de la mise en page

#Version de Python
#3.4

#LICENCE
#Cette oeuvre, crÃ©ation, site ou texte est sous licence Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International. Pour accÃ©der Ã  une copie de cette licence, merci de vous rendre Ã  l'adresse suivante http://creativecommons.org/licenses/by-nc/4.0/ ou envoyez un courrier Ã  Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

#AVERTISSEMENT
#Pour un affichage optimal, il est recommandÃ© de mettre la fenÃªtre en plein Ã©cran.

#Description : 
#Ce programme reprÃ©sente la figure d'interfÃ©rence obtenue lorsqu'une onde plane monochromatique de longueur d'onde lambda traverse un dispositif de N fentes rÃ©guliÃ¨rement espacÃ©es d'une distance a (centre-centre) et de largeur b chacunes. L'Ã©cran est positionnÃ© Ã  une distance D des fentes. 
# Le rÃ©sultat prÃ©sentÃ© est l'intensitÃ© lumineuse normalisÃ©e en fonction de la position rÃ©duite sur l'Ã©cran pour permettre une comparaison des diffÃ©rentes situations.
#Les paramÃ¨tres peuvent Ãªtre variÃ©s indÃ©pendamment pour observer leur effet sur la figure d'interfÃ©rence. Il est aussi possible de tracer l'enveloppe de diffraction correspondant Ã  la diffraction par une fente de largeur w seule. 

#Code inspiré des auteurs précédents, Corentin Naveau y a apport

#import des bibliothÃ¨ques python
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import matplotlib
matplotlib.rc('xtick', labelsize=24) 
matplotlib.rc('ytick', labelsize=24) 
matplotlib.rcParams.update({'font.size': 20})

# =============================================================================
# --- Defaults values ---------------------------------------------------------
# =============================================================================

N0 = 2  # Nombre de fentes
a0 = 2  # Pas du reseau (distance entre fentes en Âµm)
b0 = 1  # taille d'une fente (en Âµm)
lamb0 = 0.633  # Longueur d'onde dans le vide (en Âµm)
blaze0 = 0
theta = np.arange(-np.pi/2, np.pi/2, 0.001)
stheta = np.sin(theta)
st0 = np.sin(theta-blaze0)

# =============================================================================
# --- Utility functions -------------------------------------------------------
# =============================================================================

def st(blaze):
    
    return (np.sin(theta-blaze))

def forme(blaze, b, lamb):
    """
    Calcule le facteur de forme du reseau.
    """
    return (np.sinc(np.pi/lamb*b*st(blaze)))**2

def structure(blaze, lamb, a, N):
    """
    Calcule le facteur de structure du reseau.
    """
    return (np.sin(N*np.pi*a*st0/lamb) /
            (N*np.sin(np.pi*a*st0/lamb)))**2


def signal(blaze, b, lamb, a, N):
    """
    Le signal est le produit du facteur de forme et du facteur de structure.
    """
    return forme(blaze, b, lamb)*structure(blaze, lamb, a, N)

# =============================================================================
# --- Creation de la figure ---------------------------------------------------
# =============================================================================

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.38, bottom=0.35)

# Creation de l'axe des abscisses, ici sin(theta) oÃ¹ theta est l'angle de sortie du faisceau. sin(theta)=x/D

abscisses = np.arange(-2.0, 2.0, 0.001)

#La ligne qui quit indique l'Ã©quation utilisÃ© pour obtenir la courbe.
# plt.text(0, 1.2, r'$\frac{I}{I_0} = \mathrm{sinc}^2\left(\frac{\pi bx}{\lambda_0D}\right)\times\frac{\sin^2(N\pi a x/\lambda_0D)}{N^2\sin^2(\pi ax/\lambda_0D)}$',        horizontalalignment='center', fontsize='22')

#Commentaires utiles affichÃ©s
#plt.text(-3.9, 1., r'$a$ pas du reseau')
#plt.text(-3.9, 0.9, r"$\lambda_0$ longueur d'onde")
#plt.text(-3.9, 0.8, r'$\epsilon$ Taille de la fente')
#plt.text(-3.9, 0.7, r'$N$ Nombre de fentes')
#plt.text(-3.9, 0.6, r"$D$ Distance Ã  l'écran (1 m)")

#Titre de la figure
plt.title('Figure de diffraction par N fentes')

#Nom des axes
plt.xlabel(r"sin($\theta$)")
plt.ylabel('Intensite lumineuse normalisee')


# Limites des axes (xmin,xmax,ymin,ymax)
plt.axis([-1, 1, -0.1, 1.4])

# Creation de la trace de la fonction s en fonction de abscisses.
# C'est un objet qui est sauvegarde dans 'l'
PLOTS = {}
PLOTS['Fonction'] = plt.plot(stheta, signal(blaze0, b0, lamb0, a0, N0),
                             lw=2, color='red')[0]
PLOTS['Facteur de forme'] = plt.plot(stheta, forme(blaze0, b0, lamb0), lw=1.5,
                                     ls='--', color='blue', visible=False)[0]
PLOTS['Facteur de structure'] = plt.plot(stheta,
                                         structure(blaze0, lamb0, a0, N0),
                                         lw=1.5, ls='--', color='green',
                                         visible=False)[0]


# Positionnement des barres de modification
axcolor = 'lightgoldenrodyellow'  # Choix de la couleur
ax_N = plt.axes([0.3, 0.015, 0.6, 0.03], facecolor=axcolor)
ax_a = plt.axes([0.3, 0.055, 0.6, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.3, 0.095, 0.6, 0.03], facecolor=axcolor)
ax_lamb = plt.axes([0.3, 0.135, 0.6, 0.03], facecolor=axcolor)
ax_blaze = plt.axes([0.3, 0.175, 0.6, 0.03], facecolor=axcolor)

# Noter les valeurs initiales
s_N = Slider(ax_N, 'N', 2, 30.0, valinit=N0)
s_a = Slider(ax_a, 'a (µm)', 0.1, 10.0, valinit=a0)
s_b = Slider(ax_b, 'b (µm)', 0.1, 2.0, valinit=b0)
s_lamb = Slider(ax_lamb, r"$\lambda_0$ (µm)", 0.4, 0.8, valinit=lamb0)
s_blaze = Slider(ax_blaze, 'angle blaze (rad)', -np.pi/6, np.pi/6, valinit=blaze0)


def update(val):
    """
    Met a jour le graph a partir des valeurs des sliders.
    """
    N = s_N.val  # On recupere la valeur de la barre s_N
    a = s_a.val  # On recupere la valeur de la barre s_a
    b = s_b.val  # On recupere la valeur de la barre s_b
    lamb = s_lamb.val  # On recupere la valeur de la barre s_lamb
    blaze = s_blaze.val  # On recupere la valeur de la barre s_lamb

    f = forme(blaze, b, lamb)
    s = structure(blaze, lamb, a, N)

    PLOTS['Fonction'].set_ydata(f*s)  # On met a jour le signal
    PLOTS['Facteur de forme'].set_ydata(f)  # On met a jour la forme
    PLOTS['Facteur de structure'].set_ydata(s)  # On met a jour la structure

    if (N-int(N) != 0):
        s_N.set_val(int(s_N.val))

    # On provoque la mise a jour du graphique (pas automatique par defaut)
    fig.canvas.draw_idle()

# Chaque fois qu'un slider est modifie, on appelle la fonction update
for s in (s_N, s_a, s_b, s_lamb, s_blaze):
    s.on_changed(update)


# Creation du bouton de "reset"
resetax = plt.axes([0.05, 0.06, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


# Definition de la fonction de "reset" (valeurs par defaut)
def reset(event):
    """
    On rend leurs valeurs initiales a tous les sliders.
    """
    for s in (s_N, s_a, s_b, s_lamb, s_blaze):
        s.reset()

# Lorsqu'on clique sur "reset", on appelle la fonction reset
button.on_clicked(reset)

# Creation du menu de selection des traces a afficher
cax = plt.axes([0.01, 0.3, 0.28, 0.20], facecolor=axcolor)
check = CheckButtons(cax,
                     ('Fonction', 'Facteur de forme', 'Facteur de structure'),
                     (True, False, False))


# Definition de la fonction qui passe un affichage de visible a invisible
def chooseplot(label):
    """
    Choose which plot to diplay.
    """
    graph = PLOTS[label]
    graph.set_visible(not graph.get_visible())
    fig.canvas.draw_idle()  # On provoque la mise a jour du graphique

# Lorsqu'on coche un de ces boutons, on appelle la fonction chooseplot
check.on_clicked(chooseplot)

mng = plt.get_current_fig_manager()     #Plein ecran
#mng.window.showMaximized()
plt.show()