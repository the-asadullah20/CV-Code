import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math


img=cv.imread('pic.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(7,7),0)

sx=np.array([[-1,0,1],
             [-2,0,2],
             [-1,0,1]])
sy=np.array([[-1,-2,-1],
             [0,0,0],
             [1,2,1]])

gx=cv.filter2D(blur,cv.CV_64F,sx)
gy=cv.filter2D(blur,cv.CV_64F,sy)


magnitude=np.sqrt(gx**2+gy**2)


angle=np.arctan2(gy,gx)
angle=angle*180/np.pi  # -> np.arctan angle radian me deta hai
angle[angle<0]+=180

nms=np.zeros_like(magnitude)

h,w=blur.shape

for i in range(1,h-3):
    for j in range(1,w-3):
        direction=angle[i][j]
        current=magnitude[i][j]
        if (0 < direction < 22.5) or (157.5 <=direction <=180):
            q=magnitude[i][j+1]
            r=magnitude[i][j-1]
        elif 22.5 <= direction <67.5:
            q=magnitude[i+1][j-1]
            r=magnitude[i-1][j+1]
        elif 67.5 <=direction <112.5:
            q=magnitude[i+1][j]
            r=magnitude[i-1][j]
        else:
            q=magnitude[i+1][j+1]
            r=magnitude[i-1][j-1]
            
        if current>=q and current>=r:
            nms[i][j]=current

strong=255
weak=75

high=100
low=50

result=np.zeros_like(nms)

result[nms>=high]=strong
result[(nms>=low) & (nms<high)]=weak

for i in range(1,h-1):
    for j in range(1,w-1):
        if nms[i][j]==weak:
            temp=result[i-1:i+2,j-1:j+2]
            
            if np.any(temp==strong):
                result[i][j]=strong
            else:
                result=0

canny_edges=cv.Canny(blur,100,200)

plt.figure(figsize=(30,30))
plt.subplot(1,2,1)
plt.imshow(canny_edges)
plt.title('Canny Edges Library')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(result)
plt.title('Manual Canny Detection')
plt.axis('off')

plt.show()
