"""
Dora Akbulut

Training...

Input: Wikipedia texts.
Input format: 

Output:
Output format:

"""
from os import path
from base_path import PROJECT_PATH
from spacy.lang.tr.stop_words import STOP_WORDS

def tokenize(sentence):
    return [token for token in sentence.split() if token not in STOP_WORDS]

def get_sentences(filename):
    sentence_list = []
    with open(filename, encoding='utf-8') as fi:
      for line in fi:
        row=tokenize(line)
        sentence_list.append(row)
    
    return sentence_list
 
input_file_name = "asal sayılar.txt"
filename= path.join(PROJECT_PATH, "files", "input_wiki_txt" , input_file_name)
sentences=get_sentences(filename)
print(len(sentences))
