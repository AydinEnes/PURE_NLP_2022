"""
Dora Akbulut

Training...

Input: Wikipedia texts.
Input format: 

Output:
Output format:

"""
import os
from os import path
from base_path import PROJECT_PATH
from spacy.lang.tr.stop_words import STOP_WORDS
import time
start_time = time.time()

def tokenize(sentence):
    return [token for token in sentence.split() if token not in STOP_WORDS]

# return each file as a list of strings
def get_sentences(file):
    return tokenize(file.read())

# read every file in the folder input_text_wiki and create a list for each file
def get_sentences(filename):
    sentence_list = []
    with open(filename, encoding='utf-8') as fi:
      for line in fi:
        row=tokenize(line)
        sentence_list.append(row)
    
    return sentence_list
      
filename="wiki_texts.txt"
filepath = path.join(PROJECT_PATH, "files", "input_wiki_txt", filename)
sentences=get_sentences(filepath)
# print(sentences[0])

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
def create_new_corpus(filename):
    new_corpus= []
    with open(filename, encoding='utf-8') as fi:
      for line in fi:
        sent = simple_preprocess(line, min_len = 2)
        recieved=(biagrams[sent])
        recieved2=trigrams[recieved]
        new_corpus.append(recieved2)
    
    return new_corpus
    
corpus=create_new_corpus(filepath)
# print(corpus[1])

from gensim.models import FastText
# model_ted = FastText(corpus, size=100, window=15, min_count=5,iter=10, workers=10,sg=1)
model_ted = FastText(corpus, vector_size =100, window=15, min_count=5,epochs=10, workers=10,sg=1)
# model_ted.train(corpus_iterable=corpus, total_examples=len(corpus), epochs=10)
print(model_ted.wv.most_similar("asal_sayılar",topn=50))
print("--- %s seconds ---" % (time.time() - start_time))