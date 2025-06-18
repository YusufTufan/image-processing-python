# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:50:26 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, orijinal_goruntu = kamera.read()

    # Görüntüyü küçült
    kucuk_goruntu = cv2.pyrDown(orijinal_goruntu)
    
    # Görüntüyü büyüt
    buyuk_goruntu = cv2.pyrUp(orijinal_goruntu)

    # Orijinal görüntü çözünürlüğünü al
    orijinal_cozunurluk = f'{orijinal_goruntu.shape[1]}x{orijinal_goruntu.shape[0]}'
    # Küçültülmüş görüntü çözünürlüğünü al
    kucuk_cozunurluk = f'{kucuk_goruntu.shape[1]}x{kucuk_goruntu.shape[0]}'
    # Büyütülmüş görüntü çözünürlüğünü al
    buyuk_cozunurluk = f'{buyuk_goruntu.shape[1]}x{buyuk_goruntu.shape[0]}'

    # Görüntülerin sol üst köşelerine çözünürlük bilgisini yaz
    cv2.putText(orijinal_goruntu, f'Cozunurluk: {orijinal_cozunurluk}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(kucuk_goruntu, f'Cozunurluk: {kucuk_cozunurluk}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(buyuk_goruntu, f'Cozunurluk: {buyuk_cozunurluk}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Görüntüleri ayrı ayrı pencerelerde göster
    cv2.imshow('Orijinal', orijinal_goruntu)
    cv2.imshow('Kucultulmus', kucuk_goruntu)
    cv2.imshow('Buyutulmus', buyuk_goruntu)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()

