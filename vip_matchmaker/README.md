# VIP Matchmaker Module

Ce module contient une API et une logique pour associer des groupes à des tables VIP.

Endpoints:
- `POST /match` JSON `{ "groupes": [...], "tables": [...] }` → renvoie `matches`
- `POST /score` JSON `{ "age":..., "taille":..., "budget":... }` → renvoie `score`

Voir tests dans `tests/test_matching.py` pour exemples d'usage.
