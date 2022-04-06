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
    "-",
    "'",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "Ğ",
    "Ü",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "Ş",
    "İ",
    "Z",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
    "Ö",
    "Ç",
]


inputPaths = ["input_eba_ogm_bio_txt", "input_eba_ogm_chem_txt"]
outputPaths = ["eba_bio_texts.txt", "eba_chem_texts.txt"]

for i in range(2):
    with open(
        os.path.join(
            PROJECT_PATH,
            "files/model_input_texts/output_eba_ogm_txt",
            outputPaths[i],
        ),
        "w",
        encoding="utf-8",
    ) as w:
        for subdir, dirs, files in os.walk(
            os.path.join(PROJECT_PATH, "files", inputPaths[i])
        ):
            for file in files:

                filepath = subdir + os.sep + file

                with open(filepath, "r", encoding="utf-8") as f:

                    string = f.read()
                    string = string.translate(str.maketrans("", "", ".,?!"))
                    string = string.split()
                    for word in string:
                        if len(word) <= 1:
                            continue

                        if not all([char in charlist for char in word]):
                            continue

                        w.write(word + " ")

                    w.write("\n")
