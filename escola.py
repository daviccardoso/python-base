#!/usr/bin/env python3
"""Generate report on kids distribution by extracurricular activity.

This script creates a report that shows how many kids are enrolled in a specific extracurricular activity, grouping by grade and activity name.
"""

__version__ = "0.0.1"
__author__ = "Davi Cardoso"

# Grades
sala_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala_2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# Students enrolled in specific extracurricular activities
classe_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
classe_musica = ["Erik", "Carlos", "Maria"]
classe_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
        ('Inglês', classe_ingles),
        ('Música', classe_musica),
        ('Dança', classe_danca)
]

for nome_atividade, atividade in atividades:
    print(f"{nome_atividade:-^40}\n")

    atividade_sala_1 = []
    atividade_sala_2 = []

    for aluno in atividade:
        if aluno in sala_1:
            atividade_sala_1.append(aluno)
        elif aluno in sala_2:
            atividade_sala_2.append(aluno)

    print("Alunos da sala 1:", ', '.join(atividade_sala_1))
    print("Alunos da sala 2:", ', '.join(atividade_sala_2))
    print()

