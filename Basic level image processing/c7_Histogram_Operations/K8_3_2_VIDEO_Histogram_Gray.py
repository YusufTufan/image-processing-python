# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:57:47 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video yakalama
cap = cv2.VideoCapture('Video_Trafic.mp4')

while True:
    # Kare yakalama
    ret, frame = cap.read()
    
    # Video sonuna gelindiğinde döngüyü sonlandır
    if not ret:
        break
    
    # Gri seviyeye dönüştürme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Histogram hesaplama
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # Histogramı gösterme
    plt.plot(hist, color='b')
    plt.title('Gri Seviye Histogram')
    plt.pause(0.01)  # Pencereyi 0.01 saniye göster
    plt.clf()        # Önceki çizimleri temizleme
    
    # Görüntüyü gösterme
    cv2.imshow('frame', gray)
    
    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Yakalama serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
