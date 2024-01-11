import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

cap = cv.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection
reconhecedor = reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Captura cada frame
    ret, frame = cap.read()
    
    # controle de erro de captura
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    lista_rostos = reconhecedor.process(frame)
    
    if lista_rostos.detections:
        cv.putText(frame, "Aperte Espaco", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
    #    for rostos in lista_rostos.detections:
    #        desenho.draw_detection(frame,rostos)
            
    # Display the resulting frame
    cv.imshow('frame', frame)
    
    key = cv.waitKey(1)
    if key == ord(' ') and lista_rostos.detections:
        cv.imwrite("fotoTeste.png", frame)
    if key == 27:
        break
    
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()