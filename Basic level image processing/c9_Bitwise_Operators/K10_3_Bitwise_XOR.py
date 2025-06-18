# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:24:59 2024

@author: muozi
"""

import cv2

# İlk görüntüyü yükle
img1 = cv2.imread('Bitwise_1.png')

# İkinci görüntüyü yükle
img2 = cv2.imread("Bitwise_2.png")

# İki görüntü arasında bit düzeyinde XOR işlemi gerçekleştir
bit_xor = cv2.bitwise_xor(img1, img2)

print("Veri Tipi IMG_1:"+str(img1.dtype))
print("Veri Tipi IMG_2:"+str(img2.dtype))

# Görüntüleri göster
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitwise_img2", bit_xor)
cv2.imwrite("sonuc.png", bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
