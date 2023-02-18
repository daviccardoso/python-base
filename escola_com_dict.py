#!/usr/bin/env python3
"""Generate report on kids distribution by extracurricular activity.

This script creates a report that shows how many kids are enrolled in a specific extracurricular activity, grouping by grade and activity name.
"""

__version__ = "0.3.0"
__author__ = "Davi Cardoso"

# Grades
salas = {
    "sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala 2": ["João", "Antonio", "Carlos", "Maria", "Isolda"],
}

# Students enrolled in specific extracurricular activities
atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

sala_por_atividade = {}

for nome_atividade, atividade in atividades.items():
    print(f"{nome_atividade:-^40}\n")

    for nome_sala, alunos_sala in salas.items():
        sala_por_atividade[nome_sala] = set(alunos_sala) & set(atividade)
        print(f"Alunos da {nome_sala}:", ", ".join(sala_por_atividade[nome_sala]))

    print()
