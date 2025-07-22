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
````bash
py app.py
````
essayer un code postal et vous aurez peut-être la meteo (api ne retourne pas toujours (erreur 401)