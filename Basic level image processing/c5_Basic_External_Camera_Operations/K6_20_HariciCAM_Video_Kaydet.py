# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:02:46 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(2)

# Video kaydetmek için VideoWriter nesnesi oluştur
fourcc = cv2.VideoWriter_fourcc(*'XVID')
kayit = cv2.VideoWriter('kayit.avi', fourcc, 20.0, (640, 480))

while kamera.isOpened():
    # Kameradan bir video karesi oku
    ret, video = kamera.read()
    
    # Video başarılı bir şekilde okunmuşsa
    if ret:
        # Videoyu kayıt dosyasına yaz
        kayit.write(video)
        
        # Okunan videoyu göster
        cv2.imshow('kayit', video)
        
        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Kamera ve kayıt nesnelerini serbest bırak
kamera.release()
kayit.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()
