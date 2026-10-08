import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(7,7),0)

log_edges=cv.Laplacian(blur,cv.CV_64F)
canny_edges=cv.Canny(blur,100,200)

plt.figure(figsize=(30,30))

plt.subplot(1,2,1)
plt.imshow(canny_edges,cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(log_edges,cmap='gray')
plt.title('Log Edges')
plt.axis('off')

plt.show()
