#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

from dataset import load_data

# Créer le détecteur de visage et charger les données
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
(X_train, y_train), (X_test, y_test) = load_data(face_cascade)

# Création et entrainement de notre opérateur de reconnaissance faciale
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(X_train, np.array(y_train))

# Ouvrir la webcam
video_capture = cv2.VideoCapture(0)
while True:
    # Obtenir une image depuis la webcam
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # On applique la détection de visage sur cette image
    faces = face_cascade.detectMultiScale(gray)
    for face in faces:
        # extraire le visage de la fenêtre
        x, y, w, h = face
        face_region = gray[y:y+h, x:x+w]
        
        # exécuter la reconnaissance faciale
        predicted_person, _ = face_recognizer.predict(face_region)
        
        # dessiner un rectangle sur la vidéo
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(predicted_person), (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255))
    
    # Afficher l'image annotée
    cv2.imshow('Reconnaissance faciale', frame)
    
    # Quitter l'application
    if cv2.waitKey(1) == ord('q'):
        break
# Fin de la boucle    

# Fermer la webcam
video_capture.release()
cv2.destroyAllWindows()




