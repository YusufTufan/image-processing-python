# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:19:18 2024

@author: muozi
"""

import cv2
import matplotlib.pyplot as plt

# Webcam'den görüntü yakalama cihazını başlat
cap = cv2.VideoCapture(0)

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
    
    # Canny kenar dedektörünü kullanarak kenarları tespit et
    kenarlar = cv2.Canny(gray, 50, 150)
    
    # Görüntüyü görselleştir
    plt.clf()  # Önceki çizimleri temizle
    
    # Orijinal resmi ilk subplot'a ekle
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap='gray')
    plt.title('Orijinal Resim')

    # Canny kenarlarını ikinci subplot'a ekle
    plt.subplot(1, 2, 2)
    plt.imshow(kenarlar, cmap='gray')
    plt.title('Canny Kenarlar')

    plt.pause(0.001)  # Her iterasyonda güncelleme yapmak için kısa bir süre beklet

    # 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video yakalama cihazını ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
