import random
from collections import Counter
from sklearn.model_selection import train_test_split
import re

RAND_SEED = 42
random.seed(RAND_SEED)
RELEVANT_PUNCT = {'.', ',', '?', '-', ':', '!', ';'}
PUNCT_MAP = {'!': '.', ';': '.'}

WORD_SPLIT = '(\.|,|\?|-|:|!|;| )'

def to_tsv(lines, filename: str):
    label_counts = Counter()
    
    with open(filename, 'w', encoding='utf8') as output_fh:
        for line in lines:
            for tok in re.split(WORD_SPLIT, line):

                if len(tok.strip()) == 0:
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

                s = f'{tok}\t{t1_label}\t{t2_label}'
#                print(s)
                output_fh.write(s+ "\n")

    print(filename)
    for label, cnt in label_counts.most_common():
        print(label, cnt)


def dev_test_train(text_file: str, outpath: str):

    with open(text_file, "r") as textfile_fh:
        lines = textfile_fh.readlines()
        random.shuffle(lines)

        train_lines, test_lines = train_test_split(lines, test_size=.16, random_state=RAND_SEED)
        train_lines, dev_lines = train_test_split(train_lines, test_size=.2, random_state=RAND_SEED)

        to_tsv(train_lines, "ca/train/train.tsv")
        to_tsv(dev_lines, "ca/dev/dev.tsv")
        to_tsv(test_lines, "ca/test/test.tsv")

if __name__ == '__main__':
    dev_test_train('catalan.txt',  outpath='data/sepp_nlg_2021_data/')


#    create_europarl_data('data/de.zip', lang='de', outdir='data/sepp_nlg_2021_data/')
#    create_europarl_data('data/fr.zip', lang='fr', outdir='data/sepp_nlg_2021_data/')
#    create_europarl_data('data/it.zip', lang='it', outdir='data/sepp_nlg_2021_data/')
