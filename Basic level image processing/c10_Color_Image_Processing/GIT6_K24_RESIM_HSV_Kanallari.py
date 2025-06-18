# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:24:15 2024

@author: muozi
"""

import cv2

# Görüntüyü yükle
image = cv2.imread('img4_Bugday.png')

# Görüntüyü HSV renk uzayına dönüştür
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV kanallarını ayır
H, S, V = cv2.split(hsvImage)

# Orijinal görüntüyü ve HSV kanallarını göster
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsvImage)
cv2.imshow('H Channel', H)  # H Kanalı
cv2.imshow('S Channel', S)  # S Kanalı
cv2.imshow('V Channel', V)  # V Kanalı

# Görüntüleri ekranda tut
cv2.waitKey(0)
cv2.destroyAllWindows()
