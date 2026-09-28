import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')

print(img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

print(gray)

cv.imshow('gray',gray)

blur=cv.blur(gray,(10,10))

cv.imshow('blur',blur)

cv.waitKey(0)
cv.destroyAllWindows()

