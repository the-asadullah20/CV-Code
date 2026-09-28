import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('pic.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(7,7),0)
cv.imshow('blur',blur)

cv.waitKey(0)
cv.destroyAllWindows()

