import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

hist=[0]*256

img=cv.imread('pic.jpg')
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

for row in gray:
    for pixel in row:
        hist[pixel]+=1

cdf=[0]*256

cdf[0]=hist[0]

for i in range(1,256):
    cdf[i]=hist[i]+cdf[i-1]
    
mini=min(cdf)

total_pixels=gray.shape[0]*gray.shape[1]
deno=total_pixels-mini

result=np.zeros_like(gray)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        pixel=gray[i][j]
        new=((cdf[pixel]-mini)/deno)*255
        result[i][j]=int(new)

equalized=cv.equalizeHist(gray)

plt.figure(figsize=(30,30))

plt.subplot(1,4,1)
plt.imshow(rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(gray,cmap='gray')
plt.title('Gray Image')
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(equalized,cmap='gray')
plt.title('Library Equalizer')
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(result,cmap='gray')
plt.title('High Constrast -> (Manual Equalizer')
plt.axis('off')

plt.show()