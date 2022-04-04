import random
from collections import Counter
from sklearn.model_selection import train_test_split
import re

RAND_SEED = 42
random.seed(RAND_SEED)
RELEVANT_PUNCT = {'.', ',', '?', '-', ':', '!', ';'}
PUNCT_MAP = {'!': '.', ';': '.'}


'''
    This method decided how you want to tokenize your sentence into words
    This is language dependent
'''

import spacy
nlp = spacy.load("ca_core_news_lg")
def tokenize_sentence_into_words(sentence):

    doc = nlp(sentence)  # phrase to tokenize
    words = []
    for word in doc:
        words.append(word.text)

    return words

def to_tsv(lines, filename: str):
    label_counts = Counter()
    
    with open(filename, 'w', encoding='utf8') as output_fh:
        prev = None
        for line in lines:
            line = line.lower()
            if '\"' in line:
                continue

            for tok in tokenize_sentence_into_words(line):
                tok = tok.strip()
                if len(tok) == 0:
                    continue

                if prev == None:
                    prev = tok
                    continue

                if tok == '.':
                    t1_label = 1
                else:
                    t1_label = 0

                if tok in RELEVANT_PUNCT:  # subtask 2 label
                    t2_label = tok
                    label_counts[tok] += 1
                else:
                    t2_label = 0

                s = f'{prev}\t{t1_label}\t{t2_label}'
                output_fh.write(s+ "\n")

                if tok in RELEVANT_PUNCT:  # subtask 2 label
                    prev = None
                else:
                    prev = tok
            
    print(filename)
    for label, cnt in label_counts.most_common():
        print(label, cnt)


def dev_test_train(text_file: str, outpath: str):

    with open(text_file, "r") as textfile_fh:
        lines = textfile_fh.readlines()
        random.shuffle(lines)

        train_lines, test_lines = train_test_split(lines, test_size=.16, random_state=RAND_SEED)
        train_lines, dev_lines = train_test_split(train_lines, test_size=.2, random_state=RAND_SEED)

        to_tsv(train_lines, "sepp_nlg_2021_data/ca/train/train.tsv")
        to_tsv(dev_lines, "sepp_nlg_2021_data/ca/dev/dev.tsv")
        to_tsv(test_lines, "sepp_nlg_2021_data/ca/test/test.tsv")

    print(f"Wrote zip into {outpath} using {text_file} as input corpus")

if __name__ == '__main__':

    dev_test_train('europarl.en-ca.ca',  outpath='data/sepp_nlg_2021_data/')

