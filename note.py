#!/usr/bin/env python3
"""Script de notas escrito em Python

Script que permite leitura e escrita de notas baseadas em texto simples.

EXECUÇÃO:

    python note.py [write] [read [--tag=<cadeia de caracteres a ser utilizada como filtro de tags>]]

    ou

    ./note.py [write] [read [--tag=<cadeia de caracteres a ser utilizada como filtro de tags>]]

    EX.:

        ./note.py read --tag=geral
        ./note.py write
"""

__version__ = "0.1.0"
__author__ = "Davi Cardoso"

if __name__ == "__main__":
    import os, sys

    cli_arguments = sys.argv[1:]
    file_name = "notas.txt"

    if not cli_arguments:
        print("\nQuantidade de argumentos inválida.\n\nEx.:")
        print("\tnote.py write")
        print("\tnote.py read [--tag=geral]")
        sys.exit(1)

    operation, *extra_arguments = cli_arguments

    if operation != "read" and operation != "write":
        print(f"\nOperação inválida: {operation!r}")
        sys.exit(1)

    if operation == "write":
        with open(file=file_name, mode="a") as notes_file:
            print("Para criar uma nova nota, informe:\n")
            titulo = input("Título: ")
            tag = input("Tag: ")
            texto = input("Texto: ")

            notes_file.write(f"{titulo}\t{tag}\t{texto}\n")

    if operation == "read":
        _tag, tag_filter = None, None

        if extra_arguments:
            _tag, tag_filter = extra_arguments[0].split("=")
            if not _tag.lstrip("-").strip() == "tag":
                print(f"Argumento inválido: {_tag!r}")
                sys.exit(1)

        if not file_name in os.listdir(os.curdir):
            print("\nO arquivo repositório de notas ainda não foi criado. ", end="")
            print("Execute o script em modo gravação.\nEx.: note.py write")
            sys.exit(1)

        with open(file=file_name) as notes_file:
            print()
            for line in notes_file:
                titulo, tag, texto = line.split("\t")

                if tag_filter:
                    if tag != tag_filter:
                        continue

                print(f"Título...: {titulo}\nTag......: {tag}\nTexto....: {texto}")
