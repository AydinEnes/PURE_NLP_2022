"""
Dora Akbulut

Step 2 of the NLP pipeline.

Input: Texts of certain subjects.
Input format: .txt
Read folder: step_1_topics

Output: Unigrams, bigrams and trigrams of the input texts.
Output format: .txt
Output folder: step_2_n_grams

"""

from os import path
import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams

# configure input output paths and file names
basepath = path.dirname(__file__)
project_path = path.abspath(path.join(basepath, ".."))
input_file_name = "asal_sayilar_topics.txt"
input_path = path.abspath(path.join(project_path, "files", "step_1_topics" , input_file_name))
output_path = path.abspath(path.join(project_path, "files", "step_2_n_grams" , input_file_name.split("_topics.txt")[0] + "_n_grams.txt"))

# read the input file and create the n-grams
with open(input_path, "r", encoding='utf-8') as file:
    text = file.read()
text = text.translate(str.maketrans('', '', ".,?!"))
tokenized = text.split()
unigrams = tokenized 
bigrams = ngrams(tokenized, 2)
trigrams = ngrams(tokenized, 3)


# write the n-grams to output file
with open(output_path, 'w', encoding='utf-8') as f:
    for item in unigrams:
        f.write("%s\n" % item)
    f.write('\n'.join('%s %s' % x for x in bigrams))
    f.write("\n")
    f.write('\n'.join('%s %s %s' % x for x in trigrams))