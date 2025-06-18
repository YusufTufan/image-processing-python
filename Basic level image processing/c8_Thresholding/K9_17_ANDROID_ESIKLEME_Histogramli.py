import numpy as np
import os
import cv2
import requests
import matplotlib.pyplot as plt

url = "http://10.156.63.132:8080//shot.jpg"

# Histogram plotlarını oluştur
plt.figure(figsize=(12, 6))
color_hist_plot = plt.subplot(2, 1, 1)
gray_hist_plot = plt.subplot(2, 1, 2)

while True:
    # Kameradan görüntüyü al
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    image = cv2.resize(img, (960, 540))
    
    # Gri tonlamaya çevir
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Basit thresholding uygula
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Renkli çerçevenin histogramını hesapla ve görselleştir
    color_hist_plot.clear()
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        color_hist_plot.plot(hist, color=col)
    color_hist_plot.set_title('Renkli Histogram')

    # Gri tonlamalı çerçevenin histogramını hesapla ve görselleştir
    gray_hist_plot.clear()
    hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
    gray_hist_plot.plot(hist_gray, color='b')
    gray_hist_plot.set_title('Gri Seviye Histogram')

    # Ekrana güncellenmiş plotları göster
    plt.tight_layout()
    plt.draw()
    plt.pause(0.0005)

    # Eşiklenmiş görüntüyü göster
    cv2.imshow("Android", image)
    cv2.imshow("Binary Thresholding", thresh)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    