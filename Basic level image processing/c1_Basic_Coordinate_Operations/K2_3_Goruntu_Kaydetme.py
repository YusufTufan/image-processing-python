# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:59:12 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


cv2.imwrite('gri_seviye_ari.png',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()