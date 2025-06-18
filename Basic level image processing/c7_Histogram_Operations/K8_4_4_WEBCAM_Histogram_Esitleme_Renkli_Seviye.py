# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:36:55 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Webcam yakalama
cap = cv2.VideoCapture(0)

# Plot oluşturma
plt.figure(figsize=(15, 10))
plt.ion()  # Interaktif modu aç

while True:
    # Kare yakalama
    ret, frame = cap.read()
    
    # Renk kanallarını ayır
    b, g, r = cv2.split(frame)
    
    # Her bir renk kanalı için histogram eşitleme yap
    b_eq = cv2.equalizeHist(b)
    g_eq = cv2.equalizeHist(g)
    r_eq = cv2.equalizeHist(r)
    
    # Eşitlenmiş renk kanallarını birleştir
    equ = cv2.merge((b_eq, g_eq, r_eq))
    
    # Histogramları hesapla
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    hist_equ_b = cv2.calcHist([b_eq], [0], None, [256], [0, 256])
    hist_equ_g = cv2.calcHist([g_eq], [0], None, [256], [0, 256])
    hist_equ_r = cv2.calcHist([r_eq], [0], None, [256], [0, 256])
    
    # Plot'u güncelle
    plt.clf()  # Önceki plot'u temizle
    
    # Orijinal görüntü ve histogram
    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title('Orjinal Görüntü')
    
    plt.subplot(2, 3, 2)
    plt.plot(hist_b, color='b')
    plt.title('Mavi Kanal Histogramı')
    plt.xlim([0, 256])
    
    plt.subplot(2, 3, 3)
    plt.plot(hist_g, color='g')
    plt.title('Yeşil Kanal Histogramı')
    plt.xlim([0, 256])
    
    plt.subplot(2, 3, 4)
    plt.plot(hist_r, color='r')
    plt.title('Kırmızı Kanal Histogramı')
    plt.xlim([0, 256])
    
    # Histogram eşitleme sonrası görüntü ve histogram
    plt.subplot(2, 3, 5)
    plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
    plt.title('Histogram Eşitleme Sonrası Görüntü')
    
    plt.subplot(2, 3, 6)
    plt.plot(hist_equ_b, color='b')
    plt.plot(hist_equ_g, color='g')
    plt.plot(hist_equ_r, color='r')
    plt.title('Histogram Eşitleme Sonrası Tüm Kanallar')
    plt.xlim([0, 256])
    
    plt.pause(0.01)  # Plot'u güncelle
    
    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Yakalama serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
