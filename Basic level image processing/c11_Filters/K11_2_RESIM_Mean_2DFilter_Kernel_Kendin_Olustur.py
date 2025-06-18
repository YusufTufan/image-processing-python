# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:04:27 2024

@author: muozi
"""

import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread("Resim17_Bitewing1.jpg")

# Mean (ortalama) filtresi çekirdeğini tanımla
kernel_size = 7
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

print(kernel)

# Filtreyi uygula

filtered_image = cv2.filter2D(image, -1, kernel)

# -1 kullanıldığında, hedef görüntünün bit derinliğinin giriş görüntüsüyle aynı olacağı anlamına gelir. 
# -1 yerine kullanılabilecek giriş parametreleri
# cv2.CV_8U: 8-bit işaretli tamsayılar (0-255 aralığında).
# cv2.CV_8S: 8-bit işaretli tamsayılar (-128 ile 127 arasında).
# cv2.CV_16U: 16-bit işaretli tamsayılar (0-65535 aralığında).
# cv2.CV_16S: 16-bit işaretli tamsayılar (-32768 ile 32767 arasında).
# cv2.CV_32F: 32-bit kayan noktalı sayılar.
# cv2.CV_64F: 64-bit kayan noktalı sayılar.

# Görüntüyü ekranda göster
cv2.imshow("Original Image", image)
cv2.imshow("Mean Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
