import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math


img=cv.imread('pic.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sx=np.array([[-1,0,1],
             [-2,0,2],
             [-1,0,1]])
sy=np.array([[-1,-2,-1],
             [0,0,0],
             [1,2,1]])

gx=cv.filter2D(gray,cv.CV_64F,sx)
gy=cv.filter2D(gray,cv.CV_64F,sy)


