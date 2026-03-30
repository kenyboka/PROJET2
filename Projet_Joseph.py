"""
Gestion de budget
Auteur: Joseph Boka
"""
import csv 
import json
 
def lire_csv(chemin):
    """
    lire un fichier CSV contenant les dépenses
    chemin du fichier CSV
    ditionnaire {categorie: montant}
    """
    Liste_depenses = {}
    try:

        with open(chemin, "r") as fichier:
            lecteur = csv.DictReader(fichier)

        # Lire chaque ligne du CSV
    
        for ligne in lecteur:
            categorie = ligne["description"]
            montant = float(ligne["montant"])
            Liste_depenses[categorie] =  Liste_depenses.get(categorie, 0) + montant


    except FileNotFoundError:
        print("Erreur : fichier introuvable")
    except ValueError:
        print("erreur : montant invalide dans le CSV")

    return Liste_depenses


