import json
from abc import ABC, abstractmethod

import requests


class HeadHunter(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def get_vacancies(self, vacancy_name):
        pass


class HeadHunterAPI(HeadHunter):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru."""

    def get_vacancies(self, vacancy_name: str) -> dict:  # передается ключевое слово для поиска по вакансиям, н-р "Python"
        """Метод для подключения к API и получения вакансий."""
        # Получение вакансий с hh.ru в формате JSON
        params = {
            'text': f'NAME:{vacancy_name}',  # Текст фильтра. В имени должно быть слово, н-р, "Python"
            'area': 2,  # Поиск осуществляется по вакансиям города С-П
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы кириллица отображалась корректно
        with open('data_vacancy.json', 'w') as json_file:
            json_file.write(data)
            with open('data_vacancy.json') as file:
                vacancy_data = json.load(file)
                return vacancy_data
