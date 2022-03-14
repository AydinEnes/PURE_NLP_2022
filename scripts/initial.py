from gensim.models import FastText
from gensim.test.utils import common_texts  # some example sentences

def Similarity(w1,w2,model):
    A = model[w1]; B = model[w2]
    return sum(A*B)/ pow(sum(pow(A,2)),0.5)* pow(sum(pow(B,2)),0.5)

print(common_texts[0])
['human', 'interface', 'computer']
print(len(common_texts))
9
model = FastText(vector_size=4, window=3, min_count=1)  # instantiate
model.build_vocab(corpus_iterable=common_texts)
model.train(corpus_iterable=common_texts, total_examples=len(common_texts), epochs=10)  # train
# print(model.wv.similarity('computer', 'human'))
# print(model.wv.similarity('computer', 'animal'))
# print(model.wv.similarity('human', 'animal'))
print(Similarity('human', 'animal', model))
print(Similarity('computer', 'animal', model))
print(Similarity('human', 'computer', model))