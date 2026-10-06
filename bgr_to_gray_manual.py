import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')

gray=np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b=img[i][j][0]
        g=img[i][j][1]
        r=img[i][j][2]
        gray[i][j]=0.299*r+0.587*g+0.114*b
        
cv.imshow('gray',gray)
cv.waitKey(0)
cv.destroyAllWindows()