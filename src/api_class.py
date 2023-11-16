import os
import requests

from src.abstract_class import API


class HH_API(API):
    HH_API_URL = 'https://api.hh.ru/vacancies'
    HH_API_URL_AREAS = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword):
        super().__init__()

        self.params = {
            'per_page': 100,
            'text': keyword,
            'area': 1
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.params['per_page']}, "
                f"{self.params['text']}, {self.params['area']})")

    def get_vacancies(self):
        respons = requests.get(self.HH_API_URL, self.params)
        return respons.json()

    def format_vacancies(self, all_vacancies):
        vacancies = {'vacancies': []}
        for vacancy in all_vacancies['items']:
            if vacancy['salary'] is None:
                salary = 0
            elif vacancy['salary']['from'] is None:
                salary = vacancy['salary']['to']
            elif vacancy['salary']['to'] is None:
                salary = vacancy['salary']['from']
            else:
                salary = (vacancy['salary']['from'] + vacancy['salary']['to']) // 2
            new_job = {'name': vacancy['name'], 'url': vacancy['url'], 'salary': salary,
                       'experience': vacancy['experience']['name']}
            vacancies['vacancies'].append(new_job)
        return vacancies


class SJ_API(API):
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
    api_key = os.getenv('KEY_API')

    def __init__(self, keyword):
        super().__init__()
        self.base_url = 'https://api.superjob.ru/2.0/'

        self.params = {
            'per_page': 100,
            'text': keyword,
            'area': 1
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.params['per_page']}, "
                f"{self.params['text']}, {self.params['area']})")

    def get_vacancies(self):
        headers = {"X-Api-App-Id": self.api_key}
        respons = requests.get(self.SJ_API_URL, params=self.params, headers=headers)
        return respons.json()

    # def load_areas(self):
    #     req = requests.get(SuperJobAPI.SJ_API_URL_AREAS)
    #     dict_areas = req.json()
    #
    #     areas = {}
    #     for k in dict_areas:
    #         for i in range(len(k['areas'])):
    #             if len(k['areas'][i]['areas']) != 0:
    #                 for j in range(len(k['areas'][i]['areas'])):
    #                     areas[k['areas'][i]['areas'][j]['name'].lower()] = k['areas'][i]['areas'][j]['id']
    #             else:
    #                 areas[k['areas'][i]['name'].lower()] = k['areas'][i]['id']
    #     return areas

    def format_vacancies(self, all_vacancies):
        vacancies = {'vacancies': []}
        for vacancy in all_vacancies['objects']:
            if vacancy['payment_from'] is None and vacancy['payment_to'] is None:
                salary = "з.п. не указана"
            elif vacancy['payment_from'] is None:
                salary = vacancy['payment_to']
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']
            else:
                salary = (vacancy['payment_from'] + vacancy['payment_to']) // 2
            new_job = {'name': vacancy['profession'], 'url': vacancy['link'], 'salary': salary,
                       'experience': vacancy['experience']['title']}
            vacancies['vacancies'].append(new_job)
        return vacancies

# class IndeedAPI(API):
#   pass
#
#
# class LinkedInAPI(API):
#   pass
