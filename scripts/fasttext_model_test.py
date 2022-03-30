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
#     model_ted.wv.most_similar(positive=["yumurta", "doğum"], negative=["memeli"], topn=50),
#     end="\n\n",
# )
wv = model_ted.wv
# print(wv.most_similar("canlı"))
# print(wv.doesnt_match("inek kedi köpek tavuk yumurta".split()))
# print("-------------------------------------------------------------\n")
# print(model_ted.wv.n_similarity(["yumurta", "doğum"], ["memeli"]), end="\n\n")
# print("\n-------------------------------------------------------------\n")
# print(
#     model_ted.wv.doesnt_match(
#         "biyolojide metot gözlem üzerinedir ve hayvanlarla iletişimdir".split()
#     ),
#     end="\n\n",
# )

def test_model(model, file):
    score = 0
    count = 0
    wv = model.wv
    with open(file, encoding='utf-8') as f:
        for line in f:
            if line.split()[0] != "DIFFICULTY":
                prediction = wv.doesnt_match(line.strip().split())
                correct = line.strip().split()[0]
                print("prediction:", prediction + "\tcorrect:", correct)
                count = count + 1
                if (prediction == correct):
                    score += 1
            else:
                print("----------------------------------")
                print(line.strip())
    print("Score: " + str(score) + " out of " + str(count))


filename = path.join(PROJECT_PATH, "files", "input_wiki_txt", "test_model.txt")
test_model(model_ted, filename)

print("--- %s seconds ---" % (time.time() - start_time))