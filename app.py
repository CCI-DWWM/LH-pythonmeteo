from flask import Flask, request, render_template
from modele import get_nom_ville
from meteo import get_meteo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ville = None
    description = None
    temperature = None
    temp_min = None
    temp_max = None
    humidite = None

    if request.method == "POST":
        cp = request.form.get("cp")
        ville = get_nom_ville(cp)
        if ville:
            meteo = get_meteo(ville)
            if meteo:
                description = meteo["description"]
                temperature = meteo["temperature"]
                temp_min = meteo["temp_min"]
                temp_max = meteo["temp_max"]
                humidite = meteo["humidite"]
            else:
                ville = ville or "Inconnue"
                description = "Pas de météo disponible"
        else:
            ville = "Inconnue"
            description = "Pas de météo disponible"

    return render_template("index.html", ville=ville, description=description,
                           temperature=temperature, temp_min=temp_min,
                           temp_max=temp_max, humidite=humidite)

if __name__ == "__main__":
    app.run(debug=True)