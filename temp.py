import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

guassian=cv.GaussianBlur(gray,(11,11),0)

gx=cv.Sobel(gray,cv.CV_64F,1,0,3)
gy=cv.Sobel(gray,cv.CV_64F,0,1,3)

magnitude=cv.magnitude(gx,gy)

directions=cv.phase(gx,gy,True)

edges=cv.Canny(gray,100,200)

plt.figure(figsize=(30,30))

plt.subplot(1,7,1)
plt.imshow(rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,7,2)
plt.imshow(gray,cmap='gray')
plt.title('Gray Scale Image')
plt.axis('off')

plt.subplot(1,7,3)
plt.imshow(gx,cmap='gray')
plt.title('Horizontal Edges')
plt.axis('off')

plt.subplot(1,7,4)
plt.imshow(gy,cmap='gray')
plt.title('Vertical Edges')
plt.axis('off')

plt.subplot(1,7,5)
plt.imshow(magnitude,cmap='gray')
plt.title('Magnitude')
plt.axis('off')

plt.subplot(1,7,6)
plt.imshow(directions,cmap='gray')
plt.title('Directions')
plt.axis('off')

plt.subplot(1,7,7)
plt.imshow(edges,cmap='gray')
plt.title('Canny Edges Detection')
plt.axis('off')

plt.show()
