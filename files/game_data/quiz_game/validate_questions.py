from download_questions import zero_elements, trivia_quest_cat
from pathlib import Path
import json

ROOT = Path(__file__).parent
QUESTION_FOLDER = ROOT / 'questions'
zero_questions_group = []

for i in range(trivia_quest_cat[0],trivia_quest_cat[-1]+1):
    path = QUESTION_FOLDER / f'game_questions_cat_{i}.json'
    with open(path, 'r',encoding='utf-8') as arquivo:
        dict_interesting = json.load(arquivo)
        
    # print(f'qnt dicst {i}: {len(dict_interesting)}')
    for dics in dict_interesting:
        # print(dics)
        if dict_interesting[dics] == {}:
            zero_questions_group.append(dics)
            # print(f'Sem perguntas no arquivo: {dics}')
        if dics == "[13, 'hard', 'any']":
            print(dict_interesting[dics]['Question_3'])
        if dics == "[13, 'hard', 'any']":
            print(dict_interesting[dics]['Question_5'])
print(zero_questions_group)
        
        