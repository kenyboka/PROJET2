"""

"""
def analyser(depenses, budget_json):
    resultats = []
    limites = {item["categorie"]: item["limite"] for item in budget_json["budget"]}
    for categorie, montant in depenses.items():
        limite = limites.get(categorie)
        if limite is None:
            etat = "catehorie inconnue"
        elif montant > limite:
            etat = "dépassé"
        else: etat = "excellent"
        resultats.append((categorie, montant, limite,etat))
    return resultats

def ecrire_rapport(chemin, mois, devise,total, comparaison):
    """
    ecrire le rapport dans un fichier texte.
    """
    whith open chemin, "w" as r:
    
        r.write(f"le rapport du mois de {mois}")
        r.write(f"le total des depenses est : {total} {devise}")
        r.write(f"Categorie / Depense / limite / etat")
    
        for categorie, montant, limite, etat in comparaison:
            r.write(f"{categorie} / {montant} / {limite} / {etat}")
    