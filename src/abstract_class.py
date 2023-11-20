from abc import ABC, abstractmethod


class API(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def load_jobs(self, keywords, location):
        pass

    @abstractmethod
    def format_vacancies(self, all_vacancies):
        pass
