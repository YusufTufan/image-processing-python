# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:27:27 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

# İLK YÖNTEM
b,g,r = cv2.split(img);


img2=cv2.merge((b,g,r))
cv2.imshow('merge',img2)



cv2.waitKey(0)
cv2.destroyAllWindows()