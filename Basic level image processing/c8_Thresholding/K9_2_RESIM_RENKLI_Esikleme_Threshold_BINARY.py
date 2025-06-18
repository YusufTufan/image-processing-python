# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:36:16 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Renkli görüntüyü oku
img = cv2.imread('Resim1_Dort_Nohut.png')
# img = cv2.imread('Resim2_Coklu_Bugday.png')

# R, G ve B kanallarına ayır
b, g, r = cv2.split(img)

# Her bir kanalı ayrı ayrı göster
cv2.imshow("BLUE", b)
cv2.imshow("GREEN", g)
cv2.imshow("RED", r)


# Her bir kanal üzerinde eşikleme işlemi uygula
ret1, thresh1 = cv2.threshold(b, 150, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(g, 150, 255, cv2.THRESH_BINARY)
ret3, thresh3 = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)

# Eşiklenmiş kanalları ayrı ayrı göster
cv2.imshow("THRESH_BINARY_BLUE", thresh1)
cv2.imshow("THRESH_BINARY_GREEN", thresh2)
cv2.imshow("THRESH_BINARY_RED", thresh3)


# Her bir kanal üzerinde histogram hesapla
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Histogramları ayrı ayrı figure nesnelerinde çiz
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(hist_b, color='b')
plt.title('BLUE Kanal Histogramı')

plt.subplot(3, 1, 2)
plt.plot(hist_g, color='g')
plt.title('GREEN Kanal Histogramı')

plt.subplot(3, 1, 3)
plt.plot(hist_r, color='r')
plt.title('RED Kanal Histogramı')

plt.tight_layout()
plt.show()

# Eşiklenmiş kanalları birleştir
thresh_combined = cv2.merge((thresh1, thresh2, thresh3))

# Birleştirilmiş eşiklenmiş kanalları göster
cv2.imshow("THRESH_BINARY_COMBINED", thresh_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
