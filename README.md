# Coodesh Back-end challenge - Space Flight News

## Crud com python flask-restx e mongodb com cron para clonar api existente

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

## Apresentação

https://www.loom.com/share/8392cdb5106d45e29a954bdc7948fb74

<br>

>  This is a challenge by [Coodesh](https://coodesh.com/)
