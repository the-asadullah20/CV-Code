import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
equalized=cv.equalizeHist(gray)

plt.figure(figsize=(30,30))

plt.subplot(1,3,1)
plt.imshow(rgb)
plt.title('Original Color')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gray,cmap='gray')
plt.title('Gray Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(equalized,cmap='gray')
plt.title('High Constrast -> (Histogram Equalizer Applied)')
plt.axis('off')

plt.show()
