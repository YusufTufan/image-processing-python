# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:29:13 2024

@author: muozi
"""

import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('chessboard.png', 0) # Grayscale olarak yükle

# Robert kenar tespiti uygula
robert_x = cv2.filter2D(image, cv2.CV_64F, np.array([[-1, 0], [0, 1]]))
robert_y = cv2.filter2D(image, cv2.CV_64F, np.array([[0, -1], [1, 0]]))
edges = cv2.magnitude(robert_x, robert_y)

# Görüntüyü ve kenarları ekranda göster
cv2.imshow('Original Image', image)
cv2.imshow('Robert Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
