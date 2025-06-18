# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:22:56 2023

@author: MUOZIC
"""


import cv2


img=cv2.imread('bee.jpg')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


cv2.imshow("BGR",img)
cv2.imshow("RGB",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()