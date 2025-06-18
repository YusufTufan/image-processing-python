# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:18:47 2024

@author: muozi
"""

import cv2
import numpy as np

img1 = cv2.imread('skin_cancer_lesion.bmp')
img2 = cv2.imread('skin_cancer_lesion_maske.bmp')
cv2.imshow('Maske', img2)

print(img1.shape)
print(img1.dtype)
print(img2.shape)
print(img2.dtype)

carpma1 = cv2.multiply(img2, img1)  # İlk çarpma
cv2.imshow('carpma1', carpma1)

# Tüm değerleri 0'dan büyük olanları 1'e ata
img2[img2 > 0] = 1
cv2.imshow('skin_cancer', img1)
cv2.imshow('skin_cancer_maske', img2)

carpma = cv2.multiply(img2, img1)  # İkinci çarpma
cv2.imshow('carpma2', carpma)

cv2.waitKey(0)
cv2.destroyAllWindows()
