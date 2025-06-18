# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:47:10 2025

@author: muozi
"""

import cv2
from ultralytics import solutions

# Video giriş dosyası
cap = cv2.VideoCapture("Conveyor1_egg.mp4")
assert cap.isOpened(), "Video dosyası açılamadı!"

# Orijinal boyutlar
orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Yarı boyut
w, h = orig_w // 2, orig_h // 2

# Video kaydedici
video_writer = cv2.VideoWriter("region_counting_half.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Merkeze yerleştirilecek bölge boyutları
box1_width, box1_height = 100, 100
box2_width, box2_height = 70, 40

# Merkezden kutuları oluştur
region_points = {
    "region-01": [
        (w // 2 - box1_width // 2, h // 2 - box1_height // 2),
        (w // 2 + box1_width // 2, h // 2 - box1_height // 2),
        (w // 2 + box1_width // 2, h // 2 + box1_height // 2),
        (w // 2 - box1_width // 2, h // 2 + box1_height // 2),
    ],
    "region-02": [
        (w // 2 - box2_width // 2, h // 2 + box1_height // 2 + 10),  # 10px boşlukla alta yerleştirdik
        (w // 2 + box2_width // 2, h // 2 + box1_height // 2 + 10),
        (w // 2 + box2_width // 2, h // 2 + box1_height // 2 + 10 + box2_height),
        (w // 2 - box2_width // 2, h // 2 + box1_height // 2 + 10 + box2_height),
    ],
}

# RegionCounter başlat
region = solutions.RegionCounter(
    show=False,
    region=region_points,
    model="best_egg3.pt"
)

# Video karelerini işle
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video bitti veya kare okunamadı.")
        break

    # Yarı boyuta küçült
    im0 = cv2.resize(im0, (w, h))

    # Sayım işlemi
    im0 = region.count(im0)

    # Ekranda göster
    cv2.imshow("Ortalanmış Bölgelerle Sayım", im0)

    # Kaydet
    video_writer.write(im0)

    # Çıkmak için 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
