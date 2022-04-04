#wget https://www.softcatala.org/pub/softcatala/parallel-corpus-search/eng-cat.cat.zip
#unzip eng-cat.cat.zip
#grep "\.\|," tgt.txt  | grep '.\{230\}' > catalan.txt
grep '.\{50\}' tgt.txt > catalan.txt
grep '.\{50\}' gencat-corpus.txt >> catalan.txt
wc -l catalan.txt

