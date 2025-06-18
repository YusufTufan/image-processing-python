# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:10:30 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Webcam yakalama
cap = cv2.VideoCapture(0)

# Plot oluşturma
plt.figure(figsize=(10, 6))
plt.ion()  # Interaktif modu aç

# Adaptif histogram eşitleme için CLAHE nesnesi oluştur
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

while True:
    # Kare yakalama
    ret, frame = cap.read()
    
    # Görüntüyü gri seviyeye dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Adaptif histogram eşitleme
    equ = clahe.apply(gray)
    
    # Histogramları hesapla
    hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])
    
    # Plot'u güncelle
    plt.clf()  # Önceki plot'u temizle
    
    # Orijinal görüntü ve histogram
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title('Orjinal Görüntü')
    
    plt.subplot(2, 2, 2)
    plt.plot(hist_gray, color='b')
    plt.title('Orjinal Görüntü Histogramı')
    plt.xlim([0, 256])
    
    # Adaptif histogram eşitleme sonrası görüntü ve histogram
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
    plt.title('Adaptif Histogram Eşitleme Sonrası Görüntü')
    
    plt.subplot(2, 2, 4)
    plt.plot(hist_equ, color='b')
    plt.title('Adaptif Histogram Eşitleme Sonrası Histogram')
    plt.xlim([0, 256])
    
    plt.pause(0.01)  # Plot'u güncelle
       
    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Yakalama serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
