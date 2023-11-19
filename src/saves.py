import json
import os


class JsonSave:
    all_vacancies = {}

    @staticmethod
    def delete_file():
        """Удаляет файл"""
        if os.path.exists('vacancies.json'):
            os.remove('vacancies.json')

    @classmethod
    def get_vacancies(self):
        """Записывает данные в файл"""
        with open('vacancies.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def add_vacancy():
    """Открывает созданный файл"""
    with open('vacancies.json', 'a', encoding='utf-8') as json_file:
        json.dump(JsonSave.all_vacancies, json_file, indent=4, ensure_ascii=False)
