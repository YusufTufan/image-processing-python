# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:00:22 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)

a=img.shape

print("Renkli Görüntü Boyutu:"+str(img.shape))
print("Gri Görüntü Boyutu:"+str(img1.shape))


cv2.waitKey(0)
cv2.destroyAllWindows()