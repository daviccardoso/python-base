#!/usr/bin/env python3

import sys

temperatura = input("Qual é a temperatura atual? ")
indice_umidade = input("Qual é o índice de umidade atual? ")

try:
    temperatura_atual = float(temperatura)
    indice_umidade_atual = float(indice_umidade)
except:
    print(
        "Não foi possível converter os valores informados "
        "em suas representações numéricas."
    )
    sys.exit(1)

if temperatura_atual > 45:
    print("ALERTA! Perigo de calor extremo.")
elif temperatura_atual * 3 >= indice_umidade_atual:
    print("ALERTA! Perigo de calor úmido")
elif 10 <= temperatura_atual <= 30:
    print("Normal")
elif 0 <= temperatura_atual < 10:
    print("Frio")
elif temperatura_atual < 0:
    print("Frio extremo")
