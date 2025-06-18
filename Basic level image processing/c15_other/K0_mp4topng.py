# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:51:15 2024

@author: muozi
"""

import cv2
import os

# Video dosyasının yolunu belirtin
video_path = "Conveyor2_sise.mp4"  # Video dosyasının yolu
output_folder = "frames_output_bottle"        # Frame'lerin kaydedileceği klasör

# Çıkış klasörünü oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Video dosyasını aç
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video açılamadı. Lütfen yolu kontrol edin.")
    exit()

frame_count = 0  # Frame sayacını başlat

# Video karelerini oku ve PNG olarak kaydet
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Tüm kareler işlendi veya video okunamadı.")
        break
    
    # Frame'i PNG formatında kaydet
    output_path = os.path.join(output_folder, f"frame_{frame_count:05d}.png")
    cv2.imwrite(output_path, frame)
    print(f"Kayıt edildi: {output_path}")
    
    frame_count += 1

# Video dosyasını kapat
cap.release()
print(f"Tüm kareler başarıyla kaydedildi. Toplam {frame_count} frame işlendi.")
