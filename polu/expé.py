import os
import re
import cv2
import numpy as np
import argparse

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
        cv2.imshow("self.image1", im)
        x = 140
        y = 60
        h = 40
        w = 50
        
        x1 = 55
        y1 = 10
        h1 = 70
        w1 = 55
        
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        crop = im[y:y+h, x:x+w]
        cv2.rectangle(im, (x1,y1),(x1+w1,y1+h1),(0,255,255),2)


        cv2.imshow("self.image", im)
        cv2.imshow("self.image2", crop)






yo = expé()
yo.ouverture("1_1000_3000m3.jpg")
yo.roi()
