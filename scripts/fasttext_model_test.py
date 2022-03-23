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

# print(model_ted.wv.most_similar("bakteri",topn=50))
# print("\n-------------------------------------------------------------\n")
# print(
#     model_ted.wv.most_similar(positive=["kan_hücresi"], negative=["zeus"], topn=50),
#     end="\n\n",
# )
wv = model_ted.wv
# print(wv.most_similar("canlı"))
# print(wv.doesnt_match("hücre solunum kimya organik kalp".split()))
print("-------------------------------------------------------------\n")
# print(model_ted.wv.n_similarity(["beyin"], ["zihin"]), end="\n\n")
# print("\n-------------------------------------------------------------\n")
# print(
#     model_ted.wv.doesnt_match(
#         "biyolojide metot gözlem üzerinedir ve hayvanlarla iletişimdir".split()
#     ),
#     end="\n\n",
# )
print("--- %s seconds ---" % (time.time() - start_time))