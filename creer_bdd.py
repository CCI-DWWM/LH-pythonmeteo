import csv
import sqlite3

# Connexion à la base SQLite (fichier .sqlite)
conn = sqlite3.connect('villes.sqlite')
cur = conn.cursor()

# On supprime la table si elle existe
cur.execute("DROP TABLE IF EXISTS villes")

# On crée une table avec code postal et nom_commune
cur.execute("CREATE TABLE villes (cp TEXT, nom_commune TEXT)")

# Lecture du fichier CSV;
with open("019HexaSmal.csv", newline='', encoding='latin-1') as fichier:
    reader = csv.DictReader(fichier, delimiter=';')

    for ligne in reader:
        nom = ligne['Nom_de_la_commune'].strip()
        cp = ligne['Code_postal'].zfill(5)

        if cp and nom:
            cur.execute("INSERT INTO villes VALUES (?, ?)", (cp, nom))


conn.commit()
conn.close()

print("Base de données villes.sqlite créée avec succès")