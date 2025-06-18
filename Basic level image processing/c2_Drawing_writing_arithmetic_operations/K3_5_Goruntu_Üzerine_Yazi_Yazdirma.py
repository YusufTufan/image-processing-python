# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:39:12 2024

@author: muozi
"""

import cv2




img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.putText(img,'Arilar',(5,100),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),1,cv2.LINE_AA)
# #Sol Alt Köşenin koordinatı yazılır
cv2.imshow('yaz',img)


cv2.waitKey(0)
cv2.destroyAllWindows()