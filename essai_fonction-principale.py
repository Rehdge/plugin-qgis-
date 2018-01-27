# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:07:59 2018

@author: regis
"""
""" import des bibliothèques csv et numpy utiles dans l'algorithme"""
import csv

import numpy as np

"""On ouvre dans un premier temps le fichier csv afin de le lire 
permettant ainsi de remplir un tableau 
composé des données contenues dans le fichier csv"""

Tableau = []
f = open("donnees_test_text.txt")
csv_f = csv.reader(f)
for row in csv_f:
    Tableau.append(row)
#print(Tableau)
    
"""Le tableau est divisé en trois parties : 
deux listes comprenant l'une les noms des points l'autre les années 
et une matrice comprenant les coordonnées et leurs entêtes ('X' et 'Y')"""

Annees = Tableau[0]
#print(Annees)
Points = []
for i in range(len(Tableau)):
    Points.append(Tableau[i][0])
#print (Points)
Coordonnees = []
for ligne in Tableau:
    del ligne[0]
del Tableau[0]
Coordonnees = Tableau
#print(Coordonnees)


"""Création d'un tableau à trois entrées : P (matrice de matrices).
 P contiendra autant de matrices que de points 
 et autant de listes dans chaque matrice que d'années. 
 Une liste type est organisée de la manière suivante : 
 [Année,Point,'X',Coordonnée_X,'Y',Coordonnée_Y]. 
 P permet de reclasser le tableau de manière claire"""
 
 
P = [[[0 for j in range(6)]for i in range(len(Annees)/2)]for k in range(len(Points)-2)]

"""Ajout des années et des noms de points dans P"""

for k in range(len(Points)-2):
    for i in range(len(Annees)/2):
        P[k][i][0] = Annees[i*2]
for k in range(len(Points)-2):
    for i in range(len(Annees)/2):
        P[k][i][1] = Points[k+2]

""" Division de la matrice Coordonnees en deux : 
une liste comprenant les entêtes ('X' et 'Y') 
et une matrice ne comprenant que les valeurs des coordonnées"""

entetes =[]
for i in range(len(Coordonnees[0])):
    entetes.append(Coordonnees[0][i])
#print(entetes)

del Tableau[0]
valeurs = Tableau
#print(valeurs)
N = np.transpose(valeurs)
#print(N)

"""Ajout des entêtes 'X' et 'Y' ainsi que les coordonnées dans P"""

for k in range((len(Points)-2)):
    for i in range(len(Annees)/2):
        P[k][i][2] = 'X'
        P[k][i][4] = 'Y'


for k in range(len(Points)-2):
    for i in range(len(Annees)/2):
        P[k][i][3] = N[i*2][k] 
        P[k][i][5] = N[i*2+1][k]
#print(P)

"""Translation des coordonnées 
contenues dans une matrice, dans une seule liste : Calc. 
Cela est nécessaire pour effectuer le calcul de distances"""

Calc = []
for i in range(len(valeurs)):
    for j in range(len(valeurs[0])):
            Calc.append(valeurs[i][j])
            
"""Passages d'objets de types string à des flottants dans la liste Calc_float"""
            
Calc_float = []
for item in Calc:
    Calc_float.append(float(item))
#print(Calc_float)

"""Calcul des distances dans la liste Calc_float"""    

#print(len(Calc_float))
for i in range(len(Calc_float)/2-1):
    Calc_float[i]=np.sqrt((Calc_float[2*i+2]-Calc_float[2*i])**2+(Calc_float[2*i+3]-Calc_float[2*i+1])**2)
#print(Calc_float)

""" Translation des valeurs calculées dans une liste : Distances"""

Distances = []
for i in range(len(Calc_float)/2-1):
    Distances.append(Calc_float[i])
#print(Distances)

"""Suppression dans la liste des valeurs abérantes : ces valeurs correspondent au calcul dans la liste 
à une fausse distance sur la dernière année et 
la première année entre deux points : 
faute d'avoir les valeurs dans une seule liste
(ici le seuil est fixé à 20 en comparaison 
des valeurs fictives entrées en coordonnées, 
le seuil devrait être beaucoup plus faible avec des valeurs réelles)"""

#print(len(Annees)/2)
for elemt in Distances:
    if elemt >20:
        Distances.remove(elemt)
#print(Distances)

"""Création de la matrice D finale ; 
tableau à trois entrée avec le même principe que la matrice P. 
Une liste type de la matrice D est la suivante : 
[Année_début_de_déplacement, Année_fin_de_déplacement,
nom_point,déplacement_correspondant]"""    

D = [[[0 for j in range(4)]for i in range(len(Annees)/2-1)]for k in range(len(Points)-2)]
#print(D)
for k in range(len(Points)-2):
    for i in range(len(Annees)/2-1):
        D[k][i][2] = Points[k+2]

for k in range(len(Points)-2):
    for i in range(len(Annees)/2-1):
        D[k][i][0] = Annees[i*2]
        D[k][i][1] = Annees[i*2+2]
              
for k in range(len(Points)-2):
    for i in range(len(Annees)/2-1):
            D[k][i][3] = Distances[i+k*3]
        
print(D)


