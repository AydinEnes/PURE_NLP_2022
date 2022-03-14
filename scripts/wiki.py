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

    full_path = os.path.join(file_path, '../files/input_wiki_txt/{}.txt'.format(topic))
    if page.exists():
        with open(full_path, 'w', encoding='utf-8') as f:
            # f.write(''.join(page.text.split()))
            string = " ".join(re.split("\s+", page.text, flags=re.UNICODE))
            string = re.sub(r'(\\+)[a-z]*', '', string)
            f.write(string)






