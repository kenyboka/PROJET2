"""
Projet : Gestion de budget
Auteur : Joseph Boka
Analyser les dépenses et ecrire le rapport dans un fichier
"""
def analyser(depenses, budget_json):
    """
    But: analyser les dépenses et les comparer avec les dépenses par cathégorie et les limites du budget
    Entrée: depenses par catégorie 
            données JSON contenant les limites de budget
    sortie: aucune
    """
    resultats = []
    data = budget_json.get("budget", [])
    limites = {item["categorie"]: item["limite"] for item in data}
    for categorie, montant in depenses.items():
        limite = limites.get(categorie)
        if limite is None:
            etat = "categorie inconnue"
        elif montant > limite:
            etat = "dépassé"
        else: etat = "excellent"
        resultats.append((categorie, montant, limite,etat))
    return resultats


def ecrire_rapport(chemin, mois, devise,total, comparaison):
    """
    But: écrire le rapport dans un fichier texte.
    entrées: (chemin, mois, devise,total, comparaison)
    Sortie: aucun 
    """
    with open (chemin, "w") as B:

        B.write(f"\nle rapport du mois de {mois}")
        B.write(f"\nle total des depenses est : {total} {devise}")
        B.write(f"\nCategorie / Depense / limite / etat")
    
        for categorie, montant, limite, etat in comparaison:
            B.write(f"\n{categorie} / {montant} / {limite} / {etat}")
            