from set_gameplay_attributes import SetGamesAttributes
from generate_game_data import GenerateData
from answer_question_class import AnswerQuestions
from game_rules import rules
import os, random, copy, json
from pathlib import Path

data = SetGamesAttributes()
start_questions = 8


def play_trivia_game(play_again):
    
    def chose_params():
        chosen_aspects = 1
        print(f'{chosen_aspects}: CHOSE THE GAME CATHEGORY:\n')
        chosen_aspects += 1
        category_id, trivia_categories_list = data.chose_trivia_quest_categories()
        nome_categoria = ''
        for elementos in trivia_categories_list:
            if elementos['id'] == category_id:
                nome_categoria = elementos['name']  

        print(f'\n{chosen_aspects}: CHOSE THE GAME DIFFICULTY:')
        chosen_aspects += 1
        game_difficulty = data.chose_game_option_from_list('Difficulties')
        print(f'\n{chosen_aspects}: CHOSE THE GAME TYPE:')
        game_type = data.chose_game_option_from_list('Types of Game')

        ROOT = Path(__file__).parent
        QUESTION_FOLDER = ROOT / 'questions'
        path_question = QUESTION_FOLDER / f'game_questions_cat_{category_id}.json'
        with open(path_question, 'r',encoding='utf-8') as arquivo:
            dict_interesting = json.load(arquivo)
        interesting_dict_value = str([category_id,game_difficulty, game_type])
        initial_questions_dict = dict_interesting[interesting_dict_value]
        
        return category_id, nome_categoria,game_difficulty,game_type,initial_questions_dict  
    
    if play_again == 'first game':
        print('***********LETS PLAY A QUIZ GAME***********')
        print(rules)
        continue_game = input('Press any Key to star the game: ')
        os.system('cls')
    
    start_lives = 3
    questions_chosen = set()
    questions_dict = {}
    category_id, nome_categoria,game_difficulty,game_type,initial_questions_dict = chose_params() 
    
    
    if len(initial_questions_dict) == 0:
        validate_elements = False 
        while not validate_elements:
            os.system('cls')
            print('The group your parameters chosen have 0 questions. Chose another group.\n')
            category_id, nome_categoria,game_difficulty,game_type,initial_questions_dict = chose_params()
            if len(initial_questions_dict) > 0:
                validate_elements = True    
    
    if len(initial_questions_dict) > start_questions:
        all_questions = list(initial_questions_dict.keys())
        # print(all_questions)
        questions_chosen_dict = random.sample(all_questions,start_questions)
        for question in questions_chosen_dict:
            questions_dict[question] = initial_questions_dict[question]    
    else:
        questions_dict = copy.deepcopy(initial_questions_dict)
    
    # for question in questions_dict:
    #     print(question, questions_dict[question])    
    # print(questions_dict)    
    amount_questions = questions_dict.keys()
    qnt_maxima_fases = len(amount_questions) - start_lives
    
    if qnt_maxima_fases < 0:
        start_lives = 1
        qnt_maxima_fases = len(amount_questions)    
    
    qnt_acertos = 0
    fase_atual = 1
    random_question_valid = False
    continue_phases = True

    while continue_phases:
        os.system('cls')
        print('YOUR CHOICE:')
        print(f'Chosen Category: {nome_categoria} (ID - {category_id})')
        print(f'Chosen Difficulty: {game_difficulty}')
        print(f'Chosen Game Type: {game_type}')
        print(f'\nMAXIMUM LEVELS: {qnt_maxima_fases}')
        print(f'YOU ARE ON PHASE {fase_atual}')
        print(f'YOUR GAME POINTS: {qnt_acertos}')
        print(f'YOUR LIVES: {start_lives}\n')
        random_question_valid = False

        while not random_question_valid:
            random_chosen_question = random.choice(list(amount_questions))
            if random_chosen_question not in list(questions_chosen):
                questions_chosen.add(random_chosen_question)
                random_question_valid = True    

        print(f'Q.{fase_atual}: {questions_dict[random_chosen_question]['question']}')

        answer = AnswerQuestions(questions_dict[random_chosen_question])
        resposta = answer.answer_question()
        if resposta:
            qnt_acertos += 2
            fase_atual += 1
            if fase_atual > qnt_maxima_fases:
                continue_phases = False
                print('\nCongratulations, you have won all phases.')
            else:
                print('\nYou got this question right and will move on in the game.')
                move_with_game = input('Press any key to move on to the next phase: ')    
        else:
            start_lives -= 1
            qnt_acertos -= 1
            if start_lives < 1:
                print('\nYou got this question wrong and you are out of lives. Your game ends here.')
                continue_phases = False    
            else:
                print(f'\nYou got this question wrong but still have {start_lives} lives. The game will continue.')
                move_with_game = input('Press any key to move on to the next phase: ')  
             
        if not continue_phases:       
            print(f'FINAL GAME PHASE: {fase_atual} / FINAL GAME POINTS: {qnt_acertos}')

    play_new_game = input('\nDo you want to play a new game?\n[Y or YES] to play new game or anything else to exit: ').upper()
    if play_new_game != 'Y' and play_new_game != 'YES':
        return
    else:
        os.system('cls')
        play_trivia_game(play_new_game)        
    
play_trivia_game('first game')



