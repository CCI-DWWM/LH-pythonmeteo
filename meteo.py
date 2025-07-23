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
            return {
                "description": data['weather'][0]['description'],
                "temperature": data['main']['temp'],
                "temp_min": data['main']['temp_min'],
                "temp_max": data['main']['temp_max'],
                "humidite": data['main']['humidity']
            }
        except (KeyError, IndexError):
            return None
    elif response.status_code == 404:
        return None
    else:
        return None
