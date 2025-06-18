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

# Morfolojik işlemler için kernel
kernel = np.ones((5, 5), np.uint8)

# Erozyon işlemi
erosion = cv2.erode(thresh, kernel, iterations=1)

# Genişletme işlemi (Dilate)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Açma işlemi (Opening) için iterasyon sayısı
opening_iterations = 2
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=opening_iterations)

# Kapanma işlemi (Closing) için iterasyon sayısı
closing_iterations = 3
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=closing_iterations)

# Görüntüleri ve işlemlerin sonuçlarını yan yana göster
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Orijinal görüntü
axs[0, 0].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Erozyon işlemi sonucu
axs[0, 1].imshow(erosion, cmap='gray')
axs[0, 1].set_title('Erosion')
axs[0, 1].axis('off')

# Genişletme işlemi sonucu
axs[0, 2].imshow(dilation, cmap='gray')
axs[0, 2].set_title('Dilation')
axs[0, 2].axis('off')

# Açma işlemi sonucu
axs[1, 0].imshow(opening, cmap='gray')
axs[1, 0].set_title('Opening ({} iterations)'.format(opening_iterations))
axs[1, 0].axis('off')

# Kapanma işlemi sonucu
axs[1, 1].imshow(closing, cmap='gray')
axs[1, 1].set_title('Closing ({} iterations)'.format(closing_iterations))
axs[1, 1].axis('off')

# Otsu eşikleme sonucu
axs[1, 2].imshow(thresh, cmap='gray')
axs[1, 2].set_title('Otsu Thresholding')
axs[1, 2].axis('off')

plt.show()





