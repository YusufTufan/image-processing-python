# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:26:16 2024

@author: muozi
"""


# SATIR VE SÜTUN ŞEKLİNDE DEĞİL GENİŞLİK VE YÜKSEKLİK OLARAK PARAMETRE GİRİLİR
# DOLAYISIYLA SÜTUN VE SATIR SIRASIYLA GİRİLECEK


import cv2

# 'bee.jpg' adlı bir görüntü dosyası OpenCV ile yüklenir
img = cv2.imread('bee.jpg')

# Renkli olarak yüklenen görüntü ekranda gösterilir
cv2.imshow('bee', img)

# 'bee.jpg' adlı bir görüntü dosyası gri tonlamalı olarak yüklenir
img1 = cv2.imread('bee.jpg', 0)

# Gri tonlamalı olarak yüklenen görüntü ekranda gösterilir
cv2.imshow('bee1', img1)

# Yeniden boyutlandırılacak görüntü 'img' olarak belirlenir ve boyutları (1920, 1080) olarak ayarlanır
# SATIR VE SÜTUN ŞEKLİNDE DEĞİL GENİŞLİK VE YÜKSEKLİK OLARAK PARAMETRE GİRİLİR
# DOLAYISIYLA SÜTUN VE SATIR SIRASIYLA GİRİLECEK
img_coz = cv2.resize(img, (1920, 1080))

# Yeniden boyutlandırılan görüntü ekranda gösterilir
cv2.imshow('img_coz', img_coz)

# Orijinal renkli görüntünün boyutu ve yeniden boyutlandırılmış görüntünün boyutu ekrana yazdırılır
print("Renkli Görüntü Boyutu: " + str(img.shape))
print("Yeniden Boyutlandırılmış Görüntü Boyutu: " + str(img_coz.shape))

# Bir tuşa basılana kadar beklenir ve tüm pencereler kapatılır
cv2.waitKey(0)
cv2.destroyAllWindows()

