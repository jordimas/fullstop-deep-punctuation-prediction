# -*- coding: utf-8 -*-

import sys
import datetime

import logging

if __name__ == "__main__":

    start_time = datetime.datetime.now()

    with open('flores101_eng_small.txt', 'r') as source_fp, open ('output.txt', 'r') as target_fp:
        sources = source_fp.readlines()
        targets = target_fp.readlines()

        equal = 0
        diff = 0
        for idx in range(0, len(sources)):
            source = sources[idx].strip()
            target = targets[idx].strip()

            if source == target:
                equal += 1
            else:
                diff += 1
                print(f"s: {source}")
                print(f"t: {target}")

        pequal = equal * 100 / (diff+equal)
        print(f"Sentences: equal {equal}  ({pequal:.2f}%), diff {diff}")

