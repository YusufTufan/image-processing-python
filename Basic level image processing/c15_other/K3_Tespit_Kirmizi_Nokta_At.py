# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:32:48 2025

@author: muozi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  5 19:00:40 2025
@author: muozi
"""

import cv2
from ultralytics import YOLO

# YOLO modelini yükle
model = YOLO('best_egg3.pt')  # YOLOv8 formatında olmalı

# Video dosyasını aç
video_path = 'Conveyor1_egg.mp4'
cap = cv2.VideoCapture(video_path)

# Video düzgün açılmış mı kontrol et
if not cap.isOpened():
    print("Video açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü yarı boyuta küçült
    frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

    # YOLO ile tespit yap
    results = model(frame)[0]

    # Her tespit edilen nesne için kırmızı bir nokta çiz
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # kutunun köşe koordinatları
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        # Noktayı çiz
        cv2.circle(frame, (center_x, center_y), radius=5, color=(0, 0, 255), thickness=-1)

    # Son görüntüyü göster
    cv2.imshow("Yumurta Tespiti (Kırmızı Noktalar)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
