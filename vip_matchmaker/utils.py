def calculer_score(groupe):
    """Calcule un score simple pour un groupe à partir du budget, taille et âge."""
    score = 0
    budget = groupe.get("budget", 0)
    taille = groupe.get("taille", 0)
    age = groupe.get("age", 0)

    if budget >= 150:
        score += 50
    elif budget >= 100:
        score += 30
    elif budget >= 50:
        score += 10

    if taille <= 4 and taille > 0:
        score += 20
    elif taille <= 6 and taille > 0:
        score += 10

    if age >= 25:
        score += 20
    elif age >= 18:
        score += 10

    return score
