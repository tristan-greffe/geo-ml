#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import argparse
import time
import numpy as np

from dataset import load_data

# Définit les paramètres de la ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('--classifier', '-c', choices=['lbp','eigen','fisher'], default='lbp')
args = parser.parse_args()

print(args.classifier)

# Créer le détecteur de visage
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Charger les données de training et de test
(X_train, y_train), (X_test, y_test) = load_data(face_cascade)

if args.classifier in ['eigen','fisher']:
    # Redimensionner les images
    X_train = [cv2.resize(img, (128, 128)) for img in X_train]
    X_test = [cv2.resize(img, (128, 128)) for img in X_test]

# Créer l'opérateur de reconnaissance faciale
if args.classifier == 'lbp':
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
elif args.classifier == 'eigen':
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
elif args.classifier == 'fisher':
    face_recognizer = cv2.face.FisherFaceRecognizer_create()

# Entrainer la reconnaissance faciale sur le set de training
start = time.time()
face_recognizer.train(X_train, np.array(y_train))
end = time.time()
print('Durée de training:{}s'.format(end - start))

# Evaluer la reconnaissance faciale sur le set de test
accuracy = 0
prediction_time = 0
for i, test_img in enumerate(X_test):
    start = time.time()
    y_pred, confidence = face_recognizer.predict(test_img)
    end = time.time()
    prediction_time += (end - start)
    if y_pred == y_test[i]:
        accuracy += 1
        
accuracy = accuracy / len(X_test)
print('Précision: {:.4f}'.format(accuracy))
prediction_time = prediction_time / len(X_test)
print('Durée moyenne de prédiction:{}s'.format(prediction_time))

        