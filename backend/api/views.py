from django.shortcuts import render
import os
import json
import numpy as np
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from keras.models import load_model
from PIL import Image, ImageOps
from rest_framework.response import Response

##
# Réalisé des prédictions sur les image envoyer
# Input
# # Liste d'image
# # Modèle
# EndPoint -> http://localhost:8000/api/predict
# Methood -> POST
#


@api_view(['POST'])
def PredictImage(request):
    # récupère les image et le modèle
    images = request.FILES.getlist('images')

    results = doPred(images)

    response_data = json.dumps(results)

    return Response(data=response_data, content_type='application/json')

# Réaliser une prédiction


def doPred(images):
    results = []
    # Charger le modèle Keras/TensorFlow
    model_path = os.path.join(settings.BASE_DIR, 'models', 'keras_model.h5')
    model = load_model(model_path, compile=False)

    # Charger les labels depuis le fichier texte
    labels_path = os.path.join(settings.BASE_DIR, 'models', 'labels.txt')
    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()

    for image in images:
        img_norm = norm_img(image)
        predictions = model.predict(img_norm)
        pred_w_label = addLabelToPredic(predictions, labels)
        result = {
            'image': str(image),
            'prediction': pred_w_label
        }
        results.append(result)

    return results


# Fonction normalisation image
def norm_img(img_file):
    img = Image.open(img_file)
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Associer les prediciton a leur labèles


def addLabelToPredic(predictions, categories):
    img_pred = []

    for i in range(len(categories)):
        img_pred.append((categories[i], predictions[0][i]))
    # Tri des prédictions par ordre décroissant de probabilité
    img_pred.sort(key=lambda x: x[1], reverse=True)
    # Récupération de la catégorie avec la plus haute probabilité
    prediction = {
        'label': img_pred[0][0],
        'pourcentage': img_pred[0][1]*100
    }
    return prediction
