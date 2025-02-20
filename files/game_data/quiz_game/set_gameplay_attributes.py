from extract_api import ExtractAPIValues
from pathlib import Path
import json

class SetGamesAttributes(ExtractAPIValues):
    
    avaliable_difficulties = ['easy','medium','hard']
    possible_type_questions = ['any','multiple','boolean']
       
    def __init__(self,link: str | None = None):
        super().__init__(link)
        self.url_categories = 'https://opentdb.com/api_category.php'
    
    def chose_trivia_quest_categories(self):
        trivia_quest_categories = []
        
        # avaliable_categories = super().extract_api(self.url_categories)        
        # for element in avaliable_categories.values():
        #     for trivia_quests in element:
        #         trivia_quest_categories.append(trivia_quests)
        
        trivia_quest_cat = [x for x in range(9,33)]
        ROOT = Path(__file__).parent
        QUESTION_FOLDER = ROOT / 'questions'
        index_wanted = 9 - trivia_quest_cat[0]
        for i in range(trivia_quest_cat[0],trivia_quest_cat[-1]+1):
            # index_wanted = i - trivia_quest_cat[0]
            question = index_wanted + 1
            name_question = f'Question_{question}'

            new_cat = {}
            path_question = QUESTION_FOLDER / f'game_questions_cat_{i}.json'
            with open(path_question, 'r',encoding='utf-8') as arquivo:
                dict_interesting = json.load(arquivo)
            # print(dict_interesting)
            dict_interesting_keys = list(dict_interesting.keys())
            # print(dict_interesting_keys)
            dict_interesting_0 = dict_interesting_keys[index_wanted]

            name = dict_interesting[dict_interesting_0][name_question]['category']
            new_cat['id'] = i
            new_cat['name'] = name
            trivia_quest_categories.append(new_cat)
        
        
        # print(trivia_quest_categories)
        print('AVALIABLE CATEGORIES AND THEIR ID:')
        for i in range(len(trivia_quest_categories)):
            print(f'ID - {trivia_quest_categories[i]['id']} / Name -  {trivia_quest_categories[i]['name']}')
        
        correct_id_chosen = False
        while not correct_id_chosen:
            id_chosen_str = input(f'\nChose a valid ID from ({trivia_quest_categories[0]['id']} - {trivia_quest_categories[-1]['id']}): ')
            try:
                id_chosen_int = int(id_chosen_str)
                if id_chosen_int < trivia_quest_categories[0]['id'] or id_chosen_int > trivia_quest_categories[-1]['id']:
                    print('You chose an number out of range')
                else:
                    correct_id_chosen = True
            except:
                print('You did not inserted a valid number.')

        return id_chosen_int, trivia_quest_categories

    def chose_game_option_from_list(self,type_attribute_list):
        avaliable_element_str = ''
        element_str = ''
        if type_attribute_list == 'Difficulties':
            list = SetGamesAttributes.avaliable_difficulties
            element_str = 'difficulty'
        elif type_attribute_list == 'Types of Game':
            list = SetGamesAttributes.possible_type_questions
            element_str = 'type'
            
        for item in list:
            avaliable_element_str += f' [{item}]'
        print(f' - Avaliable {type_attribute_list}:{avaliable_element_str}')
        wrong_choice = True
        while wrong_choice:
            choice = input(f' - Chose the {element_str} of the game you will like to play: ').lower()
            if choice not in list:
                print(' Verify your answer.')
            else:
                wrong_choice = False
        return choice
