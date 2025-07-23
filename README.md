# LH-pythonmeteo
avec FastAPI

## Installation
Creation de l'environement virtuel
 ```bash
py -m venv .venv
```

Activer l'environement virtuel
```bash
py source .venv/Scripts/activate
```

Installation des librairies
````bash
pip install -r requirements.txt
````

## Execution du serveur
````bash
fastapi dev main.py
````

## La meteo
Pour accéder au service meteo par code postal :
````bash
py app.py
````
Rentrer un code postal et vous aurez la chance voir qu'il pleut chez vous.
````bash
41000
````