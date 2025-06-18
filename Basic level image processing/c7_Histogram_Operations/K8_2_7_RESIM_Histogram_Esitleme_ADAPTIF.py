# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:06:23 2024

@author: muozi
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resim6_sudoku.JPG', 0)

# Görüntünün histogramını hesapla
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Adaptif histogram eşitleme için CLAHE nesnesi oluştur
# clipLimit parametresi, CLAHE (Contrast Limited Adaptive Histogram Equalization - 
# Kontrast Sınırlı Uyarlamalı Histogram Eşitleme) işleminde kullanılan bir parametredir. 
# Bu parametre, adaptif histogram eşitleme işlemindeki kontrast kısıtlamasını belirler.
# tileGridSize=pencere boyutu
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))

# Görüntüyü adaptif histogram eşitle
equ = clahe.apply(img)

# Eşitlenmiş görüntünün histogramını hesapla
hist2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

# İşlenmiş görüntüleri görselleştirme
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Gri Seviye Görüntü')

plt.subplot(2, 2, 2)
plt.plot(hist, color='b')
plt.title('Orijinal Gri Seviye Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equ, cmap='gray')
plt.title('Adaptif Histogram Eşitleme Sonrası Görüntü')

plt.subplot(2, 2, 4)
plt.plot(hist2, color='b')
plt.title('Adaptif Histogram Eşitleme Sonrası Histogram')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()