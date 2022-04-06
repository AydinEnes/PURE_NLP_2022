from numpy import unicode_
from base_path import PROJECT_PATH
import os
import re


# charlist2 = [
#     "(",
#     ")",
#     "\\",
#     "{",
#     "\\",
#     "}",
#     "[",
#     "]",
#     "=",
#     "+",
#     "-",
#     ".",
#     ",",
#     "?",
#     "!",
#     "1",
#     "2",
#     "3",
#     "4",
#     "5",
#     "6",
#     "7",
#     "8",
#     "9",
#     "0",
#     " ̇",
#     "ï",
#     "¿",
#     "½",
#     "€",
#     "¢",
# ]

charlist = [
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "ğ",
    "ü",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "ş",
    "i",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
    "ö",
    "ç",
]

with open(
    os.path.join(
        PROJECT_PATH,
        "files/model_input_texts/output_eba_ogm_txt/eba_bio_texts.txt",
    ),
    "w",
    encoding="utf-8",
) as w:
    for subdir, dirs, files in os.walk(
        os.path.join(PROJECT_PATH, "files/input_eba_ogm_bio_txt")
    ):
        for file in files:

            filepath = subdir + os.sep + file

            with open(filepath, "r", encoding="utf-8") as f:

                string = f.read()
                string = string.split()
                for word in string:
                    word = word.lower()
                    if len(word) <= 1:
                        continue

                    if not all([char in charlist for char in word]):
                        continue

                    w.write(word + " ")

                w.write("\n")
