# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:09:36 2024

@author: muozi
"""

import cv2
import numpy as np

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture("Video_Trafic.mp4")

# Çekirdekleri oluştur
kernel1 = np.array([[0, -1, -1],
                    [1, 0, -1],
                    [1, 1, 0]])

kernel2 = np.array([[-1, -1, 0],
                    [-1, 0, 1],
                    [0, 1, 1]])

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Görüntüyü gri tona çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Emboss efektini uygula
    output1 = cv2.filter2D(gray, -1, kernel1)
    output2 = cv2.filter2D(gray, -1, kernel2)
    
    # Görüntüleri birleştirerek güçlendirilmiş emboss efekti oluştur
    output = np.maximum(output1, output2)
    
    # Görüntüleri ekranda göster
    cv2.imshow("Original Image", frame)
    cv2.imshow("Emboss Effect 1", output1)
    cv2.imshow("Emboss Effect 2", output2)
    cv2.imshow("Combined Emboss Effect", output)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
