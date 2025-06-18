# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:00:25 2024

@author: muozi
"""

import cv2

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Mean (ortalama) filtresini uygula
    blur = cv2.blur(frame, (25, 25))  # (7, 7) boyutlu bir filtre kullanılıyor

    # Orijinal ve filtrelenmiş görüntüleri göster
    cv2.imshow("original", frame)
    cv2.imshow("blur", blur)

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
