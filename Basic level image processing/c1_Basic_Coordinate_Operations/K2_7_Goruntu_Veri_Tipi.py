# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:09:06 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


print("Veri Tipi Renkli:"+str(img.dtype))
print("Veri Tipi Gray:"+str(img1.dtype))


cv2.waitKey(0)
cv2.destroyAllWindows()