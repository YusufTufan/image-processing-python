import cv2
from ultralytics import solutions

def count_specific_classes(video_path, output_video_path, model_path, classes_to_count):
    """Belirli sınıfları sayar, görüntüyü yarı boyuta düşürür, ekran ve kayıtta gösterir."""
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Video dosyası açılamadı!"

    # Orijinal boyutları al
    orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Yarı boyutlar
    w, h = orig_w // 2, orig_h // 2

    # Video kaydedici (yarı boyutlu)
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # Otomatik çizgi: dikey çizgi (video genişliğinin ortası)
    line_x = w // 2
    line_points = [(line_x, 0), (line_x, h)]

    # Sayım aracı
    counter = solutions.ObjectCounter(
        model=model_path,
        region=line_points,
        classes=classes_to_count,
        show=False
    )

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Video bitti veya kare okunamadı.")
            break

        # Boyutu yarı yarıya küçült
        frame = cv2.resize(frame, (w, h))

        # Sayım ve çizim işlemi
        frame = counter.count(frame)

        # Ekranda göster
        cv2.imshow("Yarı Boyutta Yumurta Sayımı", frame)

        # Kaydet
        video_writer.write(frame)

        # Çıkış için 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

# Kullanım
count_specific_classes(
    video_path="Conveyor1_egg.mp4",
    output_video_path="output_egg_count_half.avi",
    model_path="best_egg3.pt",
    classes_to_count=[0]  # sadece sınıf 0 sayılıyor
)
