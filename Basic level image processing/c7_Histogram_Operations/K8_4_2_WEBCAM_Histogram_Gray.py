# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:51:44 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Webcam yakalama
cap = cv2.VideoCapture(0)

while(True):
    # Kare yakalama
    ret, frame = cap.read()
    
    # Gri seviyeye dönüştürme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Histogram hesaplama
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # Histogramı gösterme
    plt.plot(hist, color='b')
    plt.title('Gri Seviye Histogram')
    plt.draw()
    plt.pause(0.01)
    plt.clf()  # Önceki çizimleri temizleme
    
    # Görüntüyü gösterme
    cv2.imshow('frame',gray)
    
    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Yakalama serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
