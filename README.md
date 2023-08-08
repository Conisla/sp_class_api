# Virtual env

```sh
python -m venv .env
.\.env\Scripts\activate.bat
```

# Dependencies

```sh
pip install requirements.txt
```

# Docker 

## Docker Images

```sh
cd backend
docker build -t image_api_fertility .
```

```sh
cd front
docker build -t image_streamlit_fertility .
```

## Docker compose 

```sh
docker-compose up -d
```

# Stop
```sh
docker-compose stop
```

Go to http://localhost:8501/
