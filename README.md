# Installation et Configuration

## API Django

1. Clonez le dépôt du projet
2. Accédez au répertoire de l'API Django :

    ```bash
    cd backend
    ```

3. Créez et activez un environnement virtuel :

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

5. Lancez les migrations pour créer la base de données :

    ```bash
    python manage.py migrate
    ```

6. Lancez l'API Django :

    ```bash
    python manage.py runserver
    ```

### **Application Streamlit**

1. Accédez au répertoire de l'application Streamlit :

    ```bash
    cd front
    ```

2. Lancez l'application Streamlit :

    ```bash
    streamlit run app.py
    ```
