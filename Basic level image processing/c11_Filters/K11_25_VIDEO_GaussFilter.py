# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:03:58 2024

@author: muozi
"""

import cv2

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture("Video_Trafic.mp4")

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Gauss filtresini uygula
    blur = cv2.GaussianBlur(frame, (15, 15), cv2.BORDER_DEFAULT)

    # Orijinal ve Gauss filtreli görüntüleri göster
    cv2.imshow("original", frame)
    cv2.imshow("Gaussian Blur", blur)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
