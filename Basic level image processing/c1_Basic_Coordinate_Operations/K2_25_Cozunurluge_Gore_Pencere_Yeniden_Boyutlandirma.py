import cv2

def main():
    # 'cicek.png' adlı bir görüntü dosyası OpenCV ile yüklenir
    img = cv2.imread('cicek.png')
    
    # Ekran çözünürlüğü 640x480 olarak belirlenir
    ekran_cozunulurluk = 640, 480

    # Görüntünün ekran çözünürlüğüne oranını hesaplar ve bu oranı minimum olarak alır
    skala_genislik = ekran_cozunulurluk[0] / img.shape[1]
    skala_yukseklik = ekran_cozunulurluk[1] / img.shape[0]
    skala = min(skala_genislik, skala_yukseklik)

    # Yeniden boyutlandırılmış pencere boyutunu hesaplar
    pencere_genislik = int(img.shape[1] * skala)
    pencere_yukseklik = int(img.shape[0] * skala)

    # 'Boyutlanabilir Pencere' adında bir pencere oluşturur
    cv2.namedWindow('Boyutlanabilir Pencere', cv2.WINDOW_NORMAL)
    # Pencere boyutunu belirtilen genişlik ve yükseklik değerlerine ayarlar
    cv2.resizeWindow('Boyutlanabilir Pencere', pencere_genislik, pencere_yukseklik)

    # Yüklenen görüntüyü bu pencerede görüntüler
    cv2.imshow('Boyutlanabilir Pencere', img)
    
    # Bir tuşa basılana kadar bekler
    cv2.waitKey(0)
    # Tüm pencereleri kapatır
    cv2.destroyAllWindows()

# Ana fonksiyonu çağırır
if __name__ == "__main__":
    main()
