import sys

sys.path.insert(0, 'D:\Github_Repos\morpa_nlp\PURE_NLP_2022\scripts')
import os
from os import path

from numpy import full
from base_path import base_path
import wikipediaapi
import re

import time
start_time = time.time()

print("imported")

wiki_wiki = wikipediaapi.Wikipedia(
    language="tr", extract_format=wikipediaapi.ExtractFormat.WIKI
)

file_path = os.path.dirname(__file__)
full_path = os.path.join(base_path.PROJECT_PATH, "files", "input_wiki_txt", "wiki_bio_texts2.txt")
full_path_titles = os.path.join(base_path.PROJECT_PATH, "files", "input_wiki_txt", "wiki_bio_texts2_titles.txt")

with open(full_path, "w", encoding="utf-8") as f:
    print("file created")
with open(full_path_titles, "w", encoding="utf-8") as f:
    print("file created")

def writeToText(topic, full_path):
    page = wiki_wiki.page(topic)
    string = " ".join(re.split("\s+", page.text, flags=re.UNICODE))
    string = string.lower()
    string = re.sub(r'(\\+)[a-z]*', '', string)
    string = string.translate(str.maketrans('', '', "()\{\}[]=+-.,?!1234567890"))
    string = string.split('ayrıca bakınız')[0].split('kaynakça')[0]

    if page.exists() and len(string) > 200:
        print(topic, ": ", page.exists())
        with open(full_path_titles, "a", encoding="utf-8") as f2:
            f2.write(topic + "\n")
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(string + "\n")

name_dict = {}
def findSubCats(categorymembers, full_path, level=0, max_level=2):
        for c in categorymembers.values():
            #print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
            if c.title not in name_dict and c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                name_dict[c.title] = 1
                findSubCats(c.categorymembers, full_path, level=level + 1, max_level=max_level)
            elif c.title not in name_dict and c.ns == 0: # wikipediaapi.Namespace.PAGE:
                name_dict[c.title] = 1
                writeToText(c.title, full_path)

cats = "Biyoloji Terminolojisi,Canlılar,Moleküler biyoloji teknikleri,Biyoloji tarihi,Bilimsel sınıflandırma,Biyoloji sistemleri,Biyoloji kavramları,Biyolojik etkileşimler,Biyolojinin genel alanları"
cats_list = cats.split(",")
for category in cats_list:
    cat = wiki_wiki.page("Category:{}".format(category))
    findSubCats(cat.categorymembers, full_path)

print("--- %s seconds ---" % (time.time() - start_time))
