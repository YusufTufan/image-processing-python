# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:02:46 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture('Video_Trafic.mp4')

# Video kaydetmek için VideoWriter nesnesi oluştur
fourcc = cv2.VideoWriter_fourcc(*'XVID')
kayit = None
kayit_basladi = False

while kamera.isOpened():
    # Kameradan bir video karesi oku
    ret, video = kamera.read()
    
    # Video başarılı bir şekilde okunmuşsa
    if ret:
        # 'q' tuşuna basıldığında kayıt işlemine başla veya durdur
        tus = cv2.waitKey(1) & 0xFF
        if tus == ord('q'):
            if not kayit_basladi:
                kayit_basladi = True
                kayit = cv2.VideoWriter('kayit.mp4', fourcc, 20.0, (video.shape[1], video.shape[0]))
            else:
                kayit_basladi = False
                kayit.release()
                kayit = None
        
        # Eğer kayıt başladıysa, videoyu kayıt dosyasına yaz
        if kayit_basladi and kayit is not None:
            kayit.write(video)
        
        # Okunan videoyu göster
        cv2.imshow('kayit', video)
        
    else:
        break

# Kamera nesnesini serbest bırak
kamera.release()

# Kayıt nesnesini serbest bırak ve kayıt dosyasını kapat
if kayit is not None:
    kayit.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()

        

