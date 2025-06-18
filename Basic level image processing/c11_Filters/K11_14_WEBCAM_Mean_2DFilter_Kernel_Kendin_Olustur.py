# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:02:30 2024

@author: muozi
"""

import cv2
import numpy as np

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture(0)

# Mean (ortalama) filtresi çekirdeğini tanımla
kernel_size = 7
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Filtreyi uygula
    filtered_frame = cv2.filter2D(frame, -1, kernel)

    # Görüntüyü ekranda göster
    cv2.imshow("Original Image", frame)
    cv2.imshow("Mean Filtered Image", filtered_frame)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
