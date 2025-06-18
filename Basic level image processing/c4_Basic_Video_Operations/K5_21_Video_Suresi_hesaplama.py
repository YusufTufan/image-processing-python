# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:20:52 2024

@author: muozi
"""

import cv2

# Video dosyasını aç
video = cv2.VideoCapture('Video_Trafic.mp4')

# Başlangıç zamanını al
baslangic_zamani = cv2.getTickCount()

while True:
    # Kareyi yakala
    ret, kare = video.read()

    # Videonun sonuna gelindiğinde döngüyü sonlandır
    if not ret:
        # Video bitiş zamanını al
        bitis_zamani = cv2.getTickCount()
        
        # Geçen süreyi hesapla ve milisaniye cinsine çevir
        gecen_sure_ms = (bitis_zamani - baslangic_zamani) / cv2.getTickFrequency() * 1000

        # Geçen süreyi saniye cinsine çevir
        gecen_sure_sn = gecen_sure_ms / 1000
        
        print(f"Toplam video süresi: {gecen_sure_sn:.2f} s ({gecen_sure_ms:.2f} ms)")
        
        break

    # Geçen süreyi hesapla ve milisaniye cinsine çevir
    gecen_sure_ms = (cv2.getTickCount() - baslangic_zamani) / cv2.getTickFrequency() * 1000

    # Geçen süreyi saniye cinsine çevir
    gecen_sure_sn = gecen_sure_ms / 1000

    # Geçen süreyi ekrana yazdır
    cv2.putText(kare, f'Gecen Sure: {gecen_sure_sn:.2f} s ({gecen_sure_ms:.2f} ms)', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Kareyi göster
    cv2.imshow('Video', kare)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(25) & 0xFF == ord('q'):
        print(f"Mevcut süre: {gecen_sure_sn:.2f} s ({gecen_sure_ms:.2f} ms)")
        break

# Videoyu serbest bırak
video.release()

# Pencereleri kapat
cv2.destroyAllWindows()
