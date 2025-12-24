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
    if groupe["age"] > 18 and groupe["budget"] > 50 and groupe["taille"] > 6:
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
