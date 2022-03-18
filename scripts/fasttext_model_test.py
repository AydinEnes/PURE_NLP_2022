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

from gensim.models import FastText
import gensim

model_ted = gensim.models.FastText.load("fasttext_ds.model")

print(model_ted.wv.most_similar("bakteri",topn=50))
print("--- %s seconds ---" % (time.time() - start_time))