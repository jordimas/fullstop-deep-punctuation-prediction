rm -r -f ca/
mkdir -p ca/dev
mkdir -p ca/train
mkdir -p ca/test
python3 create_shared_task_data_from_text_file.py
zip -r data-ca ca/
