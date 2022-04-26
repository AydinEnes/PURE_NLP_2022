"""
Dora Akbulut

Training...

Input: Wikipedia texts.
Input format: 

Output:
Output format:

"""
import sys

# enes path
# sys.path.insert(0, '/Users/aydo/Desktop/pure/PURE_NLP_2022/scripts')
sys.path.insert(0, 'D:\Github_Repos\morpa_nlp\PURE_NLP_2022\scripts')

import os
from os import path
from base_path import base_path
from spacy.lang.tr.stop_words import STOP_WORDS
import time
start_time = time.time()

from gensim.models import FastText
import gensim


#           ////////////////////        change accordingly          ////////////////////
model_ted = gensim.models.FastText.load("fasttext_bio_all.model")

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
    cat_score = 0
    cat_count = 0
    cat_1_acc = 0
    wv = model.wv
    with open(file, encoding='utf-8') as f:
        for line in f:
            if line == "\n":
                continue
            elif line.split()[0] != "DIFFICULTY":
                prediction = wv.doesnt_match(line.strip().split())
                correct = line.strip().split()[0]
                print("prediction:", prediction + "\tcorrect:", correct)
                count = count + 1
                cat_count += 1
                if (prediction == correct):
                    score += 1
                    cat_score += 1
            else:
                if cat_count != 0:
                    cat_1_acc = cat_score/cat_count * 100
                cat_count = 0
                cat_score = 0
                print("----------------------------------")
                print(line.strip())

    # print("Score: {} out of {}: \n{}%".format(score, count, 100*score/count))
    acc = "{:.2f}".format(100*score/count)
    cat_1_acc= "{:.2f}".format(cat_1_acc)
    cat_2_acc = "{:.2f}".format(100*cat_score/cat_count)
    print(f"Score: {score} out of {count}\nAccuracy: {acc}%")
    print(f"Category 1 accuracy: {cat_1_acc}%")
    print(f"Category 2 accuracy: {cat_2_acc}%")

#           ////////////////////        change accordingly          ////////////////////
filename = path.join(base_path.PROJECT_PATH, "files", "tests", "test_bio_model.txt")
test_model(model_ted, filename)

print("--- %s seconds ---" % (time.time() - start_time))