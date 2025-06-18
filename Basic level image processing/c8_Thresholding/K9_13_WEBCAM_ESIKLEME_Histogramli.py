import cv2
import numpy as np
import matplotlib.pyplot as plt

# Video dosyasını oku
cap = cv2.VideoCapture(0)

# Histogram plotlarını oluştur
plt.figure(figsize=(12, 6))
color_hist_plot = plt.subplot(2, 1, 1)
gray_hist_plot = plt.subplot(2, 1, 2)

while True:
    # Bir sonraki çerçeveyi oku
    ret, frame = cap.read()

    # Eğer çerçeve alınamazsa döngüden çık
    if not ret:
        break

    # Çerçeveyi gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gri tonlamalı çerçeve üzerine eşikleme uygula
    ret, thresh_frame = cv2.threshold(gray_frame, 100, 255, cv2.THRESH_BINARY)

    # Renkli çerçevenin histogramını hesapla ve görselleştir
    color_hist_plot.clear()
    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
        color_hist_plot.plot(hist, color=col)
    color_hist_plot.set_title('Renkli Histogram')

    # Gri tonlamalı çerçevenin histogramını hesapla ve görselleştir
    gray_hist_plot.clear()
    hist_gray = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])
    gray_hist_plot.plot(hist_gray, color='b')
    gray_hist_plot.set_title('Gri Seviye Histogram')

    # Ekrana güncellenmiş plotları göster
    plt.tight_layout()
    plt.draw()
    plt.pause(0.0005)

    # Çerçeve ve eşiklenmiş çerçeveyi göster
    cv2.imshow("Video_Trafic", frame)
    cv2.imshow("Video_Trafic_Gray", gray_frame)
    cv2.imshow("Video_Trafic_Threshold", thresh_frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Videoyı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()






