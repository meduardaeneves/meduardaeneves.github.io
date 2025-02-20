import requests
import copy

class ExtractAPIValues():
    def __init__(self,link: str | None = None):
        self.link = link
    
    def extract_api(self, link):      
        questions = {}
        response = requests.get(url=link, json=questions)

        if response.status_code >= 200 and response.status_code <= 299:
            #sucesso
            response_data = response.json()
        else:
            ...
            #erros
            print(f'{response.status_code=};')
            print(f'{response.reason=};')
            print(f'{response.text=};') #html em texto

        data_list = copy.deepcopy(response_data)
        return data_list