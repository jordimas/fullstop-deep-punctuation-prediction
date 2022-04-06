#sed 's/,//g' flores101_eng.txt  > flores101_eng_no_comas.txt
head -n 300 flores101_eng.txt > flores101_eng_small.txt
python3 inference.py
