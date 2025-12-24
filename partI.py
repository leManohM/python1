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


for g in groupes:
    g["score"] = calculer_score(g)
    print(g["nom"], "→ Score :", g["score"])


# tri des groupes par score décroissant
groupes_tries = sorted(groupes, key=lambda x: x["score"], reverse=True)
print("Groupes triés par score décroissant :")
for g in groupes_tries:
    print(g["nom"], "→ Score :", g["score"])