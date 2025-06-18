# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:41:29 2024

@author: muozi
"""


import cv2

# İlk görüntüyü yükle
img1 = cv2.imread('Resim1_Dort_Nohut.png',0)

# İkinci eşikleme işlemi için görüntünün boyutlarına uygun olarak eşikleme yap
ret, thresh = cv2.threshold(img1, 150, 255, cv2.THRESH_TOZERO_INV)

# İki görüntü arasında bit düzeyinde AND işlemi gerçekleştir
bit_and = cv2.bitwise_and(img1, thresh)

# İki görüntü arasında bit düzeyinde OR işlemi gerçekleştir
bit_or = cv2.bitwise_or(img1, thresh)

# İki görüntü arasında bit düzeyinde XOR işlemi gerçekleştir
bit_xor = cv2.bitwise_xor(img1, thresh)

# İki görüntü arasında bit düzeyinde NOT işlemi gerçekleştir
bit_not = cv2.bitwise_not(img1)

# Görüntüleri göster
cv2.imshow("img1", img1)
cv2.imshow("thresh", thresh)
cv2.imshow("bitwise_and", bit_and)
cv2.imshow("bitwise_or", bit_or)
cv2.imshow("bitwise_xor", bit_xor)
cv2.imshow("bitwise_not", bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()