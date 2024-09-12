import tkinter as tk
from tkinter import filedialog
import tensorflow as tf
import numpy as np
from PIL import Image, ImageTk

# Charger le modèle
modele = tf.keras.models.load_model('mon_modele.h5')

# Fonction pour charger et prétraiter une image
def charger_et_pretraiter_image(chemin_image, taille=(128, 128)):
    # Charger l'image
    image = Image.open(chemin_image)
    # Convertir l'image en mode RVB (RGB)
    image = image.convert('RGB')
    # Redimensionner l'image
    image_redimensionnee = image.resize(taille)
    # Convertir en tableau numpy et normaliser les valeurs de pixel
    image_np = np.array(image_redimensionnee) / 255.0
    # Ajouter une dimension pour correspondre à l'entrée attendue du modèle
    image_pretraitee = np.expand_dims(image_np, axis=0)
    return image_pretraitee

# Fonction pour effectuer une prédiction avec le modèle
def faire_prediction(chemin_image):
    # Charger et prétraiter l'image
    image_test = charger_et_pretraiter_image(chemin_image)
    # Faire une prédiction avec le modèle
    prediction = modele.predict(image_test)
    # Convertir la sortie de la prédiction en classe prédite
    classes = ['demented', 'non demented', 'mild demented', 'moderate demented']
    classe_predite = classes[np.argmax(prediction)]
    return classe_predite

# Fonction appelée lorsque le bouton "Sélectionner une image" est cliqué
def parcourir_galerie():
    chemin_image = filedialog.askopenfilename(title="Sélectionner une image", filetypes=(("Fichiers image", "*.jpg;*.jpeg;*.png"), ("Tous les fichiers", "*.*")))
    if chemin_image:
        # Charger l'image sélectionnée et l'afficher dans la fenêtre
        image = Image.open(chemin_image)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        label_image.configure(image=photo)
        label_image.image = photo
        # Faire une prédiction avec le modèle
        classe_predite = faire_prediction(chemin_image)
        # Afficher la classe prédite avec une couleur correspondante
        if classe_predite == 'non demented':
            label_prediction.configure(text="Classe prédite: " + classe_predite, fg="green")
        elif classe_predite == 'demented':
            label_prediction.configure(text="Classe prédite: " + classe_predite, fg="red")
        else:
            label_prediction.configure(text="Classe prédite: " + classe_predite, fg="orange")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface Utilisateur pour Modèle de Prédiction")
root.geometry("600x400")  # Taille de la fenêtre

# Ajouter un style pour un thème médical
root.configure(bg="#F0F0F0")  # Couleur de fond
root.option_add("*Font", "Arial 12")  # Police de caractères
root.option_add("*Background", "#F0F0F0")  # Couleur de fond pour tous les widgets

# Charger et afficher l'image de fond
image_fond = Image.open("Screenshot 2023-03-16 212831.png")  # Remplacez "background_image.jpg" par le chemin de votre propre image de fond
image_fond = image_fond.resize((600, 400), Image.ANTIALIAS)
photo_fond = ImageTk.PhotoImage(image_fond)
label_fond = tk.Label(root, image=photo_fond)
label_fond.place(x=0, y=0, relwidth=1, relheight=1)

# Créer les widgets
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
label_instructions = tk.Label(frame, text="Sélectionnez une image à prédire :", bg="white")
button_browse = tk.Button(frame, text="Parcourir", command=parcourir_galerie)
label_image = tk.Label(frame, bg="white")
label_prediction = tk.Label(frame, text="", bg="white")

# Placer les widgets dans la fenêtre
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centrer la frame dans la fenêtre
label_instructions.grid(row=0, column=0, padx=10, pady=10, sticky="w")
button_browse.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_image.grid(row=2, column=0, padx=10, pady=10)
label_prediction.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Lancer la boucle principale
root.mainloop()
