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

__version__ = "0.0.1"
__author__ = "Davi Cardoso"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]
message = "Hello, world!"

if current_language == "pt_BR":
    message = "Olá, mundo!"
elif current_language == "it_IT":
    message = "Ciao, mondo!"

print(message)
