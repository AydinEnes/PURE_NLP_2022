from gensim.test.utils import datapath
from gensim.models import FastText
from gensim.utils import tokenize
from gensim import utils

class MyIter:
    def __iter__(self):
        path = datapath('crime-and-punishment.txt')
        with utils.open(path, 'r', encoding='utf-8') as fin:
            for line in fin:
                yield list(tokenize(line))

model4 = FastText(vector_size=4, window=3, min_count=1)
model4.build_vocab(sentences=MyIter())