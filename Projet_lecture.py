"""
Gestion de budget
Auteur: Joseph Boka
Description : Programme pour lire les fichiers CSV et JSON.
"""
import csv 
import json
 
def lire_csv(chemin):
    """
    but : lire un fichier CSV contenant les dépenses
    entre : chemin vers le csv
    sortie : aucune
    """
    Liste_depenses = {}
    try:

        with open(chemin, "r") as fichier:
            lignes = fichier.readlines()

            entetes = lignes[0].strip().split(",")
            index_description = entetes.index("description")
            index_montant = entetes.index("montant")
            

        # Lire chaque ligne du CSV
        for ligne in lignes[1:]:
            print("Ligne brute :", repr(ligne))

            elements = ligne.strip().split(",")
            print("Éléments :", elements)

            categorie = elements[index_description].strip()
            montant = float(elements[index_montant].strip())
            
            Liste_depenses[categorie] =  Liste_depenses.get(categorie, 0) + montant


    except FileNotFoundError:
        print("Erreur : fichier introuvable")
    except ValueError:
        print("erreur : montant invalide dans le CSV")

    return Liste_depenses

def lire_json(chemin):
    """
    But: lire un fichier JSON contenant le budget.
    Entrée: chemin json
    Sortie: aucune
    """
    try: 
        with open(chemin, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("erreur : fichier JSON introuvable.")
        return {}
    except json.JSONDecodeError:
        print("erreur : JSON mal formé."
        return {}

