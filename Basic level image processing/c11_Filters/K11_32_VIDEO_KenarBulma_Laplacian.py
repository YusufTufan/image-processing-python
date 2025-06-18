# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:17:50 2024

@author: muozi
"""

import cv2
from matplotlib import pyplot as plt

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture("Video_Trafic.mp4")


# Tek bir figür oluştur
plt.figure(figsize=(10, 5))

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Kareyi siyah beyaz olarak dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Laplacian kenar tespiti uygula
    laplacian = cv2.Laplacian(gray, cv2.CV_8U)
    
    # Görüntüyü görselleştir
    plt.clf()  # Önceki çizimleri temizle
    
    plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    plt.pause(0.001)  # Her iterasyonda güncelleme yapmak için kısa bir süre beklet

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
