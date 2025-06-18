# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 23:10:48 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resmi siyah beyaz olarak yükle
img = cv2.imread('chessboard.png', 0)

# Prewitt kenar bulma uygula
prewittx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
prewitty = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

# Prewitt kenarlarını birleştir
prewitt_OR = cv2.bitwise_or(prewittx, prewitty)

# Görüntüleri görselleştir
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(prewittx, cmap='gray')
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(prewitty, cmap='gray')
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(prewitt_OR, cmap='gray')
plt.title('Prewitt OR'), plt.xticks([]), plt.yticks([])

plt.show()
