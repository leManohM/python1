from vip_matchmaker.matching import match_groups_to_tables


def test_simple_match():
    groupes = [
        {"nom": "G1", "age": 30, "taille": 4, "budget": 120},
        {"nom": "G2", "age": 22, "taille": 6, "budget": 80},
        {"nom": "G3", "age": 28, "taille": 3, "budget": 200},
    ]
    tables = [
        {"nom": "T1", "capacite": 4, "min_budget": 100},
        {"nom": "T2", "capacite": 6, "min_budget": 70},
    ]

    matches = match_groups_to_tables(groupes, tables)
    # Expect G3 (high budget) get T1 or T2; algorithm sorts by score then budget.
    assert any(g == "G3" and t in ("T1", "T2") for g, t in matches)
    # All groups are present in result
    assert set(g for g, _ in matches) == {"G1", "G2", "G3"}


def test_no_table_available():
    groupes = [{"nom": "G4", "age": 25, "taille": 8, "budget": 30}]
    tables = [{"nom": "T1", "capacite": 6, "min_budget": 50}]
    matches = match_groups_to_tables(groupes, tables)
    assert matches == [("G4", None)]
