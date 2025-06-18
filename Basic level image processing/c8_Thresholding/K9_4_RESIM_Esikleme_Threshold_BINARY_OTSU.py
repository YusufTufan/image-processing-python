
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi oku
img1 = cv2.imread('Resim1_Dort_Nohut.png')
#img1 = cv2.imread('Resim2_Coklu_Bugday.png')

# Gri tonlamaya çevir
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Otsu eşikleme işlemi uygula (cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret1, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gri seviye resmin histogramını hesapla
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogramı çiz
plt.plot(hist, color='b')
plt.title('Gri Seviye Histogram')
plt.show()

# Resimleri göster
cv2.imshow("RENKLI", img1)
cv2.imshow("GRAY", img)
cv2.imshow("OTSU_THRESHOLD", thresh1)

# Bekle ve ekrandan çık
cv2.waitKey(0)
cv2.destroyAllWindows()



