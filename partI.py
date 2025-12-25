#jour 1 avec chatGPT
def creer_groupe():
    groupe = {}
    groupe["nom"] = input("Nom du groupe : ")
    groupe["age"] = int(input("Age du groupe : "))
    groupe["taille"] = int(input("Taille du groupe : "))
    groupe["budget"] = int(input("Budget de la table : "))
    return groupe

# jour 2 avec chatGPT

def verifier_acces(groupe):
    res = False
    if groupe["age"] >= 18 and groupe["budget"] >= 50 and groupe["taille"] <= 6:
        res = True
    return res
"""
groupe = creer_groupe()
if verifier_acces(groupe):
    print("Accès autorisé")
else:
    print("Accès refusé")
"""
# jour 3 avec chatGPT
"""
groupes = []

while True:
    groupe = creer_groupe()
    groupes.append(groupe)

    continuer = input("Ajouter un autre groupe ? (o/n) : ")
    if continuer != "o":
        break


for g in groupes:
    if verifier_acces(g):
        print(g["nom"], "→ Accès autorisé")
    else:
        print(g["nom"], "→ Accès refusé")

        
print("Fin du programme")
print("Nombre de groupes traités :", len(groupes))
print('les groupes : ', groupes)
"""
# jour 4 avec chatGPT
# ajout d'une fonctionnalité pour les scores des groupes
# chaque groupe aura un score basé sur son budget et sa taille et son age moyen

def calculer_score(groupe):
    score = 0
    if groupe["budget"] >= 150:
        score += 50
    elif groupe["budget"] >= 100:
        score += 30
    elif groupe["budget"] >= 50:
        score += 10
    

    if groupe["taille"] <= 4:
        score += 20
    elif groupe["taille"] <= 6:
        score += 10

    if groupe["age"] >= 25: 
        score += 20
    elif groupe["age"] >= 18:
        score += 10

    return score

"""
for g in groupes:
    g["score"] = calculer_score(g)
    print(g["nom"], "→ Score :", g["score"])


# tri des groupes par score décroissant
groupes_tries = sorted(groupes, key=lambda x: x["score"], reverse=True)
print("Groupes triés par score décroissant :")
for g in groupes_tries:
    print(g["nom"], "→ Score :", g["score"])
"""
# jour 5 avec chatGPT

#a list of groupes with their scores and dates of creation

groupe_data = [
    {"nom": "Groupe A", "age": 30, "taille": 4, "budget": 120, "score": 60, "date_creation": "2024-01-15"},
    {"nom": "Groupe B", "age": 22, "taille": 6, "budget": 80, "score": 30, "date_creation": "2024-02-10"},
    {"nom": "Groupe C", "age": 28, "taille": 3, "budget": 200, "score": 90, "date_creation": "2024-03-05"},
    {"nom": "Groupe D", "age": 19, "taille": 5, "budget": 60, "score": 20, "date_creation": "2024-01-25"},
]
"""
#sort by budget descending
groupes_sorted_by_budget = sorted(groupe_data, key=lambda x: x["budget"], reverse=True)
print("Groupes triés par budget décroissant :")     
for g in groupes_sorted_by_budget:
    print(g["nom"], "→ Budget :", g["budget"])
    """
#tache 1 find the highst score groupe 

def trouver_groupe_meilleur_score(groupes):
    meilleur_groupe = max(groupes, key=lambda x: x["score"])
    return meilleur_groupe
def departager_egalite(groupes):
    max_score = max(g["score"] for g in groupes)
    groupes_egaux = [g for g in groupes if g["score"] == max_score]
    if len(groupes_egaux) > 1:
        groupes_egaux_sorted = sorted(groupes_egaux, key=lambda x: x["budget"])
        return groupes_egaux_sorted[0]
    else:
        return groupes_egaux[0]
