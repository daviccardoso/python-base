#! /usr/bin/env python3
"""Multilanguage 'Hello, world' script.

Based on the environment language, the script shows a message related to that language.

Usage:

The enviroment variable LANG should be properly set. E.G.:

    export LANG=pt_BR
    
    or

    provide a language for the argument `--lang`

    or

    pick a language during runtime

Execution:

    python hello.py

    or

    ./hello.py
"""

__version__ = "0.1.3"
__author__ = "Davi Cardoso"
__license__ = "Unlicense"


import os, sys

arguments = {"lang": None, "count": 1}

for argument in sys.argv[1:]:
    key, value = argument.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option: {key!r}")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Pick a language, please: ")

current_language = current_language[:5]

message = {
    "en_US": "Hello, world!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(f"\n{message[current_language]}" * int(arguments["count"]))
