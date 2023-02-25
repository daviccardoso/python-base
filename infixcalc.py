#!/usr/bin/env python3
"""Calculadora infix

Funcionamento:

    [operação] [n1] [n2]

Operações:

    sum -> +
    sub -> -
    mul -> *
    div -> /

Uso:

    infixcalc.py sum 5 2
    7

    infixcalc.py mul 10 5
    50

    infixcalc.py
    operacao: sum
    n1: 5
    n2: 4
    9
"""

__version__ = "0.1.0"
__author__ = "Davi Cardoso"

import sys

valid_operations = {
    "sum": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y,
}

arguments = sys.argv[1:]

if not arguments:
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("\nQuantidade de argumentos inválida.")
    print("Ex.: sum 5 2")
    sys.exit(1)

operation, *numbers = arguments

if operation not in valid_operations:
    print(f"\nOperação inválida: {operation!r}")
    sys.exit(1)

valid_numbers = []

for number in numbers:
    if number.replace(".", "").isdigit():
        if "." in number:
            valid_numbers.append(float(number))
        else:
            valid_numbers.append(int(number))
    else:
        print(f"\nNúmero inválido: '{number}'")
        sys.exit(1)

n1, n2 = valid_numbers

print(valid_operations[operation](n1, n2))
