# -*- coding: utf-8 -*-

import sys
import datetime

import logging
from punctuationmodel import PunctuationModel

if __name__ == "__main__":

    start_time = datetime.datetime.now()

    with open('flores101_cat_no-comas_small.txt', 'r') as fp:
        test_sample = fp.readlines()

    with open('output.txt', 'w') as ot:

        model = PunctuationModel()

        for line in test_sample:
            line = line.strip()
            if len(line) == 0:
                continue

            print(f"source: '{line}'")
            punctuated = model.restore_punctuation(line)

            ot.write(punctuated + "\n")
            
            print(f"result: '{punctuated}'")
            print("--")

    s = 'Time used: {0}'.format(datetime.datetime.now() - start_time)
    print(s)
