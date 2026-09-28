import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("pic.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
gy=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

magnitude=cv2.magnitude(gx,gy)

plt.figure(figsize=(20,20))

plt.subplot(1,3,1)
plt.imshow(gx,cmap="gray")
plt.title("Gx")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gy,cmap="gray")
plt.title("Gy")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(magnitude,cmap="gray")
plt.title("Gradient Magnitude")
plt.axis("off")

plt.show()