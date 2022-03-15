from base_path import PROJECT_PATH
import wikipediaapi
import os
import re

print('imported')

wiki_wiki = wikipediaapi.Wikipedia(
        language='tr',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

topic_list = ['asal sayılar' , 'doğal sayılar', 'karmaşık sayılar', 'toplama', 'çarpma', 'kümeler', 'modüler aritmetik']

file_path = os.path.dirname(__file__)

for topic in topic_list:
    page = wiki_wiki.page(topic)
    print(topic, ": " , page.exists())

    # full_path = os.path.join(file_path, '../files/input_wiki_txt/{}.txt'.format(topic.replace(' ', '_')))
    full_path = os.path.join(PROJECT_PATH, "files", "input_wiki_txt", "wiki_texts.txt")
    if page.exists():
        with open(full_path, 'a', encoding='utf-8') as f:
            string = " ".join(re.split("\s+", page.text, flags=re.UNICODE))
            string = string.lower()
            string = re.sub(r'(\\+)[a-z]*', '', string)
            string = string.translate(str.maketrans('', '', "()\{\}[]=+-.,?!"))
            string = string.split('ayrıca bakınız')[0].split('kaynakça')[0]
            f.write(string + "\n")






