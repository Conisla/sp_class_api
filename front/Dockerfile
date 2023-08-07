# Utilisez l'image python officielle comme image de base
FROM python:3.10.6

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances du projet
RUN pip install streamlit

# Copier le reste du code source dans le conteneur
COPY . .

# Exposer le port sur lequel votre application Streamlit écoute (par exemple, 8501)
EXPOSE 8501

# Lancer l'application Streamlit lors du démarrage du conteneur
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]
