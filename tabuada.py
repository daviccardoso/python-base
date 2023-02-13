#!/usr/bin/env python3
"""Imprime as tabuadas de 1 ao 10."""

__version__ = "0.0.1"
__author__  = "Davi Cardoso"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)

    for outro_numero in numeros:
        print(numero * outro_numero)

    print("--------------")
