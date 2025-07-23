import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_meteo(ville):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville},FR&appid={api_key}&units=metric&lang=fr"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"{ville.title()} : {description}, {temperature}°C"
        except (KeyError, IndexError):
            return "Données météo incomplètes"
    elif response.status_code == 404:
        return "Ville non trouvée"
    else:
        return f"Erreur {response.status_code} : Météo non disponible"