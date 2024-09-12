import os
import cv2
import numpy as np

def preprocess_data(input_folder, output_folder, image_size=(224, 224)):
    # Créer le dossier de sortie s'il n'existe pas déjà
    os.makedirs(output_folder, exist_ok=True)

    # Parcourir toutes les images dans le dossier d'entrée
    for image_file in os.listdir(input_folder):
        # Construire le chemin d'accès complet de l'image
        image_path = os.path.join(input_folder, image_file)
        
        # Vérifier si le chemin correspond à un fichier
        if os.path.isfile(image_path):
            # Charger l'image
            image = cv2.imread(image_path)

            # Redimensionner l'image
            image = cv2.resize(image, image_size)

            # Normaliser l'image
            image = image.astype(np.float32) / 255.0

            # Construire le chemin d'accès pour sauvegarder l'image prétraitée dans le dossier de sortie
            output_image_path = os.path.join(output_folder, image_file)

            # Sauvegarder l'image prétraitée dans le dossier de sortie
            cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    # Chemin vers le dossier contenant les images IRM
    input_folder = "D:\\Alzheimer\\donnes\\new_moderate_dementia"
    # Chemin vers le dossier où vous souhaitez enregistrer les images prétraitées
    output_folder = "D:\\Alzheimer\\pretraitement\\moderate_demented"
    preprocess_data(input_folder, output_folder)
