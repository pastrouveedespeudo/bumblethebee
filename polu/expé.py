import os
import re
import cv2
import numpy as np
from PIL import Image
from statistics import mean


class expé:

    def ouverture(self, image):

        self.image = image
        
        im = cv2.imread(self.image)
        imgray = cv2.cvtColor (im, cv2.COLOR_BGR2GRAY)
        
        ret, thresh = cv2.threshold (imgray, 127,255,0)
        im2, contours, hiérarchie = cv2.findContours (thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours (im, contours, -1, (0,0,0), 2)
        cv2.drawContours (im, contours, 3, (0,0,0), 1)
        cnt = contours [4]
        cv2.drawContours (im, [cnt], 0, (0,0,0), 1)

    
        cv2.imshow("self.image", im)
        cv2.imwrite("contour.png",im)


    def roi(self):
        
        im = cv2.imread("contour.png")
        #cv2.imshow("self.image1", im)
        x = 140
        y = 60
        h = 40
        w = 50
        
        x1 = 55
        y1 = 10
        h1 = 62
        w1 = 55

        x2 = 1
        y2 = 1
        h2 = 50
        w2 = 50
        
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        crop = im[y:y+h, x:x+w]
        cv2.rectangle(im, (x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        crop2 = im[y1:y1+h1, x1:x1+w1]
        cv2.rectangle(im, (x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        crop3 = im[y2:y2+h2, x2:x2+w2]

        #cv2.imshow("self.image", im)
        #cv2.imshow("self.image2", crop)
        cv2.imwrite("contour1.png", crop)
        cv2.imwrite("contour2.png", crop2)
        cv2.imwrite("contour3.png",crop3)

    def image_gris(self):
       
        im = cv2.imread("1_1000_3000m3.jpg")
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("yo.png", imgray)
        cv2.imwrite("coucou.png", imgray)

        im = cv2.imread("coucou.png")
     

        x = 140
        y = 60
        h = 40
        w = 50
        
        x1 = 55
        y1 = 10
        h1 = 62
        w1 = 55

        x2 = 1
        y2 = 1
        h2 = 50
        w2 = 50
        
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        crop = im[y:y+h, x:x+w]
        cv2.rectangle(im, (x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        crop2 = im[y1:y1+h1, x1:x1+w1]
        cv2.rectangle(im, (x2,y2),(x2+w2,y2+h2),(255,0,0),2)
        crop3 = im[y2:y2+h2, x2:x2+w2]

        cv2.imshow("self.image", crop)
        cv2.imshow("self.image2", crop2)
        cv2.imshow("self.image3", crop3)
        
        cv2.imwrite("contour1_nb.png", crop)
        cv2.imwrite("contour2_nb.png", crop2)
        cv2.imwrite("contour3_nb.png",crop3)

        
    def contraste(self):
        #luminance0.2126*R+0.7152*V+0.0722*B
        #faire la moyenne
        #contraste = limage - lcontour3/lcontour3

        
        liste_fond = []
        liste_image_loin = []
        liste_image_pres = []
        
        lumi_fond = cv2.imread("contour3_nb.png")
        for x in range(lumi_fond.shape[0]):
            for y in range(lumi_fond.shape[1]):
                a = lumi_fond[x,y][0] * 0.2126
                b = lumi_fond[x,y][1] * 0.7152
                c = lumi_fond[x,y][2] * 0.0722
                total = a + c + c
                liste_fond.append(total)
                
        lumi_im_pres = cv2.imread("contour1_nb.png")
        for x in range(lumi_im_pres.shape[0]):
            for y in range(lumi_im_pres.shape[1]):
                a = lumi_im_pres[x,y][0] * 0.2126
                b = lumi_im_pres[x,y][1] * 0.7152
                c = lumi_im_pres[x,y][2] * 0.0722
                total = a + c + c
                lumi_im_pres.append(total)

        liste_image_loin = cv2.imread("contour1_nb.png")
        for x in range(liste_image_loin.shape[0]):
            for y in range(liste_image_loin.shape[1]):
                a = liste_image_loin[x,y][0] * 0.2126
                b = liste_image_loin[x,y][1] * 0.7152
                c = liste_image_loin[x,y][2] * 0.0722
                total = a + c + c
                liste_image_loin.append(total)


        print(mean(liste_fond))
        print(mean(liste_image_loin))
        print(mean(liste_image_pres))



        #contraste = limage - lcontour3/lcontour3
        #factorise ouais ben jle ferai apres

        
        
yo = expé()
yo.ouverture("1_1000_3000m3.jpg")
yo.roi()
yo.image_gris()
yo.contraste()
