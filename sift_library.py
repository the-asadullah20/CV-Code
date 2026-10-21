import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


sift=cv.SIFT_create()


keypoints,descriptors=sift.detectAndCompute(gray,None)

print('keypoints',len(keypoints))
print('descriptors',len(descriptors))

plt.figure(figsize=(30,30))
plt.subplot(1,2,1)
plt.imshow(keypoints)
plt.title('Keypoints:')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(descriptors)
plt.title('Descriptors:')
plt.axis('off')

plt.show()

