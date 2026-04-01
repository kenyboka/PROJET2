"""
Gestion de budget
Auteur: Joseph Boka
"""
import csv 
import json
 
def lire_csv(chemin):
    """
    lire un fichier CSV contenant les dépenses
    """
    Liste_depenses = {}
    try:

        with open(chemin, "r") as fichier:
            lecteur = csv.DictReader(fichier)

        # Lire chaque ligne du CSV
    
        for ligne in lecteur:
            categorie = ligne["description"]
            montant = (ligne["montant"])
            Liste_depenses[categorie] =  Liste_depenses.get(categorie, 0) + montant


    except FileNotFoundError:
        print("Erreur : fichier introuvable")
    except ValueError:
        print("erreur : montant invalide dans le CSV")

    return Liste_depenses

def lire_json(chemin):
    """
    lire un fichier JSON contenant le budget.
    """
    try: 
        with open(chemin, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("erreur : fichier JSON introuvable.")
        return {}
    except json.JSONDecodeError:
        print("erreur : JSON mal formé.")
        return {}

