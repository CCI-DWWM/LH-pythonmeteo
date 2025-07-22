import csv
import sqlite3

# Connexion à la base SQLite (fichier .sqlite)
conn = sqlite3.connect('villes.sqlite')
cur = conn.cursor()

# On supprime la table si elle existe
cur.execute("DROP TABLE IF EXISTS villes")

# On crée une table simple avec cp (code postal) et nom_commune
cur.execute("CREATE TABLE villes (cp TEXT, nom_commune TEXT)")

# Lecture du fichier CSV avec encodage latin-1 et séparateur ;
with open("019HexaSmal.csv", newline='', encoding='latin-1') as fichier:
    reader = csv.DictReader(fichier, delimiter=';')

    for ligne in reader:
        nom = ligne['Nom_de_la_commune'].strip()
        cp = ligne['Code_postal'].zfill(5)  # remet les zéros au début si nécessaire

        if cp and nom:
            cur.execute("INSERT INTO villes VALUES (?, ?)", (cp, nom))

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("Base de données villes.sqlite créée avec succès ✅")