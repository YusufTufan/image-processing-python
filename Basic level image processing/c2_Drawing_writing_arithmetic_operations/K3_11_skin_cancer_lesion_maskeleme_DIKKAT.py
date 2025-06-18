# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:48:17 2023

@author: muozi
"""

import cv2
import numpy as np



img1=cv2.imread('skin_cancer_lesion.bmp')
img2=cv2.imread('skin_cancer_lesion_maske.bmp')
cv2.imshow('Maske',img2)


print(img1.shape)
print(img1.dtype)
print(img2.shape)
print(img2.dtype)

carpma1=cv2.multiply(img2,img1) # İLK ÇARPMADA TÜM DEĞERLER 255 İ AŞTIĞI İÇİN 255 E ÇEKİLİYOR
cv2.imshow('carpma1',carpma1)



img2[img2 == 255] = 1
cv2.imshow('skin_cancer',img1)
cv2.imshow('skin_cancer_maske',img2) # NEDEN KOMPLE SİYAH GÖZÜKÜYOR, ÇÜNKÜ 1 E ÇEKİLDİ, SİYAHA YAKIN DEĞER

carpma=cv2.multiply(img2,img1)
cv2.imshow('carpma2',carpma)

cv2.waitKey(0)
cv2.destroyAllWindows()