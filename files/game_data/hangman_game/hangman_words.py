from pathlib import Path
import pandas as pd
import itertools
# word_list = ['melancia','abacaxi','escola','zebra','creche','edificio','avenida']

ROOT = Path(__file__).parent

EN_WORDS = ROOT / 'df_hangman_en.csv'
PT_WORDS = ROOT / 'df_hangman_pt.csv'

df_en = pd.read_csv(EN_WORDS)
words_en_raw = df_en.values.tolist()
words_en = list(itertools.chain(*words_en_raw))

df_pt = pd.read_csv(PT_WORDS)
words_pt_raw = df_pt.values.tolist()
words_pt = list(itertools.chain(*words_pt_raw))

# print(words_pt)
# print(len(words_pt))

# print(words_en)
# print(len(words_en))

