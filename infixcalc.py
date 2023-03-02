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

    Os resultados são salvos em `infixcalc.log`
"""

__version__ = "0.2.0"
__author__ = "Davi Cardoso"

import sys, os
from datetime import datetime

math_operations = {
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
    log_file_path = input("Arquivo de log de operações (ENTER para ignorar): ")
    arguments = [operation, n1, n2, log_file_path]
elif len(arguments) < 3:
    print("\nQuantidade de argumentos inválida.")
    print("Ex.: sum 5 2 [--logfile=log_file_name]")
    sys.exit(1)

operation, n1, n2, *log_file_path = arguments
numbers = [n1, n2]
log_file_path = log_file_path[0] if log_file_path else ""

if operation not in math_operations:
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
        print(f"\nNúmero inválido: {number!r}")
        sys.exit(1)

n1, n2 = valid_numbers
result = math_operations[operation](n1, n2)
print(f"\nO resultado da operação matemática é {result}.")

if log_file_path.strip():
    if "=" in log_file_path:
        argument_key, argument_value = log_file_path.split("=")
        if argument_key.lstrip("-").strip() != "logfile":
            print(f"\nArgumento inválido: {argument_key!r}")
            sys.exit(1)
    else:
        argument_value = log_file_path

    path = os.curdir
    filepath = os.path.join(path, argument_value)
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER", "anonymous")

    with open(filepath, "a") as log_file:
        log_file.write(f"{timestamp} - {user} - "
                       f"{operation},{n1},{n2} = {result}\n")
