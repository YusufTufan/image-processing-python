# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:51:19 2024

@author: muozi
"""

import cv2

# 'messi.jpg' adlı bir görüntü dosyası OpenCV ile yüklenir
resim = cv2.imread('messi.jpg')

# Görüntü, cv2.pyrUp() fonksiyonu kullanılarak tam iki kat büyütülür
up = cv2.pyrUp(resim)

# Görüntü, cv2.pyrDown() fonksiyonu kullanılarak tam iki kat küçültülür
down = cv2.pyrDown(resim)

# Orijinal görüntü ve işlem sonucu elde edilen görüntüler ekranda gösterilir
cv2.imshow('Orjinal', resim)
cv2.imshow('Üst', up)
cv2.imshow('Alt', down)

# Bir tuşa basılana kadar bekler ve tüm pencereleri kapatır
cv2.waitKey(0)
cv2.destroyAllWindows()
