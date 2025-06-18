# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:29:22 2025

@author: muozi
"""

import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO('best_egg3.pt')  # yolov8 formatında olmalı

# Video kaynağını aç
video_path = 'Conveyor1_egg.mp4'
cap = cv2.VideoCapture(video_path)

# Video düzgün açılmış mı kontrol et
if not cap.isOpened():
    print("Video açılamadı!")
    exit()

# Her kareyi işle
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü yarı boyuta küçült
    frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

    # YOLO ile tahmin
    results = model(frame)[0]

    # Tahminleri çiz
    annotated_frame = results.plot()

    # Görüntüyü göster
    cv2.imshow("Yumurta Tespiti", annotated_frame)

    # Çıkmak için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
