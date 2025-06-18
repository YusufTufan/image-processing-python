# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:16:37 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


# Region of Interest (ROI) Belirleme

ROI=img[200:270,150:220]# İlk Bileşen y ekseni
cv2.imshow('roi',ROI)

ROI2=img1[200:270,150:220]# İlk Bileşen y ekseni
cv2.imshow('roi2',ROI2)


cv2.waitKey(0)
cv2.destroyAllWindows()