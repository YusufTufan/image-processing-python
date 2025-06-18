# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:08:10 2024

@author: muozi
"""

import cv2
import numpy as np

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture("Video_Trafic.mp4")

# Sharpening kernel oluştur
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Kenar artırma (sharpening) uygula
    sharpened_frame = cv2.filter2D(frame, -1, kernel)

    # Orijinal ve kenar artırılmış görüntüleri göster
    cv2.imshow("original", frame)
    cv2.imshow("Sharpened Image", sharpened_frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
