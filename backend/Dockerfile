# Utilisez l'image python officielle comme image de base
FROM python:3.10.6

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances du projet
RUN pip install django djangorestframework django-cors-headers tensorflow pillow

# Copier le reste du code source dans le conteneur
COPY . .

# Exposer le port sur lequel votre application Django écoute 
EXPOSE 8000

# Lancer le serveur Django lors du démarrage du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
