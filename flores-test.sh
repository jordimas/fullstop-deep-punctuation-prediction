#sed 's/,//g' flores101_cat.txt  > flores101_cat_no_comas.txt
#head -n 20 flores101_cat.txt > flores101_cat_small.txt
#head -n 20 flores101_cat_no_comas.txt > flores101_cat_no-comas_small.txt
python3 inference.py
#diff -u flores101_cat_small.txt output.txt > small.txt
python3 diff.py
