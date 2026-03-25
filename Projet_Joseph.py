"""
Gestion de budget
Auteur: Joseph Boka
"""
import csv 
 
def lire_liste_depense(chemin):
    """
    lire un fichier CSV
    afficher chaque dépense
    calculer le total
    """
    Liste_depenses = {}
    try:
        fichier = open(chemin, "r")
        lecteur = csv.DictReader(fichier)
        print(lecteur.fieldnames)

        # Lire chaque ligne du CSV
    
        for ligne in lecteur:
            description = ligne["description"]
            montant = float(ligne["montant"])
            Liste_depenses[description] = montant

        fichier.close()

        # Affichage des dépenses
        for element in Liste_depenses:
            print(f"{element} : {Liste_depenses[element]}$")

        # Calcul du total
        Total = 0
        for montant in Liste_depenses.values():
            Total += montant

        print(f"\nMontant total : {Total}$")

    except FileNotFoundError:
        print("Erreur : fichier introuvable")

    return Liste_depenses

chemin = "Liste_depenses.csv"
lire_liste_depense(chemin)

