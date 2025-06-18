# -*- coding: utf-8 -*-
"""
Created on Thu May 22 07:45:18 2025

@author: muozi
"""

import cv2
from ultralytics import solutions

# Video giriş dosyası
cap = cv2.VideoCapture("Conveyor1_egg.mp4")
assert cap.isOpened(), "Video dosyası açılamadı!"

# Orijinal boyutları al
orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Yarı boyutlar
w, h = orig_w // 2, orig_h // 2

# Video kaydedici
video_writer = cv2.VideoWriter("region_counting_half.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Küçültülmüş videoya uygun region tanımları (yeniden ayarlandı)
region_points = {
    "region-01": [(25, 25), (125, 25), (125, 125), (25, 125)],
    "region-02": [(320, 320), (390, 320), (390, 360), (320, 360)],
}

# RegionCounter nesnesi
region = solutions.RegionCounter(
    show=False,  # Biz göstereceğiz
    region=region_points,
    model="best_egg3.pt"
)

# Video karelerini işle
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video bitti veya kare okunamadı.")
        break

    # Görüntüyü yarı boyuta küçült
    im0 = cv2.resize(im0, (w, h))

    # Bölge bazlı sayım
    im0 = region.count(im0)

    # Ekranda göster
    cv2.imshow("Bölge Sayımı (Yarı Boyut)", im0)

    # Kaydet
    video_writer.write(im0)

    # 'q' ile çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Temizlik
cap.release()
video_writer.release()
cv2.destroyAllWindows()
