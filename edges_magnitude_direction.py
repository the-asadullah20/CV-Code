import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gx=cv.Sobel(gray,cv.CV_64F,0,1,3)
gy=cv.Sobel(gray,cv.CV_64F,0,1,3)

magnitude=cv.magnitude(gx,gy)
direction=cv.phase(gx,gy,True)

plt.figure(figsize=(20,20))

plt.subplot(1,6,1)
plt.imshow(rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,6,2)
plt.imshow(gray,cmap='gray')
plt.title('Gray Image')
plt.axis('off')

plt.subplot(1,6,3)
plt.imshow(gx,cmap='gray')
plt.title('Horizontal Edges')
plt.axis('off')

plt.subplot(1,6,4)
plt.imshow(gy,cmap='gray')
plt.title('Vertical Edges')
plt.axis('off')

plt.subplot(1,6,5)
plt.imshow(magnitude,cmap='gray')
plt.title('Magnitude')
plt.axis('off')

plt.subplot(1,6,6)
plt.imshow(direction,cmap='gray')
plt.title('Direction of Edges')
plt.axis('off')

plt.show()

