import json
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
        Возвращает объект Python.
        """
        params = {
            'text': f'{key_word}',  # Переданное знач-е ищется в полях в-сии, ук-х в пар-ре search_field(Область поиска)
            'area': (1, 2),  # Поиск осуществляется по вакансиям города по номеру
            'page': 0,  # Номер страницы (установлено дефолтное значение)
            'per_page': 100  # Количество элементов на 1 странице (установлено дефолтное значение)
        }

        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы кириллица отображалась корректно
        json_data = json.loads(data)  # Преобразуем строку в формате JSON в объект Python
        return json_data
