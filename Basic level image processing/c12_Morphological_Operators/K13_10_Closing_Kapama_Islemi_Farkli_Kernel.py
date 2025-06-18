# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:02:44 2024

@author: muozi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüleri oku
img1 = cv2.imread("j.png")
img2 = cv2.imread("j2.png")
img3 = cv2.imread("j3.png")

# Farklı bir kernel tanımla
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], dtype=np.uint8)

# Iterasyon sayısı
iterations = 2

# Kapama işlemi (dilation + erosion)
closing1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel, iterations=iterations)
closing2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel, iterations=iterations)
closing3 = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel, iterations=iterations)

# Görüntüleri ve kapama işlemi sonucunu yan yana göster
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Orijinal görüntüleri göster
axs[0, 0].imshow(img1)
axs[0, 0].set_title('Orijinal Image 1')
axs[0, 0].axis('off')

axs[1, 0].imshow(img2)
axs[1, 0].set_title('Orijinal Image 2')
axs[1, 0].axis('off')

axs[2, 0].imshow(img3)
axs[2, 0].set_title('Orijinal Image 3')
axs[2, 0].axis('off')

# Kapama işlemi sonuçlarını göster
axs[0, 1].imshow(cv2.cvtColor(closing1, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Closing Image 1')
axs[0, 1].axis('off')

axs[1, 1].imshow(cv2.cvtColor(closing2, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Closing Image 2')
axs[1, 1].axis('off')

axs[2, 1].imshow(cv2.cvtColor(closing3, cv2.COLOR_BGR2RGB))
axs[2, 1].set_title('Closing Image 3')
axs[2, 1].axis('off')

plt.show()
