"""
rapport.py
Analyser les dépenses et ecrire le rapport dans un fichier
"""
def analyser(depenses, budget_json):
    resultats = []
    limites = {item["categorie"]: item["limite"] for item in budget_json["budget"]}
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
    ecrire le rapport dans un fichier texte.
    """
    with open (chemin, "w") as B:

        B.write(f"\nle rapport du mois de {mois}")
        B.write(f"\nle total des depenses est : {total} {devise}")
        B.write(f"\nCategorie / Depense / limite / etat")
    
        for categorie, montant, limite, etat in comparaison:
            B.write(f"\n{categorie} / {montant} / {limite} / {etat}")
            ligne = "-" * 50
            B.write(ligne + "\n")