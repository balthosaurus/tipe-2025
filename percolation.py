# Date : 16/07/2024 - 
# Balthazar RICHARD
# Algorithme modélisant une percolation de site


import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import GifImagePlugin


# Fonction qui crée un tableau de n couleurs distinctes et ni noir, ni blanche

def colors_tab(n) :
    colors = list()
    for i in range(n) :
        r = 0
        g = 0
        b = 0
        while (r,g,b) == (0,0,0) or (r,g,b) == (255,255,255) or (r,g,b) == (203,51,255) or (r,g,b) in colors :
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        colors.append((r,g,b))
    return colors


# Modélistation d'une percolation de Bernoulli de paramètre p

def percolation(n, p, r='') :

    print("\nProbabilité p =", p)
    
    # Modélisation du réseau de la forêt 
    grid = [list() for i in range(n)]
    for i in range(n) :
        grid[i] = [list() for j in range(n)]
        for j in range(n) :
            q = random.randint(1,100)/100
            if q < p or p==1 :
                grid[i][j] = 0
            else : 
                grid[i][j] = 1

    # Système sans mise en évidence des différents amas
    im = Image.new('RGB',(n,n))
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                im.putpixel((i,j),(203,51,255))
            else :
                im.putpixel((i,j),(0,0,0))

    # Recherche des amas
    clusters = list()
    in_cluster = [[False for j in range(n)] for i in range(n)]
    tmp  = list()
    
    stack = list()
    visited = [[False for j in range(n)] for i in range(n)]
    for x in range(n) :
        for y in range(n) :
            if grid[x][y] == 0 and in_cluster[x][y] == False : 
                stack.append([x,y])
                tmp.append([x,y])
                while stack != [] :
                    ind = stack.pop()
                    i = ind[0]; j = ind[1]
                    if visited[i][j] == False :
                        in_cluster[i][j] = True
                        # Gauche
                        if i-1>=0 and grid[i-1][j] == 0 and in_cluster[i-1][j] == False :
                            stack.append([i-1, j])
                            tmp.append([i-1, j])
                            
                        # Droite
                        if i+1<n and grid[i+1][j] == 0 and in_cluster[i+1][j] == False :
                            stack.append([i+1, j])
                            tmp.append([i+1, j])

                        # Bas
                        if j-1>=0 and grid[i][j-1] == 0 and in_cluster[i][j-1] == False :
                            stack.append([i, j-1])
                            tmp.append([i, j-1])

                        # Haut
                        if j+1<n and grid[i][j+1] == 0 and in_cluster[i][j+1] == False :
                            stack.append([i, j+1])
                            tmp.append([i, j+1])
                        visited[i][j] = True
                
                clusters.append(tmp)
                tmp = list()

    colors = colors_tab(len(clusters))
    color = (128,68,181)
    
    
    for l in range(len(clusters)):
    	print(clusters[l])
    	if len(clusters[l]) != 0 :
    		for i in range(len(clusters[l])) :
    			for j in range(len(clusters[l])) :
    				print(i, j)
	    			if i != j :
	    				if clusters[l][i] == clusters[l][j] :
	    					clusters[l].pop(i)
	    					l -= 1

    maxi = 0
    ind_maxi = 0
    for l in range(len(clusters)) :
        if len(clusters[l]) > maxi :
            maxi = len(clusters[l])
            ind_maxi = l
    					
 
    			
    
    for l in range(len(clusters)) :
        while clusters[l] != [] :
            ind = clusters[l].pop()
            i = ind[0]
            j = ind[1]
            if l != ind_maxi :
                im.putpixel((i,j), colors[l])
            else :
                im.putpixel((i,j), color)


    titre = 'image_'+str(r)+'_'+str(p)+'.png'
    im.save(titre, 'png')



for i in range(21) :
    percolation(500, 5*i/100, i)
