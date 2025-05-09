# Date : 16/07/2024 - 
# Balthazar RICHARD
# Analyses de percolations dans un reseaux carre modélisant un feu de forết.


import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import GifImagePlugin


# Modélistation de la propagation du feu.

def percolation(n, m, p, r='') :

    print("\nProbabilité de transmission du feu d'un arbre à l'autre :", p)
    
    # Modélisation du réseau de la forêt 
    grid = [list() for i in range(n)]
    for i in range(n) :
        grid[i] = [list() for j in range(m)]
        for j in range(m) :
            grid[i][j] = 0
    burning = list()
    neighbor = list()
    burnt = list()

    # Fôret sans feu
    im = Image.new('RGB',(n,m))
    for i in range(n):
        for j in range(m):
            im.putpixel((i,j),(0,255,0))
    im.save('foret_0.png', 'png')

    # Premier arbre en feu
    x = random.randint(0,n-1)
    y = random.randint(0,m-1)
    burning.append([x, y])
    grid[x][y] = 1
    im.putpixel((x,y),(194,24,7))
    im.save('foret_1.png', 'png')


    # Percolation
    alpha = 2
    while burning != [] or neighbor != []  :
        while burning != [] :
            ind = burning.pop(0)
            x = ind[0]; y = ind[1]

            # Gauche
            if x-1>=0 and grid[x-1][y] == 0:
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x-1, y])
                    grid[x-1][y] = 1
                    im.putpixel((x-1,y),(255,0,0))
            
            # Droite
            if x+1<n and grid[x+1][y] == 0:
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x+1, y])
                    grid[x+1][y] = 1
                    im.putpixel((x+1,y),(255,0,0))

            # Bas
            if y-1>=0 and grid[x][y-1] == 0:
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x, y-1])
                    grid[x][y-1] = 1
                    im.putpixel((x,y-1),(255,0,0))

            # Haut
            if y+1<m and grid[x][y+1] == 0:
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x, y+1])
                    grid[x][y+1] = 1
                    im.putpixel((x,y+1),(255,0,0))

            """ # Bas gauche
            if x-1>=0 and y-1>=0 and grid[x-1][y-1] == 0 :
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x-1, y-1])
                    grid[x-1][y-1] = 1
                    im.putpixel((x-1,y-1),(255,0,0))

            # Haut gauche
            if x-1>=0 and y+1<m and grid[x-1][y+1] == 0 :
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x-1, y+1])
                    grid[x-1][y+1] = 1
                    im.putpixel((x-1,y+1),(255,0,0))

            # Bas droit
            if x+1<n and y-1>=0 and grid[x+1][y-1] == 0 :
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x+1, y-1])
                    grid[x+1][y-1] = 1
                    im.putpixel((x+1,y-1),(255,0,0))
            
            # Haut droit
            if x+1<n and y+1<m and grid[x+1][y+1] == 0 :
                q = random.randint(1, 100)/100
                if q<p or p==1 :
                    neighbor.append([x+1, y+1])
                    grid[x+1][y+1] = 1
                    im.putpixel ((x+1,y+1),(255,0,0))"""
        
            burnt.append(ind)
            grid[x][y] = 2
            im.putpixel((x,y),(0,0,0))

        burning = neighbor
        neighbor = list()
        titre = 'foret_'+str(alpha)+'.png'
        im.save(titre, 'png')
        alpha += 1

    alive = 0
    burnt2 = 0
    for i in range(n) :
        for j in range(m) :
            if grid[i][j] == 0 :
                alive += 1
            elif grid[i][j] == 2 :
                burnt2 += 1
    
    print("Au total,", burnt2, "arbre(s) brulé(s) et", alive, "arbre(s) encore vert.\n")


    # Création d'un GIF

    imgs = list()
    im1 = Image.open('foret_0.png')
    
    for i in range(1, alpha) :
        noms = 'foret_'+str(i)+'.png'
        imgs.append(Image.open(noms))
    im1.save('percolation_foret_'+str(r)+'_'+str(p)+'.gif', save_all=True, append_images=imgs, duration=alpha/10, loop=0, optimize=True, include_color_table=True, interlace=True)



for i in range(10) :
	percolation(200, 200, 52/100, i) 
