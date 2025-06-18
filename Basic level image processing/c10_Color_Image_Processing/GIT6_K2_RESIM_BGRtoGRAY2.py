# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:22:56 2023

@author: MUOZIC
"""


import cv2


img=cv2.imread('bee.jpg')
img2=cv2.imread('bee.jpg',0)

cv2.imshow("RENKLI",img)
cv2.imshow("GRI SEVIYE",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()