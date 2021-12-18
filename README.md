# Coodesh Back-end challenge - Space Flight News

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Descrição !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## Tecnologias utilizadas

- Python
- Flask
- Flask-restx
- MongoDB
- Docker

## Setup

1. Configure .env
2.
```
# Configure virtual environnement 
python -m venv .venv

# Enter in virtual environnement
## Windows
.\.venv\Scripts\activate

## Linux
source .venv/bin/activate

# Install required packages
pip install -r .\api\requirements.txt

# Seed db
python .\seed.py

# Run local
python .\api\local.py

# Run production
docker-compose up --build
```

<br>

>  This is a challenge by [Coodesh](https://coodesh.com/)
