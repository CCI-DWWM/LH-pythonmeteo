import requests

API_KEY = "76e50ba2c3e0c31cfda9edaf2f7f833f"

def get_meteo(ville):
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Paris,FR&appid=76e50ba2c3e0c31cfda9edaf2f7f833f&units=metric&lang=fr"
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