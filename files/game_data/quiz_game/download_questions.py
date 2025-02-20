from itertools import product
from generate_game_data import GenerateData
import time
import json
from pathlib import Path

trivia_quest_cat = [x for x in range(9,33)]
trivia_difficulties = ['easy','medium','hard']
trivia_type_questions = ['any','multiple','boolean']

final_list_elements = [list(x) for x in product(trivia_quest_cat, trivia_difficulties, trivia_type_questions)]
print(f'Quantidade de grupos de questões: {len(final_list_elements)}')

complete_question_dict = {}
start_questions = 25

def create_url(type_question,list_element,amount_questions):
    if type_question == 'any':
        url = f'https://opentdb.com/api.php?amount={amount_questions}&category={list_element[0]}&difficulty={list_element[1]}&encode=base64' 
    else:      
        url = f'https://opentdb.com/api.php?amount={amount_questions}&category={list_element[0]}&difficulty={list_element[1]}&type={list_element[2]}&encode=base64'   
    return url  

# generate_data = GenerateData(start_questions,final_list_elements[17][0],final_list_elements[17][1], final_list_elements[17][2])
# questions_dict = generate_data.generate_data_questions()

# element_list = [final_list_elements[17][0],final_list_elements[17][1],final_list_elements[17][2]]
# print(element_list)
# str_element_list = str(element_list)

# complete_question_dict[str_element_list] = questions_dict
# print(complete_question_dict)

ROOT_PATH = Path(__file__).parent
NEW_PATH = ROOT_PATH / 'questions'
# NEW_PATH = ROOT_PATH / "game_questions.json"
zero_elements = []

if __name__ == '__main__':
    qnt = 1
    qnt_per_cat = 1
    max_cat = 10
    actual_amount_cat = 13
    cat_questions_dict = {}
    for elements in final_list_elements:

        actual_category = trivia_quest_cat[actual_amount_cat-9]
        category = elements[0]
        # question_path = NEW_PATH / f"game_questions_cat{category}.json"
        if category == actual_category:
            if qnt_per_cat < max_cat:
                generate_data = GenerateData(start_questions,elements[0],elements[1], elements[2])    
                questions_dict = generate_data.generate_data_questions()
                element_list = [elements[0],elements[1],elements[2]]
                
                if questions_dict == {}:
                    zero_elements.append(element_list)   
                     
                str_element_list = str(element_list)
                
                cat_questions_dict[str_element_list] = questions_dict
                # complete_question_dict[str_element_list] = questions_dict
                print(f'{qnt} - {elements} - ok')
                qnt += 1
                time.sleep(10)
                qnt_per_cat += 1
                
            if qnt_per_cat == max_cat:
                question_path = NEW_PATH / f"game_questions_cat_{category}.json"
                with open(question_path, "w") as arquivo:
                    json.dump(cat_questions_dict, arquivo, indent=4)
                cat_questions_dict = {}    
                qnt_per_cat = 1
                actual_amount_cat += 1

