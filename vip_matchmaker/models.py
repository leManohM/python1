from dataclasses import dataclass
from typing import Dict

@dataclass
class Group:
    nom: str
    age: int
    taille: int
    budget: int
    score: int = 0

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(
            nom=d.get("nom", ""),
            age=int(d.get("age", 0)),
            taille=int(d.get("taille", 0)),
            budget=int(d.get("budget", 0)),
            score=int(d.get("score", 0)),
        )

@dataclass
class Table:
    nom: str
    capacite: int
    min_budget: int
    assigned_groups: list = None

    def __post_init__(self):
        if self.assigned_groups is None:
            self.assigned_groups = []

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(
            nom=d.get("nom", "Table"),
            capacite=int(d.get("capacite", 0)),
            min_budget=int(d.get("min_budget", 0)),
        )
