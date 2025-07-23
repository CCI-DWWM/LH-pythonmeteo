import sqlite3

def get_nom_ville(cp):
    conn = sqlite3.connect('villes.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT nom_commune FROM villes WHERE cp = ?", (cp,))
    resultat = cur.fetchone()
    conn.close()
    if resultat:
        return resultat[0]
    else:
        return None