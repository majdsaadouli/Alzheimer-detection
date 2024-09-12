import os
import random
import shutil

# Définir le chemin vers le dossier contenant les données d'origine
original_folder = r'D:\archive (5)\Data\Non Demented'

# Définir le nouveau chemin pour le dossier de sortie
new_folder_path = r'D:\Alzheimer\donnes\new_non_demented'

# Créer le dossier de sortie s'il n'existe pas déjà
os.makedirs(new_folder_path, exist_ok=True)

# Définir le nombre maximal d'images à conserver par dossier
max_images_per_folder = 100

# Parcourir les images dans le dossier d'origine
images = os.listdir(original_folder)

# Vérifier si le nombre d'images dépasse le maximum
if len(images) > max_images_per_folder:
    # Sélectionner aléatoirement max_images_per_folder images à conserver
    images_to_keep = random.sample(images, max_images_per_folder)

    # Copier les images sélectionnées dans le nouveau dossier de sortie
    for image in images_to_keep:
        image_path = os.path.join(original_folder, image)
        output_image_path = os.path.join(new_folder_path, image)
        shutil.copy(image_path, output_image_path)
else:
    # Copier toutes les images dans le nouveau dossier de sortie
    for image in images:
        image_path = os.path.join(original_folder, image)
        output_image_path = os.path.join(new_folder_path, image)
        shutil.copy(image_path, output_image_path)
