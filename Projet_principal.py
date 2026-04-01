"""
Projet : Gestion de budget
Auteur : Joseph Boka
Description : Programme principal qui excécute la lecture, l'analyse et écrire du rapport.
"""
from Projet_lecture import lire_csv, lire_json
from Projet_rapport import analyser, ecrire_rapport

def principal():
    """
    Programme principal qui excécute la lecture, l'analyse et écrire du rapport
    Entrées: les chemins csv et json
    Sortie: le rapport en fichier text
    """

    chemin_csv = "data/liste_depenses.csv"
    chemin_json = "data/budget.json"
    chemin_sortie = "output/rapport.txt"

    depenses = lire_csv(chemin_csv)
    budget = lire_json(chemin_json)

    comparaison = analyser(depenses, budget)

    total = sum(depenses.values())
    mois = "Mars"
    devise = "$"

    ecrire_rapport(chemin_sortie, mois, devise, total, comparaison)


if __name__ == "__main__":
    principal()
