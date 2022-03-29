wget https://www.softcatala.org/pub/softcatala/parallel-corpus-search/eng-cat.cat.zip
unzip eng-cat.cat.zip
grep "\.\|," tgt.txt  | grep '.\{230\}' > catalan_train.txt
wc -l catalan.txt

