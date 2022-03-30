rm -r -f sepp_nlg_2021_data/
mkdir -p sepp_nlg_2021_data/ca/dev
mkdir -p sepp_nlg_2021_data/ca/train
mkdir -p sepp_nlg_2021_data/ca/test
python3 create_shared_task_data_from_text_file.py
zip -r data-ca sepp_nlg_2021_data/
