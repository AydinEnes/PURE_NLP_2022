"""
Dora Akbulut

Training...

Input: Texts.
Input format: 

Output:
Output format:

"""
import sys


# enes path
sys.path.insert(0, '/Users/aydo/Desktop/pure/PURE_NLP_2022/scripts')

from base_path import base_path

import os
from os import path
from spacy.lang.tr.stop_words import STOP_WORDS
import time
start_time = time.time()

print("Started")

def tokenize(sentence):
    return [token for token in sentence.split() if token not in STOP_WORDS]

# return each file as a list of strings
def get_sentences(file):
    return tokenize(file.read())

# read every file in the folder input_text_wiki and create a list for each file
def get_sentences(file_list):
    sentence_list = []
    for filename in file_list:
        with open(filename, encoding='utf-8') as fi:
            for line in fi:
                row=tokenize(line)
                sentence_list.append(row)
    return sentence_list

#           ////////////////////        change for every model         ////////////////////

foldername = "model_input_texts/chem_texts"
filename="wiki_chem_texts.txt"
filepath = path.join(base_path.PROJECT_PATH, "files", foldername , filename)
file_list = [filepath]
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "eba_chem_texts.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "limit_chem_ayt.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "limit_chem_tyt.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "meschemy_chem_9.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "meschemy_chem_10.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "semih_balmuk_chem_ayt.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "semih_balmuk_chem_tyt.txt"))
file_list.append(path.join(base_path.PROJECT_PATH, "files", foldername , "semih_balmuk_chem_organik.txt"))


sentences=get_sentences(file_list)
# print(sentences[0])

#           ////////////////////        change for every model         ////////////////////

from gensim.models.phrases import Phrases, Phraser
def build_phrases(sentences):
    phrases = Phrases(sentences,
                      min_count=10,
                      threshold=1,
                      progress_per=1000)
    return Phraser(phrases)

biagrams=build_phrases(sentences)
corpus_with_biagrams=biagrams[sentences]


def build_phrases2(sentences):
    phrases = Phrases(biagrams[sentences],
                      min_count=10,
                      threshold=1,
                      progress_per=1000)
    return Phraser(phrases)

trigrams=build_phrases2(sentences)
corpus_with_trigrams=trigrams[corpus_with_biagrams]
# print((corpus_with_trigrams[0]))

# biagrams.save('biagram_model_ds.txt')
# trigrams.save('triagram_model_ds.txt')
#phrases_model= Phraser.load('phrases_model.txt')



from gensim.utils import simple_preprocess
def create_new_corpus(file_list):
    new_corpus= []
    for filename in file_list:
        with open(filename, encoding='utf-8') as fi:
            for line in fi:
                sent = simple_preprocess(line, min_len = 2)
                recieved=(biagrams[sent])
                recieved2=trigrams[recieved]
                new_corpus.append(recieved2)
    return new_corpus
    
corpus=create_new_corpus(file_list)
# print(corpus[1])

from gensim.models import FastText
# model_ted = FastText(corpus, size=100, window=15, min_count=5,iter=10, workers=10,sg=1)
model_ted = FastText(corpus, vector_size =100, window=20, min_count=5,epochs=20, workers=10, sg=1)
# model_ted.train(corpus_iterable=corpus, total_examples=len(corpus), epochs=10)
# print(model_ted.wv.most_similar("asal_sayılar",topn=50))
print("--- %s seconds ---" % (time.time() - start_time))

print("Finished")

#           ////////////////////        change for every model         ////////////////////

model_ted.save("fasttext_chem_all.model")    

#           ////////////////////        change for every model         ////////////////////