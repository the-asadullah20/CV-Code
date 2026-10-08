import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(7,7),0)

kernel=np.array([[0,1,0],
                 [1,-4,1],
                 [0,1,0]])

lap=cv.filter2D(blur,cv.CV_64F,kernel)

threshold=7

zero_cross=np.zeros_like(lap,dtype=np.uint8)

for i in range(1,lap.shape[0]-1):
    for j in range(1,lap.shape[1]-1):
        region=lap[i-1:i+2,j-1:j+2]

        if region.max()>threshold and region.min()<-threshold:
            zero_cross[i,j]=255

canny=cv.Canny(blur,100,200)   
    
plt.figure(figsize=(30,30))
plt.subplot(1,2,1)
plt.imshow(canny,cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(zero_cross,cmap='gray')
plt.title('LoG Edges')
plt.axis('off')

plt.show()