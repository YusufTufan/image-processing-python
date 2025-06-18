# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:25:27 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


# İKİNCİ YÖNTEM
blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]

cv2.imshow('blue2',blue)
cv2.imshow('green2',green)
cv2.imshow('red2',red)





cv2.waitKey(0)
cv2.destroyAllWindows()