# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:48:12 2024

@author: muozi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüleri oku
img1 = cv2.imread("j.png")
img2 = cv2.imread("j2.png")
img3 = cv2.imread("j3.png")

# Erozyon için kernel
kernel = np.ones((5, 5), np.uint8)

# Erozyon işlemi
erosion1 = cv2.erode(img1, kernel, iterations=5)
erosion2 = cv2.erode(img2, kernel, iterations=5)
erosion3 = cv2.erode(img3, kernel, iterations=5)

# Görüntüleri ve erozyona uğramış hallerini yan yana göster
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Orijinal görüntüleri göster
axs[0, 0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Orijinal Image 1')
axs[0, 0].axis('off')

axs[1, 0].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('Orijinal Image 2')
axs[1, 0].axis('off')

axs[2, 0].imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
axs[2, 0].set_title('Orijinal Image 3')
axs[2, 0].axis('off')

# Erozyona uğramış görüntüleri göster
axs[0, 1].imshow(cv2.cvtColor(erosion1, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Eroded Image 1')
axs[0, 1].axis('off')

axs[1, 1].imshow(cv2.cvtColor(erosion2, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Eroded Image 2')
axs[1, 1].axis('off')

axs[2, 1].imshow(cv2.cvtColor(erosion3, cv2.COLOR_BGR2RGB))
axs[2, 1].set_title('Eroded Image 3')
axs[2, 1].axis('off')

plt.show()