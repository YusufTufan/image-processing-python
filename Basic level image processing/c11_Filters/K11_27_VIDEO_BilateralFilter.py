# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:06:55 2024

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
    
    # Bilateral filtre uygula
    blur = cv2.bilateralFilter(frame, 9, 75, 75)

    # Orijinal ve Bilateral filtreli görüntüleri göster
    cv2.imshow("original", frame)
    cv2.imshow("Bilateral Blur", blur)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
