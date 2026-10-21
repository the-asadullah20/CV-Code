import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray=cv.resize(gray,(64,128))

hog=cv.HOGDescriptor((64,128),(16,16),(8,8),(8,8),9)

features=hog.compute(gray)

print("HOG feature vector shape:",features.shape)
print("Total features:",features.size)
