import cv2
import numpy as np

# Görüntüyü belirtilen dosya yoluna kaydetmek için bir fonksiyon tanımlanır
def kaydet(path, image, jpg_kalite=None, png_compress=None):

    # Eğer jpeg kalitesi belirtilmişse, belirtilen kaliteyle JPEG olarak kaydedilir
    if jpg_kalite:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_kalite])
    # Eğer png sıkıştırması belirtilmişse, belirtilen sıkıştırma seviyesiyle PNG olarak kaydedilir
    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compress])
    # Eğer herhangi bir kalite veya sıkıştırma belirtilmemişse, varsayılan olarak kaydedilir
    else:
        cv2.imwrite(path, image)

# Ana fonksiyon tanımlanır
def main():
    # Giriş görüntüsünün dosya yolu belirlenir
    impath = "cicek.png"
    # Giriş görüntüsü OpenCV ile yüklenir
    img = cv2.imread(impath)

    # Giriş görüntüsü ekranda gösterilir
    cv2.imshow('Cicek', img)

    # JPEG formatında kaydedilecek dosyanın adı belirlenir ve kaydedilir
    cikis_jpeg = "cicek2JPG.jpg"
    kaydet(cikis_jpeg, img, jpg_kalite=60)

    # PNG formatında kaydedilecek dosyanın adı belirlenir ve kaydedilir
    cikis_png = "cicek2PNG.png"
    kaydet(cikis_png, img, png_compress=3)

    # Bir tuşa basılana kadar beklenir ve tüm pencereler kapatılır
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ana fonksiyon çağırılır
if __name__ == "__main__":
    main()
