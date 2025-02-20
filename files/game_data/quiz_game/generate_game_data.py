from extract_api import ExtractAPIValues
import copy
import base64
from time import sleep

class GenerateData(ExtractAPIValues):
    def __init__(self,amount_questions,id_chosen,game_dificulty,type_questions,link: str | None = None):
        super().__init__(link)
        self.amount_questions = amount_questions
        self.id_chosen = id_chosen
        self.game_dificulty = game_dificulty
        self.type_questions = type_questions
        #the keys are the names and the responses the values:
        self.dict_trivia = {
            'trivia_amount': self.amount_questions,
            'trivia_category': str(self.id_chosen), 
            'trivia_difficulty': self.game_dificulty,
            'trivia_type': self.type_questions,
        }
    
    def create_url(self,qnt_questions):
        if self.type_questions == 'any':
            url = f'https://opentdb.com/api.php?amount={qnt_questions}&category={self.id_chosen}&difficulty={self.game_dificulty}&encode=base64' 
        else:      
            url = f'https://opentdb.com/api.php?amount={qnt_questions}&category={self.id_chosen}&difficulty={self.game_dificulty}&type={self.type_questions}&encode=base64'   
        return url
    
    def generate_data_questions(self):
        link_url_initial = self.create_url(1)
        response_data_initial = super().extract_api(link_url_initial) 
        
        if response_data_initial['response_code'] == 1:
            reduce_number_questions = False
            return {}
        else:           
            sleep(10)
            reduce_number_questions = True
            link_url = self.create_url(self.amount_questions)
            response_data = super().extract_api(link_url)   
                      
        while reduce_number_questions:
            if response_data['response_code'] == 1: 
                sleep(10)
                self.amount_questions -= 1
                self.dict_trivia['trivia_amount'] = self.amount_questions
                link_url = self.create_url(self.amount_questions)
                # print(link_url)
                response_data = super().extract_api(link_url)
                # sleep(10)
                if self.amount_questions == 0:
                    reduce_number_questions = False    
            elif response_data['response_code'] == 0:
                reduce_number_questions = False

        if self.amount_questions != 0:
            data_list = copy.deepcopy(response_data['results'])
            data_list_elements = set()

            for i,element in enumerate(data_list):
                for item in element:
                    if type(data_list[i][item]) == list:
                        for element in range(len(data_list[i][item])):
                            data_list[i][item][element] = base64.b64decode(data_list[i][item][element]).decode('utf-8')            
                    else:
                        data_list[i][item] =  base64.b64decode(data_list[i][item]).decode('utf-8')    
                    data_list_elements.add(item)
                    
            questions_dict = {}
            for i,element in enumerate(data_list):
                questions_dict[f'Question_{(i+1)}'] = data_list[i]
        # else:
        #     questions_dict = {}
        
        return questions_dict