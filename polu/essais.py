import matplotlib.pyplot as plt
import cv2
from PIL import Image

im = cv2.imread("Image_blanche.png")



im[200:400,200:400] = [150, 150, 150]



cv2.imshow("coucou.png", im)
