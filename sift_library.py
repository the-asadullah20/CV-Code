import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


sift=cv.SIFT_create()


keypoints,descriptors=sift.detectAndCompute(gray,None)

print('keypoints',len(keypoints))
print('descriptors',len(descriptors))


