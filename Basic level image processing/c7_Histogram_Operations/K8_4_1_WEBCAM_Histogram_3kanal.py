# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:10:30 2024

@author: muozi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Webcam yakalama
cap = cv2.VideoCapture(0)

while True:
    # Kare yakalama
    ret, frame = cap.read()
    
    # Video sonuna gelindiğinde döngüyü sonlandır
    if not ret:
        break
    
    # Histogramları hesapla
    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    
    # Histogramları göster
    plt.title('Image Histogram')
    plt.draw()
    plt.pause(0.01)
    plt.clf()
    
    # Görüntüyü göster
    cv2.imshow('frame', frame)
    
    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Yakalama serbest bırakma ve pencereleri kapatma
cap.release()
cv2.destroyAllWindows()
