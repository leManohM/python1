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
    print(f" le groupe {groupe['nom']} a accès : {res}")
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
    {"nom": "Groupe A", "age": 30, "taille": 4, "budget": 120, "score": 60},
    {"nom": "Groupe B", "age": 22, "taille": 6, "budget": 80, "score": 30},
    {"nom": "Groupe C", "age": 28, "taille": 3, "budget": 200, "score": 90},
    {"nom": "Groupe D", "age": 19, "taille": 5, "budget": 60, "score": 20},
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
#gestion des nouveaux groupes qui arrivent
# priorité = score > budget > ancienneté
groupe_data = sorted(groupe_data, key=lambda x: x["score"], reverse=True)
while True :
    #arriver de nouveaux groupes
    if input("Ajouter un nouveau groupe ? (o/n) : ") == "o":
        nouveau_groupe = creer_groupe()
        if verifier_acces(nouveau_groupe):
            nouveau_groupe["score"] = calculer_score(nouveau_groupe)
            groupe_data.append(nouveau_groupe)
            groupe_data = sorted(groupe_data, key=lambda x: x["score"], reverse=True)
            meilleur_groupe = departager_egalite(groupe_data)
            print("Le groupe avec le meilleur score est :", meilleur_groupe["nom"], "avec un score de", meilleur_groupe["score"])
            print("une table leur est attribuée")
            groupe_data.remove(meilleur_groupe)
    else:
        break

#On par du principe que l'on gere que les groupe qui n'ont pas de table
#et qui arrivent au fur et a mesure

wainting_for_new_group = [] #Wainting list for new groups
def nouvelle_arrivee_groupes(wainting_for_new_group):
    """Gère l'arrivée de nouveaux groupes et leur attribution de table. si ne serait ce q'un groupe a été inscrit ca renvoi a True"""
    while (input("Ajouter un nouveau groupe ? (o/n) : ") == "o"):
            nouveau_groupe = creer_groupe(wainting_for_new_group
            if verifier_acces(nouveau_groupe):
                nouveau_groupe["score"] = calculer_score(nouveau_groupe)
                nouveau_groupe["anciennete"] = 0 # initialiser l'ancienneté
                wainting_for_new_group.append(nouveau_groupe)
            else:
                break
                return True
    return False
def departager_groupe(groupes):
        groupeskey=lambda x: (x["anciennete"],x["score"]), reverse=True)

def check_wainting_list(wainting_for_new_group):
    """Vérifie la liste d'attente et attribue des tables aux groupes en fonction de leur score, budget et ancienneté."""
