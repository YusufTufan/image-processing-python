



import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resim2_Coklu_Bugday.png', 0)

# Görüntünün histogramını hesapla
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogram eşitleme işlemi
equ = cv2.equalizeHist(img)

# Eşitlenmiş görüntünün histogramını hesapla
hist2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

# İşlenmiş görüntüleri görselleştirme
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Gri Seviye Görüntü')

plt.subplot(2, 2, 2)
plt.plot(hist, color='b')
plt.title('Orijinal Gri Seviye Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equ, cmap='gray')
plt.title('Histogram Eşitleme Sonrası Görüntü')

plt.subplot(2, 2, 4)
plt.plot(hist2, color='b')
plt.title('Histogram Eşitleme Sonrası Histogram')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()