# OpenCV, numpy ve matplotlib kütüphanelerini içe aktarılır
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Kenar çerçeveleme için kullanılacak mavi rengi tanımlar
mavi = [255, 0, 0]

# 'bee.jpg' adlı bir görüntü dosyası OpenCV ile yüklenir
img = cv2.imread('opencv.JPG')

# Farklı kenar çerçeveleme yöntemlerini uygulayarak çerçevelenmiş görüntüler oluşturulur
# cv2.copyMakeBorder() fonksiyonu kullanılır
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=mavi)

# Görüntüleri görselleştirmek için 6 adet alt grafik oluşturulur
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('Orijinal')  # Orijinal görüntü
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('Replicate')  # Replicate kenar çerçeveleme
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('Reflect')  # Reflect kenar çerçeveleme
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('Reflect101')  # Reflect101 kenar çerçeveleme
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('Wrap')  # Wrap kenar çerçeveleme
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('Constant')  # Constant kenar çerçeveleme

# Oluşturulan alt grafiklerin görüntülenmesi
plt.show()

# Bir tuşa basılana kadar bekler ve ardından tüm pencereleri kapatır
cv2.waitKey(0)
cv2.destroyAllWindows()

