# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:47:45 2024

@author: muozi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Bugday.png', 0)

min_val = np.min(image)
max_val = np.max(image)

stretched_image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

stretched_image2 = cv2.normalize(image, None, alpha=100, beta=200, norm_type=cv2.NORM_MINMAX)

original_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
stretched_hist = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])
stretched_hist2 = cv2.calcHist([stretched_image2], [0], None, [256], [0, 256])


# Orijinal histogramı göster
plt.figure()
plt.plot(original_hist, color='blue')
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

# Gerilmiş histogramı göster
plt.figure()
plt.plot(stretched_hist, color='red')
plt.title('Stretched Histogram 0-255')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

# Gerilmiş histogramı göster
plt.figure()
plt.plot(stretched_hist2, color='green')
plt.title('Stretched Histogram 100-200')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()

cv2.imshow("image", image)
cv2.imshow("stretched_image 0-255", stretched_image)
cv2.imshow("stretched_image2 100-200", stretched_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()