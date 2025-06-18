# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:10:19 2023

@author: MUOZIC
"""

import cv2

# İlk görüntüyü yükle
img1 = cv2.imread('Bitwise_1.png')

# İkinci görüntüyü yükle
img2 = cv2.imread("Bitwise_2.png")

# İki görüntü arasında bit düzeyinde AND işlemi gerçekleştir
bit_and = cv2.bitwise_and(img2, img1)

print("Veri Tipi IMG_1:"+str(img1.dtype))
print("Veri Tipi IMG_2:"+str(img2.dtype))

# Görüntüleri göster
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitwise_and", bit_and)

cv2.waitKey(0)
cv2.destroyAllWindows()
