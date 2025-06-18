import numpy as np
import cv2
import matplotlib.pyplot as plt

# Resmi oku
frame = cv2.imread("coins.jpg")

# Resmi yeniden boyutlandır
frame = cv2.resize(frame, (640, 480))

# Resmi gri tonlamaya dönüştür
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Otsu eşikleme uygula
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Morfolojik işlemler için kernel boyutları
closing_kernel = np.ones((15, 15), np.uint8)
opening_kernel = np.ones((9, 9), np.uint8)

# Kapatma işlemi (Closing) uygula
closing_iterations = 3
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, closing_kernel, iterations=closing_iterations)

# Açma işlemi (Opening) uygula
opening_iterations = 2
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, opening_kernel, iterations=opening_iterations)

# Görüntüleri ve işlemlerin sonuçlarını yan yana göster
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Orijinal görüntü
axs[0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')

# Kapatma işlemi sonucu
axs[1].imshow(closing, cmap='gray')
axs[1].set_title('Closing ({} iterations)'.format(closing_iterations))
axs[1].axis('off')

# Açma işlemi sonucu
axs[2].imshow(opening, cmap='gray')
axs[2].set_title('Opening ({} iterations)'.format(opening_iterations))
axs[2].axis('off')

plt.show()


