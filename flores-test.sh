head -n 300 flores101_cat.txt > flores101_cat_small.txt
python3 inference.py
#diff -u flores101_cat_small.txt output.txt > small.txt
#python3 diff.py
