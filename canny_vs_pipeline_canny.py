import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(5,5),0)

edges=cv.Canny(blur,100,200)

plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gray)
plt.title('Gray Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(edges)
plt.title('Edges Detection Image')
plt.axis('off')

plt.show()
