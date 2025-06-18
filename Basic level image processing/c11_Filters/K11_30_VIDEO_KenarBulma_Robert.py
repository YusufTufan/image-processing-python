# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:10:58 2024

@author: muozi
"""

import cv2
from matplotlib import pyplot as plt

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture("Video_Trafic.mp4")

# Tek bir figür oluştur
plt.figure(figsize=(10, 10))

while True:
    # Kameradan bir kareyi yakala
    ret, frame = cap.read()
    
    # Eğer kare yakalanamadıysa döngüyü kır
    if not ret:
        break
    
    # Kareyi siyah beyaz olarak dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Sobel kenar tespiti uygula
    sobelx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=3)
    
    # Sobel kenarlarını birleştir
    sobel_OR = cv2.bitwise_or(sobelx, sobely)
    
    # Görüntüleri tek bir figürde göster
    plt.clf()
    plt.subplot(2, 2, 1), plt.imshow(gray, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobel_OR, cmap='gray')
    plt.title('Sobel OR'), plt.xticks([]), plt.yticks([])

    plt.pause(0.001)  # Her iterasyonda güncelleme yapmak için kısa bir süre beklet

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()

