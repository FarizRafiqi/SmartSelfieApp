# import cv2
# import datetime
# # import simpleaudio as sa
# import time

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# # Inisialisasi variabel untuk melacak jumlah foto yang diambil
# photo_count = 0

# while True:
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)

#     _, frame = cap.read()
#     original_frame = frame.copy()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     face = face_cascade.detectMultiScale(gray, 1.3, 5)

#     # wave_obj = sa.WaveObject.from_wave_file('camera_click.wav')

#     for x, y, w, h in face:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
#         face_roi = frame[y:y + h, x:x + w]
#         gray_roi = gray[y:y + h, x:x + w]
#         smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 5)
                                               
#         for x1, y1, w1, h1 in smile:
#             cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            
#             if photo_count < 3:
#                 # Menampilkan countdown selama 3 detik sebelum mengambil foto
#                 for i in range(3, 0, -1):
#                     frame_with_text = frame.copy()
#                     cv2.putText(frame_with_text, f"Foto dalam {i}", (20, 30),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
#                     cv2.imshow('Smile Detection', frame_with_text)
#                     cv2.waitKey(1000)  # Delay 1 
                    
#                 # Mengambil foto
#                 time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#                 file_name = f'my_photos/selfie-{time_stamp}.png'
#                 cv2.imwrite(file_name, original_frame)
#                 # play_obj = wave_obj.play()
#                 # play_obj.wait_done()
                
#                 photo_count += 1

#     cv2.imshow('Smile Detection', frame)

#     if cv2.waitKey(10) == ord('q') or photo_count == 3:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import datetime
import simpleaudio as sa
import time

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Inisialisasi variabel untuk melacak jumlah foto yang diambil
photo_count = 0

# Membuat jendela dengan ukuran khusus
cv2.namedWindow('Smile Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Smile Detection', 400, 300)

while True:
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    wave_obj = sa.WaveObject.from_wave_file('camera_click.wav')

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y + h, x:x + w]
        gray_roi = gray[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 35)

        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            
            if photo_count < 3:
                # Menampilkan countdown selama 3 detik sebelum mengambil foto
                for i in range(3, 0, -1):
                    frame_with_text = frame.copy()
                    cv2.putText(frame_with_text, f"Foto dalam {i}", (20, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.imshow('Smile Detection', frame_with_text)
                    cv2.waitKey(1000)  # Delay 1 
                    
                # Mengambil foto
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                file_name = f'my_photos/selfie-{time_stamp}.png'
                cv2.imwrite(file_name, original_frame)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                
                photo_count += 1

    cv2.imshow('Smile Detection', frame)

    if cv2.waitKey(10) == ord('q') or photo_count == 3:
        break

cap.release()
cv2.destroyAllWindows()