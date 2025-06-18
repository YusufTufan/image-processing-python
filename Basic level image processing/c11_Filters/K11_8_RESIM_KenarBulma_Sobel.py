# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 01:35:52 2023

@author: MUOZIC
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Resmi siyah beyaz olarak yükle
img = cv2.imread('chessboard.png', 0)

# Sobel kenar tespiti uygula
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

# sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
# sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)

# dst = cv2.Sobel(src, ddepth, dx, dy, ksize)

# src: Giriş görüntüsü.

# ddepth: Türe dönüşüm derinliği. Bu parametre, çıktı gradyan görüntüsünün veri türünü belirler.
# Genellikle cv2.CV_8U, cv2.CV_16U, cv2.CV_32F veya cv2.CV_64F gibi sabitler kullanılır. 
# Örneğin, cv2.CV_64F kullanıldığında, gradyan hesaplamaları 64-bit kayan nokta sayılarla yapılır.

# cv2.CV_8U: 8-bit işaretli tamsayılar. Bu, 0 ile 255 arasındaki tam sayıları depolamak için kullanılır. 
# Yani, her piksel 0 ile 255 arasında bir gri tonlama seviyesini temsil eder. Özellikle siyah-beyaz görüntüler için yaygın olarak kullanılır.

# cv2.CV_16U: 16-bit işaretli tamsayılar. Bu, 0 ile 65535 arasındaki tam sayıları depolamak için kullanılır. 
# Genellikle derinlik bilgisi gibi yüksek dinamik aralıklı verileri saklamak için kullanılır.

# cv2.CV_32F: 32-bit kayan noktalı sayılar. Bu, tek hassasiyetli kayan nokta sayılarını depolamak için kullanılır. 
# Özellikle görüntü işleme algoritmalarında matematiksel işlemler yapılırken daha yüksek hassasiyet gerektiren durumlarda kullanılır.

# cv2.CV_64F: 64-bit kayan noktalı sayılar. Bu, çift hassasiyetli kayan nokta sayılarını depolamak için kullanılır. 
# Daha yüksek hassasiyet gerektiren uygulamalarda kullanılır, ancak daha fazla bellek kullanımı gerektirir.

# Hangi derinlik tipini seçeceğiniz, uygulamanın gereksinimlerine, bellek kullanımına ve hesaplama hassasiyetine bağlıdır. 
# Örneğin, genellikle hesaplama hızı daha önemliyse 8-bit tamsayılar tercih edilirken, 
# daha yüksek hassasiyet gerekiyorsa 32-bit veya 64-bit kayan noktalı sayılar kullanılabilir.

# dx: x yönündeki gradyan derecesi (x yönlü türev). 1, x yönünde birinci dereceden türev alınacağını belirtir.

# dy: y yönündeki gradyan derecesi (y yönlü türev). 0, y yönünde birinci dereceden türev alınmayacağını belirtir.

# ksize: Her iki yönde de Sobel kernel boyutu. 
# Varsayılan olarak 3'tür, ancak bu parametre isteğe bağlıdır. 
# Genellikle 3, 5 veya 7 gibi tek sayılar kullanılır.

# Sobel kenarlarını birleştir
sobel_OR = cv2.bitwise_or(sobelx, sobely)

# Görüntüleri görselleştir
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(sobel_OR, cmap='gray')
plt.title('Sobel OR'), plt.xticks([]), plt.yticks([])

plt.show()
