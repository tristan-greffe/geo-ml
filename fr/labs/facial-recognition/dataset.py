import os
import sys
import numpy as np
from PIL import Image

def _extract_face(filepath, face_cascade):
	"""Extrait la zone du visage depuis filepath en utilisant face_cascade
	
	Args:
		filepath (str): chemin du fichier image
		face_cascade (cv2.CascadeClassifier): classificateur en cascade pour des visages
	
	Returns:
		ndarray: zone ou région du visage
	"""

	# charge une image et convertit en array numpy
	img = Image.open(filepath).convert('L')
	img = np.array(img, np.uint8)

	# exécute la détection de visage avec les paramètres par défaut
	face = face_cascade.detectMultiScale(img)

	# quitte s'il n'y a pas exactement un visage
	if len(face) != 1:
		sys.exit("Exemple {} n'a pas exactement un visage!".format(filepath))

	# extrait le visage de l'image
	face = face[0]
	x, y, w, h = face
	face_region = img[y:y+h,x:x+w]
	return face_region

def load_data(face_cascade, data_dir='yalefaces'):
	"""Charge les données de training et de testing
	
	Args:
		face_cascade (cv2.CascadeClassifier): classificateur en cascade pour des visages
		data_dir (str, optional): par défaut 'yalefaces'. dossier des données
	
	Returns:
		(X_train, y_train), (X_test, y_test): données de training et de testing
	"""

	X_train = []
	y_train = []

	X_test = []
	y_test = []

	# sépare les fichiers en sets de training et de testing
	training_image_files = [f for f in os.listdir(data_dir) if not f.endswith('.wink')]
	test_image_files = [f for f in os.listdir(data_dir) if f.endswith('.wink')]

	# construit le set de training
	for image_file in training_image_files:
		filepath = os.path.join(data_dir, image_file)

		face_region = _extract_face(filepath, face_cascade)
		person_number = int(image_file.split('.')[0].replace('subject', ''))

		X_train.append(face_region)
		y_train.append(person_number)

	# construit le set de test
	for image_file in test_image_files:
		filepath = os.path.join(data_dir, image_file)

		face_region = _extract_face(filepath, face_cascade)
		person_number = int(image_file.split('.')[0].replace('subject', ''))

		X_test.append(face_region)
		y_test.append(person_number)
	
	return (X_train, y_train), (X_test, y_test)
