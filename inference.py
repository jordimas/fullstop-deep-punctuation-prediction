# -*- coding: utf-8 -*-

import datetime
from punctuationmodel import PunctuationModel


def do_inference(ref_lines, lines, output, file_type):

    with open(output, 'w') as ot:

        model = PunctuationModel()

        cnt = 0
        equal = 0
        diff = 0
        for idx in range(0, len(lines)):
            line = lines[idx].strip()
            ref_line = ref_lines[idx].strip()
        
            line = line.strip()
            if len(line) == 0:
                continue

#            print(f"source: '{line}'")
            line = model.restore_punctuation(line)

            ot.write(line + "\n")
            cnt += 1

            if cnt % 100 == 0:
                print(cnt)

#            print(f"{line == ref_line} - '{ref_line}' - '{line}'")
            if line == ref_line:
                equal += 1
            else:
                diff += 1

    pequal = equal * 100 / (diff+equal)
    print(f"Sentences: for {file_type} equal {equal}  ({pequal:.2f}%), diff {diff}")


if __name__ == "__main__":

    start_time = datetime.datetime.now()

    with open('flores101_cat_small.txt', 'r') as fp:
        lines = fp.readlines()
    
    with open('flores101_cat_no-comas.txt', 'w') as fp:
        processed_lines = []
        for line in lines:
            line = line.replace(",", "")
            fp.write(line)
            processed_lines.append(line)

        do_inference(lines, processed_lines, "output-no-commas.txt", "no commas")

    with open('flores101_cat_no-comas-no-dots.txt', 'w') as fp:
        processed_lines = []
        for line in lines:
            line = line.replace(",", "")
            line = line.replace(".", "")
            fp.write(line)
            processed_lines.append(line)

        do_inference(lines, processed_lines, "output-flores101_cat_no-comas-no-dots.txt", "no commas and no dots")

    s = 'Time used: {0}'.format(datetime.datetime.now() - start_time)
    print(s)
