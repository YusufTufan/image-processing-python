# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:56:21 2024

@author: muozi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüleri oku
img1 = cv2.imread("j.png")
img2 = cv2.imread("j2.png")
img3 = cv2.imread("j3.png")

# Opening işlemi için kernel
kernel = np.ones((3, 3), np.uint8)

# Iterasyon sayısı
iterations = 5

# Opening işlemi (erosion + dilation)
opening1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel, iterations=iterations)
opening2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel, iterations=iterations)
opening3 = cv2.morphologyEx(img3, cv2.MORPH_OPEN, kernel, iterations=iterations)

# Görüntüleri ve opening işlemi sonucunu yan yana göster
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

# Opening işlemi sonuçlarını göster
axs[0, 1].imshow(cv2.cvtColor(opening1, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Opening Image 1')
axs[0, 1].axis('off')

axs[1, 1].imshow(cv2.cvtColor(opening2, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Opening Image 2')
axs[1, 1].axis('off')

axs[2, 1].imshow(cv2.cvtColor(opening3, cv2.COLOR_BGR2RGB))
axs[2, 1].set_title('Opening Image 3')
axs[2, 1].axis('off')

plt.show()
