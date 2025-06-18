# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:06:52 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


print("Renkli toplam piksel sayisi: " + str(img.size))
print("Gri toplam piksel sayisi " +str(img1.size))

img_size=img.size
img1_size=img1.size


cv2.waitKey(0)
cv2.destroyAllWindows()