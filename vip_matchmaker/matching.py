from .models import Group, Table
from .utils import calculer_score


def match_groups_to_tables(groups_data, tables_data):
    """Match groups to tables.

    groups_data: list of dicts with keys nom, age, taille, budget (score optional)
    tables_data: list of dicts with keys nom, capacite, min_budget

    Retourne: list of tuples (group_nom, table_nom or None)
    """
    groups = [Group.from_dict(g) for g in groups_data]
    tables = [Table.from_dict(t) for t in tables_data]

    # calculer score si absent
    for g in groups:
        if g.score == 0:
            g.score = calculer_score({"age": g.age, "taille": g.taille, "budget": g.budget})

    # tri par score décroissant, puis par budget décroissant
    groups.sort(key=lambda x: (x.score, x.budget), reverse=True)

    # tables disponibles (on ne permet qu'un groupe par table dans cette version simple)
    available_tables = {t.nom: t for t in tables}

    matches = []

    for g in groups:
        # trouver tables qui acceptent le groupe
        suitable = [t for t in available_tables.values() if t.capacite >= g.taille and g.budget >= t.min_budget]
        if suitable:
            # choisir la table avec min_budget le plus bas (on satisfait d'abord les groupes sans gaspiller)
            chosen = sorted(suitable, key=lambda x: (x.min_budget, x.capacite))[0]
            chosen.assigned_groups.append(g.nom)
            # une seule assignation par table ici
            del available_tables[chosen.nom]
            matches.append((g.nom, chosen.nom))
        else:
            matches.append((g.nom, None))

    return matches


if __name__ == "__main__":
    # test rapide
    groupes = [
        {"nom": "Groupe A", "age": 30, "taille": 4, "budget": 120},
        {"nom": "Groupe B", "age": 22, "taille": 6, "budget": 80},
        {"nom": "Groupe C", "age": 28, "taille": 3, "budget": 200},
    ]
    tables = [
        {"nom": "Table VIP 1", "capacite": 4, "min_budget": 100},
        {"nom": "Table VIP 2", "capacite": 6, "min_budget": 70},
    ]
    print(match_groups_to_tables(groupes, tables))
