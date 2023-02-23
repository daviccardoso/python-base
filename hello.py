#! /usr/bin/env python3
"""Multilanguage 'Hello, world' script.

Based on the environment language, the script shows a message related to that language.

Usage:

The enviroment variable LANG should be properly set. E.G.:

    export LANG=pt_BR

Execution:

    python hello.py

    or

    ./hello.py
"""

__version__ = "0.1.2"
__author__ = "Davi Cardoso"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]
message = {
    "en_US": "Hello, world!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(message[current_language])

