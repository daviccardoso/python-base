#!/usr/bin/env python3

formatted_words_list = []
vowels = (
    "a",
    "á",
    "à",
    "ã",
    "ä",
    "e",
    "é",
    "è",
    "ë",
    "i",
    "í",
    "ì",
    "ï",
    "o",
    "ó",
    "ò",
    "õ",
    "ö",
    "u",
    "ú",
    "ù",
    "ü",
)

while True:
    word = input("Digite uma palavra ou ENTER para sair: ").strip("")

    if not word:
        break

    final_word = ""

    for letter in word:
        final_word += letter * 2 if letter.lower() in vowels else letter

    formatted_words_list.append(final_word)

print()
print(*formatted_words_list, sep="\n")
