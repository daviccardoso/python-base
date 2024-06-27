#!/usr/bin/env python3

def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""

    final_word = ""

    for letter in word:
        if letter.lower() in "aeiouãõâôêéáíóú":
            final_word = letter * 2
        else:
            final_word = letter

    return final_word

print(repete_vogal("banana"))
