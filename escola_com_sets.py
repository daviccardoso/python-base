#!/usr/bin/env python3
"""Generate report on kids distribution by extracurricular activity.

This script creates a report that shows how many kids are enrolled in a specific extracurricular activity, grouping by grade and activity name.
"""

__version__ = "0.2.0"
__author__ = "Davi Cardoso"

# Grades
sala_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala_2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# Students enrolled in specific extracurricular activities
classe_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
classe_musica = ["Erik", "Carlos", "Maria"]
classe_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", classe_ingles),
    ("Música", classe_musica),
    ("Dança", classe_danca),
]

for nome_atividade, atividade in atividades:
    print(f"{nome_atividade:-^40}\n")

    atividade_sala_1 = set(sala_1) & set(atividade)
    atividade_sala_2 = set(sala_2) & set(atividade)

    print("Alunos da sala 1:", ", ".join(atividade_sala_1))
    print("Alunos da sala 2:", ", ".join(atividade_sala_2))
    print()
