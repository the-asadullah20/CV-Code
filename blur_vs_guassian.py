import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

mean=cv.blur(img,(10,10))
guassian=cv.GaussianBlur(img,(11,11),0)
median=cv.medianBlur(img,11)

mean_rgb=cv.cvtColor(mean,cv.COLOR_BGR2RGB)
guassain_rgb=cv.cvtColor(guassian,cv.COLOR_BGR2RGB)
median_rgb=cv.cvtColor(median,cv.COLOR_BGR2RGB)

plt.figure(figsize=(20,20))
plt.subplot(1,4,1)
plt.imshow(rgb)
plt.title('Real Image')
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(mean_rgb)
plt.title('Mean RGB')
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(guassain_rgb)
plt.title('Guassian RBG')
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(median_rgb)
plt.title("Medain RGB")
plt.axis('off')

plt.show()
