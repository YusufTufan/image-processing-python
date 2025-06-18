# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:27:04 2024

@author: muozi
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt

# Resmi renkli olarak al
img = cv2.imread('bee.jpg')

# Renk kanallarını ayır
b, g, r = cv2.split(img)

# Her bir renk kanalı için histogramları hesapla
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Her bir renk kanalı için histogram eşitleme yap
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# Eşitlenmiş renk kanallarını birleştir
equ = cv2.merge((b_eq, g_eq, r_eq))

# Eşitlenmiş renk kanalları için histogramları hesapla
hist_b_eq = cv2.calcHist([b_eq], [0], None, [256], [0, 256])
hist_g_eq = cv2.calcHist([g_eq], [0], None, [256], [0, 256])
hist_r_eq = cv2.calcHist([r_eq], [0], None, [256], [0, 256])

# Görüntü ve histogramları göster
plt.figure(figsize=(15, 10))

# Orjinal görüntü ve histogramlar
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Orjinal Görüntü')

plt.subplot(2, 4, 2)
plt.plot(hist_b, color='b')
plt.title('Mavi Kanal Histogramı')

plt.subplot(2, 4, 3)
plt.plot(hist_g, color='g')
plt.title('Yeşil Kanal Histogramı')

plt.subplot(2, 4, 4)
plt.plot(hist_r, color='r')
plt.title('Kırmızı Kanal Histogramı')

# Eşitlenmiş görüntü ve histogramlar
plt.subplot(2, 4, 5)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title('Histogram Eşitleme Sonrası Görüntü')

plt.subplot(2, 4, 6)
plt.plot(hist_b_eq, color='b')
plt.title('Mavi Kanal Histogramı (Eşitleme Sonrası)')

plt.subplot(2, 4, 7)  # Yedinci subplot
plt.plot(hist_g_eq, color='g')
plt.title('Yeşil Kanal Histogramı (Eşitleme Sonrası)')

plt.subplot(2, 4, 8)  # Sekizinci subplot
plt.plot(hist_r_eq, color='r')
plt.title('Kırmızı Kanal Histogramı (Eşitleme Sonrası)')

plt.tight_layout()
plt.show()

