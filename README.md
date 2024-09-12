##Détection de la maladie d'Alzheimer à partir d'images IRM
Dans ce projet, j'ai développé un modèle d'apprentissage automatique pour détecter la maladie d'Alzheimer à partir d'images IRM du cerveau. Les données proviennent de bases de données publiques sur Kaggle, qui fournissent des images IRM de patients atteints de la maladie d'Alzheimer à différents stades (léger, modéré, sévère) ainsi que des contrôles non affectés.

##Étapes principales du projet
1. Obtention des données
J'ai utilisé des images IRM de patients atteints de la maladie d'Alzheimer disponibles sur Kaggle. Les images sont étiquetées en fonction du diagnostic clinique : stades léger, modéré, sévère, ainsi que des contrôles sains.

2. Prétraitement des données
Réduction du Nombre d'Images :
Étant donné la taille importante des données, j'ai réduit le nombre d'images par dossier à 100 pour chaque classe en utilisant un script Python.

Normalisation des Intensités d'Image :
Pour faciliter l'entraînement du modèle, j'ai normalisé les valeurs des pixels des images afin qu'elles soient dans une plage spécifique, généralement entre 0 et 1. Cela permet de rendre les données plus comparables.

3. Modélisation avec CNN (Convolutional Neural Network)
J'ai utilisé un modèle CNN pour extraire les caractéristiques discriminantes des images IRM. Ce réseau de neurones convolutif a permis de capturer les détails visuels essentiels pour la classification des différents stades de la maladie d'Alzheimer.

4. Entraînement du modèle
J'ai entraîné le modèle en utilisant la méthode fit, en fournissant un générateur de données d'entraînement et de validation (train_generator et test_generator). Le modèle a été entraîné sur un nombre d'époques défini et une taille de lot spécifique.

5. Évaluation du modèle
J'ai évalué les performances du modèle à l'aide des métriques suivantes :

Training Loss : mesure de l'erreur du modèle sur les données d'entraînement à chaque étape.
Training Accuracy : mesure de la proportion d'images correctement classées sur l'ensemble d'entraînement.
J'ai également utilisé une matrice de confusion pour comparer les prédictions du modèle avec les vraies étiquettes des données de test. La matrice montre les prédictions correctes (éléments diagonaux) et les erreurs de classification (éléments hors diagonale).

6. Déploiement de l'interface utilisateur
Après avoir entraîné le modèle, je l'ai déployé dans une interface utilisateur conviviale construite en utilisant Python. Cette interface permet aux utilisateurs de charger des images IRM du cerveau et d'obtenir des prédictions instantanées sur la présence ou non de la maladie d'Alzheimer.

Lien vers la présentation
[https://www.canva.com/design/DAGEBVK1woQ/3r3dPUQvuCpnHFGPCoszWQ/edit?utm_content=DAGEBVK1woQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton]
