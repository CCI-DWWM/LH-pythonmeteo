from flask import Flask, request, render_template
from modele import get_nom_ville
from meteo import get_meteo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ville = None
    meteo = None
    if request.method == "POST":
        cp = request.form.get("cp")
        ville = get_nom_ville(cp)
        if ville:
            meteo = get_meteo(ville)
        else:
            ville = "Inconnue"
            meteo = "Pas de météo disponible"
    return render_template("index.html", ville=ville, meteo=meteo)

if __name__ == "__main__":
    app.run(debug=True)