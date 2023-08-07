import requests
import json
import streamlit as st

# Titre de l'application
st.title('Fertility Prediction API')

# Widget pour télécharger plusieurs images
uploaded_images = st.file_uploader(
    "Télécharger des images",
    type=['jpg', 'jpeg', 'png', 'bmp'],
    accept_multiple_files=True
)

# URL de l'API Django
API_URL = 'http://localhost:8000/api/predict'

# Bouton pour soumettre les images à l'API
if st.button('Prédire'):
    if uploaded_images is not None:
        results_str = []
        for image in uploaded_images:
            image_bytes = image.read()
            files = {'images': (image.name, image_bytes, image.type)}
            response = requests.post(API_URL, files=files)

            # Vérifier si la requête a réussi
            if response.status_code == 200:
                prediction = response.json()
                result = prediction
                results_str.append(result)
            else:
                st.write(
                    f"Erreur lors de la prédiction pour l'image {image.name}. Veuillez réessayer.")

        results_json = [json.loads(result_str) for result_str in results_str]

        # Afficher les résultats des prédictions
        st.write("Résultats des prédictions :")

        for i, result in enumerate(results_json):
            prediction = result[0]
            image_name = prediction['image']
            label = prediction['prediction']['label']
            pourcentage = prediction['prediction']['pourcentage']

            # Afficher l'image avec les informations à côté
            col1, col2 = st.columns(2)

            with col1:
                st.image(uploaded_images[i], use_column_width=True)

            with col2:
                st.write(f"Image: {image_name}")
                st.write(f"Prédiction: {label}")
                st.write(f"Taux de confiance: {pourcentage:.2f}")
