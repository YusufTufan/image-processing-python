# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:10:49 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

# İLK YÖNTEM
b,g,r = cv2.split(img);

cv2.imshow('blue1',b)
cv2.imshow('green1',g)
cv2.imshow('red1',r)


cv2.waitKey(0)
cv2.destroyAllWindows()