# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:55:18 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

img3=cv2.imread('bee.jpg')
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
cv2.imshow('bee_gray',gray)


cv2.waitKey(0)
cv2.destroyAllWindows()