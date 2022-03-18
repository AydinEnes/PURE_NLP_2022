from numpy import full
from base_path import PROJECT_PATH
import wikipediaapi
import os
import re

import time
start_time = time.time()

print("imported")

wiki_wiki = wikipediaapi.Wikipedia(
    language="tr", extract_format=wikipediaapi.ExtractFormat.WIKI
)

file_path = os.path.dirname(__file__)
full_path = os.path.join(PROJECT_PATH, "files", "input_wiki_txt", "wiki_bio_texts.txt")

with open(full_path, "w", encoding="utf-8") as f:
    print("file created")

def writeToText(topic, full_path):
    page = wiki_wiki.page(topic)
    print(topic, ": ", page.exists())

    if page.exists():
        with open(full_path, "a", encoding="utf-8") as f:
            string = " ".join(re.split("\s+", page.text, flags=re.UNICODE))
            string = string.lower()
            string = re.sub(r'(\\+)[a-z]*', '', string)
            string = string.translate(str.maketrans('', '', "()\{\}[]=+-.,?!1234567890"))
            string = string.split('ayrıca bakınız')[0].split('kaynakça')[0]
            f.write(string + "\n")


def findSubCats(categorymembers, full_path, level=0, max_level=2):
        for c in categorymembers.values():
            #print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                findSubCats(c.categorymembers, full_path, level=level + 1, max_level=max_level)
            elif c.ns == 0: # wikipediaapi.Namespace.PAGE:
                writeToText(c.title, full_path)

cats = "Biyoloji Terminolojisi,Canlılar,Moleküler biyoloji teknikleri,Biyoloji tarihi,Bilimsel sınıflandırma,Biyoloji sistemleri,Biyoloji kavramları,Biyolojik etkileşimler,Biyolojinin genel alanları"
cats_list = cats.split(",")
for category in cats_list:
    cat = wiki_wiki.page("Category:{}".format(category))
    findSubCats(cat.categorymembers, full_path)

print("--- %s seconds ---" % (time.time() - start_time))
