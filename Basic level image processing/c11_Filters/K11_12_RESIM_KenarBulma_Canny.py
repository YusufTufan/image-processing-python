import cv2
import matplotlib.pyplot as plt

# Resmi siyah-beyaz olarak yükle
img = cv2.imread('Resim7_Fasulye.png', 0)

# Canny kenar dedektörünü kullanarak kenarları tespit et
kenarlar = cv2.Canny(img, 50, 200)

# İlk parametre (50), kenarlar tespit edilirken kullanılan alt eşik değeridir. 
# Eşik değerinden düşük olan gradyanlar genellikle kenarlar olarak kabul edilmez.

# İkinci parametre (200), kenarlar tespit edilirken kullanılan üst eşik değeridir. 
# Eşik değerinden yüksek olan gradyanlar kesinlikle kenarlar olarak kabul edilir.

# Bu eşik değerlerinin seçimi, uygulamanın gereksinimlerine ve işlenen görüntünün özelliklerine bağlıdır. 
# Düşük eşik değeri, daha fazla kenar tespitine ve daha fazla yanıltıcı kenarlar içermesine neden olabilirken, 
# yüksek eşik değeri daha kesin ancak daha az kenar tespitine neden olabilir. 
# Önerilen bir yaklaşım, farklı eşik değerleriyle deney yapmaktır ve en iyi sonucu veren değerleri seçmektir. 
# Bu nedenle, genellikle kenar tespiti uygulamasında kullanılacak eşik değerleri, önceden belirlenmiş deneme yanılma yoluyla belirlenir.

# Orijinal ve Canny kenarlarını göstermek için iki yan yana subplot oluştur
plt.figure(figsize=(10, 5))

# Orijinal resmi ilk subplot'a ekle
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Resim')

# Canny kenarlarını ikinci subplot'a ekle
plt.subplot(1, 2, 2)
plt.imshow(kenarlar, cmap='gray')
plt.title('Canny Kenarlar')

# Görüntüleri göster
plt.show()

# Orijinal ve Canny kenarlarını göster
cv2.imshow("original", img)
cv2.imshow("Canny Kenarlar", kenarlar)

# Kullanıcı bir tuşa basana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()