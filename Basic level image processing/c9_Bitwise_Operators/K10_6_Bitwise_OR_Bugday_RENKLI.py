# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:23:29 2024

@author: muozi
"""

import cv2

# İlk görüntüyü yükle
img1 = cv2.imread('Resim2_Coklu_Bugday.png')

# İkinci görüntüyü yükle
img2 = cv2.imread("Resim3_Bugday_Binary.png")

print("Veri Tipi IMG_1:"+str(img1.dtype))
print("Veri Tipi IMG_2:"+str(img2.dtype))

print("IMG1 Görüntü Boyutu:"+str(img1.shape))
print("IMG2 Görüntü Boyutu:"+str(img2.shape))
# İki görüntü arasında bit düzeyinde OR işlemi gerçekleştir
bit_or = cv2.bitwise_or(img2, img1)

# Görüntüleri göster
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitwise_or", bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows() 
