# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:42:04 2025

@author: muozi
"""

import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO("best_egg3.pt")

# Video dosyasını aç
cap = cv2.VideoCapture("Conveyor1_egg.mp4")

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break

    # Kareyi yarı boyuta küçült
    im0 = cv2.resize(im0, (im0.shape[1] // 2, im0.shape[0] // 2))

    # YOLO ile tahmin yap
    results = model.predict(im0, show=False)

    # Her tespit edilen kutuyu bulanıklaştır
    for box in results[0].boxes.xyxy.cpu().tolist():
        x1, y1, x2, y2 = map(int, box)
        obj = im0[y1:y2, x1:x2]
        im0[y1:y2, x1:x2] = cv2.blur(obj, (50, 50))

    # Ekranda göster
    cv2.imshow("YOLO - Bulanıklaştırılmış Tespitler", im0)

    # 'q' tuşu ile çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
