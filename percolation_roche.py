# Date : 14/07/2024 - 16/07/2024
# Balthazar RICHARD
# Analyses de percolations dans des reseaux carre aleatoires modélisant 
# l'écoulement d'eau dans une roche poreuse ou bien un percolateur de café.


import random
import matplotlib.pyplot as plt
import numpy as np


# Modélistation de la recherche de la composante connexe dans un resaux carre aleatoire de taille

def percolation(n, m, p, r=0) :

    # Modélisation du reseau
    grid = [list() for i in range(2*n+1)]
    q = 0
    for i in range(2*n+1) :
        grid[i] = [list() for j in range(2*m+1)]
        if i%2!=0 :
            grid[i][0].append([[0, 0], [n-i//2, n-i//2-1]])
            grid[i][0].append("darkseagreen")
        else :
            grid[i][0] = False 
        for j in range(1, 2*m+1) :
            q = random.randint(1,100)/100
            grid[i][j] = list()
            if (i%2==1 and j%2==1) or (i%2!=1 and j%2!=1) :
                grid[i][j] = False
            else :
                # Vertical
                if i%2==0 and j%2!=0 :
                    grid[i][j].append([[j//2, j//2+1], [n-i//2, n-i//2]])
                # Horizontal
                elif i%2!=0 and j%2==0 :
                    grid[i][j].append([[j//2, j//2], [n-i//2, n-i//2-1]])
                if q<p or p==1  :
                    grid[i][j].append("darkseagreen")
                else :
                    grid[i][j].append("white")

    plt.plot([0, 0, m, m, m, m, 0], [n, n, n, n, 0, 0, 0], 'gainsboro') # Cadre du réseau

    for i in range(2*n+1) :
        for j in range(2*m+1) :
            if grid[i][j] != False :
                if grid[i][j][1] != "white" :
                    plt.plot(grid[i][j][0][0], grid[i][j][0][1], color=grid[i][j][1])
    
    # Calcul de la composante connexe 
    # Initialisation :
    for i in range(2*n+1) :
        if i%2!=0 :
            if grid[i][0][1]=="darkseagreen" :
                grid[i][0][1] = 'Orange'
                
    stack = list()
    visited = [[False for j in range(2*m+1)] for i in range(2*n+1)]
    stack.append([1, 0])
    while stack != [] :
        ind = stack.pop()
        i = ind[0]
        j = ind[1]
        if visited[i][j] == False :
            if grid[i][j][1] == "darkseagreen" :
                grid[i][j][1] = "Orange"
            # Vertical
            if i%2!=0 and j%2==0 :
                if i-1>=0 and j-1>=0 and grid[i-1][j-1][1]!='white' :
                    stack.append([i-1, j-1])
                if i-2>=0 and grid[i-2][j][1]!='white' :
                    stack.append([i-2, j])
                if i-1>=0 and j+1<2*m+1 and grid[i-1][j+1][1]!='white' :
                    stack.append([i-1, j+1])
                if i+1<2*n+1 and j+1<2*m+1 and grid[i+1][j+1][1]!='white' :
                    stack.append([i+1, j+1])
                if i+2<2*n+1 and grid[i+2][j][1]!='white' :
                    stack.append([i+2, j])
                if i+1<2*n+1 and j-1>=0 and grid[i+1][j-1][1]!='white' :
                    stack.append([i+1, j-1])
            # Horizontal
            elif i%2==0 and j%2!=0 :  
                if j-2>=0 and grid[i][j-2][1]!='white' :
                    stack.append([i, j-2])
                if i-1>=0 and j-1>=0 and grid[i-1][j-1][1]!='white' :
                    stack.append([i-1, j-1])
                if i-1>=0 and j+1<2*m+1 and grid[i-1][j+1][1]!='white' :
                    stack.append([i-1, j+1])
                if i+1<2*n+1 and j-1>=0 and grid[i+1][j-1][1]!='white' :
                    stack.append([i+1, j-1])
                if i+1<2*n+1 and j+1<2*m+1 and grid[i+1][j+1][1]!='white' :
                    stack.append([i+1, j+1])
                if j+2<2*m+1 and grid[i][j+2][1]!='white' :
                    stack.append([i, j+2])
        visited[i][j] = True

    # Donnée de l'atteinte du bord droit par la composante connexe
    goal = False 
    for i in range(2*n+1) :
        if grid[i][2*m] != False :
            if grid[i][2*m][1] == "Orange" :
                goal = True
                
    # Calcul de la profondeure de la composante connexe
    depht = 0
    for j in range(2*m+1) :
    	for i in range(2*n+1) :
            if grid[i][j] != False :
 	            if grid[i][j][1] == "Orange" :
	                depht = j//2
                
    # Affichages
    print("Probabilité d'ouverture d'un lien p =", p)
    print("Profondeur de la composante connexe ouverte :", depht, "\n\n")
    title = "Probabilité d'ouverture d'un lien p = " + str(p)
    plt.axis(False)
    plt.title(title)
    nom = 'percolation_eau_'+str(r)+'.svg'
    plt.savefig(nom)

    plt.pause(0.1)
    for j in range(2*m+1) :
        for i in range(2*n+1) :
            if grid[i][j] != False :
                if grid[i][j][1] == "Orange" :
                    plt.plot(grid[i][j][0][0], grid[i][j][0][1], 'Orange')

    plt.draw()
    plt.pause(1)
    
    nom2 = 'percolation_eau_0'+str(r)+'.svg'
    plt.savefig(nom2)
    
    plt.clf()
    return goal
    
    

percolation(50, 100, 0.229)
for i in range(3) :
    percolation(60, 100, 0.47, i+1)
for i in range(3) :
    percolation(50, 100, 0.53, i+4)
percolation(50, 100, 0.829, i+6)
