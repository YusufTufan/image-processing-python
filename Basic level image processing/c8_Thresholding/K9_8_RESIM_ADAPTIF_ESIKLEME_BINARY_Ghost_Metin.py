import cv2
import numpy as np

# Resmi oku
img = cv2.imread('Resim5_Ghost_sayfa.jpg')

# Basit thresholding
ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# Gri tonlamaya çevir
griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamada basit thresholding
ret, thresholdgri = cv2.threshold(griton, 12, 255, cv2.THRESH_BINARY)

# Adaptif thresholding (GAUSSIAN_C)
gaus = cv2.adaptiveThreshold(griton, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Otsu thresholding
ret, otsu = cv2.threshold(griton, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Görselleştirme
cv2.imshow('Orjinal', img)
cv2.imshow('Basit Thresholding', threshold)
cv2.imshow('Gri Tonlama ve Thresholding', thresholdgri)
cv2.imshow('Adaptif Thresholding (GAUSSIAN_C)', gaus)
cv2.imshow('Otsu Thresholding', otsu)

cv2.imwrite('Duzelmis_G.png',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

