
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
original=cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ix=cv.Sobel(gray,cv.CV_64F,1,0,3)
iy=cv.Sobel(gray,cv.CV_64F,0,1,3)

ixx=ix*ix
iyy=iy*iy
ixy=ix*iy

sxx=cv.GaussianBlur(ixx,(3,3),1)
syy=cv.GaussianBlur(iyy,(3,3),1)
sxy=cv.GaussianBlur(ixy,(3,3),1)

k=0.04
det=sxx*syy-sxy*sxy
trace=sxx+syy

R=det-k*(trace*trace)

threshold=0.01*R.max()

for j in range(1,R.shape[0]-1):
    for i in range(1,R.shape[1]-1):
        if R[j,i]>threshold and R[j,i]==np.max(R[j-1:j+2,i-1:i+2]):
            cv.circle(original,(i,j),3,(255,0,0),-1)

plt.figure(figsize=(12,12))
plt.imshow(original)
plt.title("Harris Corners")
plt.axis('off')
plt.show()
