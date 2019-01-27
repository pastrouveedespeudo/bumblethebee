
import os
import cv2
import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from resizeimage import resizeimage

class image:

    def resizer(self):

        os.chdir(r"C:\Users\jeanbaptiste\polu\image\polution")
        liste = os.listdir()
        for i in liste:
            with open(i, 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, [200, 100])
                    cover.save(str(i), "png")

        

    def parcours_image(self, image, couleur):

        self.image = image
        self.couleur = couleur
        
        c = 0
        
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                if self.image[x,y][0] == self.couleur[0]and\
                   self.image[x,y][1] == self.couleur[1]and\
                   self.image[x,y][2] == self.couleur[2]:
                    c+=1

        print("couleur bleu reucrente:",c)
        

                
    def image(self, path):

        self.path = path

        os.chdir(self.path)
        liste = os.listdir()
        print(liste)
        
        for imageliste in liste:
 
     
            #image.parcours_image(self, ima, [0,0,0])

            dico = {}
            
            im = Image.open(imageliste)
            
            for value in im.getdata():
                if value in dico.keys():
                     dico[value] += 1
                else:
                     dico[value] = 1

     
            liste_dico = []
            
            for i in dico.values():
                liste_dico.append(i)
                
            liste_dico= sorted(liste_dico, reverse = True)
            c = 0
            liste_couleur = []

            for i in liste_dico:
                if [c for c,v in dico.items() if v==i] == [(0, 0, 255)]:
                    c-=1
                elif [c for c,v in dico.items() if v==i] != [(0, 0, 255)]:
                    liste_couleur.append(i)
                    liste_couleur.append([c for c,v in dico.items() if v==i])
                c+=1
                if c == 20:
                    break
            print(liste_couleur)
                                
            print("image:",imageliste)
     
            

#regarde quel tonalité bleu et rouge quand est ce que ca passe du rouge au bleu ou jaune orange 

#correlation de couleur et polution

yo = image()
#yo.resizer()
yo.image(r"C:\Users\jeanbaptiste\polu\image\polution")




