# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:12:38 2024

@author: muozi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü oku
img = cv2.imread("Top_bottom_img.png")

# Tophat için disk şeklinde bir kernel tanımla
tophat_kernel_size = 30
tophat_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (tophat_kernel_size, tophat_kernel_size))

# Bottomhat için dikdörtgen şeklinde bir kernel tanımla
bottomhat_kernel_size = 100
bottomhat_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (bottomhat_kernel_size, bottomhat_kernel_size))

# Tophat işlemi
tophat_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, tophat_kernel)

# Bottomhat işlemi
bottomhat_img = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, bottomhat_kernel)

# Görüntüleri ve işlem sonuçlarını yan yana göster
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Orijinal görüntü
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')

# Tophat işlemi sonucu
axs[1].imshow(cv2.cvtColor(tophat_img, cv2.COLOR_BGR2RGB))
axs[1].set_title('Tophat')
axs[1].axis('off')

# Bottomhat işlemi sonucu
axs[2].imshow(cv2.cvtColor(bottomhat_img, cv2.COLOR_BGR2RGB))
axs[2].set_title('Bottomhat')
axs[2].axis('off')

plt.show()

