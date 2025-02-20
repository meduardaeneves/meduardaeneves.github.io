import copy

class AnswerQuestions():
    def __init__(self,dict_chosen_question):
        self.dict_chosen_question = dict_chosen_question
        self.type_question = self.dict_chosen_question['type']
    
    def define_possible_answers(self):
        total_possible_answers = []
        total_possible_answers = copy.deepcopy(self.dict_chosen_question['incorrect_answers'])
        total_possible_answers.append(self.dict_chosen_question['correct_answer'])
        total_possible_answers.sort()
        return total_possible_answers
       
    def answer_question(self):
        possible_answers = self.define_possible_answers()
        wrong_choice = True
        answer_right = True
        possible_answer_str = ''
        possible_answer_number_str = ''
        possible_answer_dict = {}
        for i, element in enumerate(possible_answers):
            possible_answer_dict[f'{i+1}'] = element
            if i == 0:
                possible_answer_str += f'  - {i+1}: {element}'
            else:
                possible_answer_str += f'\n  - {i+1}: {element}'    
            possible_answer_number_str += f' [{i+1}]'     
        print(possible_answer_str)
        print(' Chose the number related to the answer you think is correct:')
        while wrong_choice:
            answer = input(f' Type one of the following values - {possible_answer_number_str}: ').lower()
            if answer not in possible_answer_dict:
                print(' Verify your answer.')
            else:
                wrong_choice = False
        if possible_answer_dict[answer] == self.dict_chosen_question['correct_answer']:
            answer_right = True
        else:
            answer_right = False
        return answer_right          