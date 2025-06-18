# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:25:48 2024

@author: muozi
"""

import cv2

# İlk görüntüyü yükle
img1 = cv2.imread('Bitwise_1.png')

# İkinci görüntüyü yükle
img2 = cv2.imread("Bitwise_2.png")

# İlk görüntü için NOT işlemi
not_img1 = cv2.bitwise_not(img1)

# İkinci görüntü için NOT işlemi
not_img2 = cv2.bitwise_not(img2)


print("Veri Tipi IMG_1:"+str(img1.dtype))
print("Veri Tipi IMG_2:"+str(img2.dtype))

# Görüntüleri göster
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitwise_img1", not_img1)
cv2.imshow("bitwise_not_img2", not_img2)
cv2.imwrite("sonuc_bitwisenot.png", not_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
