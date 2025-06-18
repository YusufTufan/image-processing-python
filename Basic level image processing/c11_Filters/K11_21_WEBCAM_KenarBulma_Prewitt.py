# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:15:03 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture(0)

# Tek bir figür oluştur
plt.figure(figsize=(10, 10))

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Kareyi siyah beyaz olarak dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Prewitt kenar tespiti uygula
    prewittx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
    prewitty = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=3)
    
    # Prewitt kenarlarını birleştir
    prewitt_OR = cv2.bitwise_or(prewittx, prewitty)
    
    # Görüntüyü görselleştir
    plt.clf()  # Önceki çizimleri temizle
    plt.subplot(2, 2, 1), plt.imshow(gray, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(prewittx, cmap='gray')
    plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(prewitty, cmap='gray')
    plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(prewitt_OR, cmap='gray')
    plt.title('Prewitt OR'), plt.xticks([]), plt.yticks([])

    plt.pause(0.001)  # Her iterasyonda güncelleme yapmak için kısa bir süre beklet

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()

