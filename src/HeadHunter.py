from abc import ABC, abstractmethod

import requests


class HeadHunter(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def get_vacancies(self, key_word):
        pass


class HeadHunterAPI(HeadHunter):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru."""

    def get_vacancies(self, key_word: str) -> dict:
        """
        Метод для подключения к API и получения вакансий.
        Получает вакансии с hh.ru в формате JSON.
        """
        params = {
            'text': f'{key_word}',
            'area': (1, 2),
            'page': 0,
            'per_page': 100
        }

        request = requests.get('https://api.hh.ru/vacancies', params)
        data = request.json()
        return data
